"""Photonic component library."""


import gdsfactory as gf
from gdsfactory import cell, get_component


@cell
def _dbr_cell(
    w1: float = 0.5,
    w2: float = 0.65,
    l1: float = 0.288,
    l2: float = 0.288,
    straight: gf.types.ComponentSpec = gf.components.straight,
) -> gf.Component:
    """Distributed Bragg Reflector unit cell.

    Args:
        w1: thin width in um.
        l1: thin length in um.
        w2: thick width in um.
        l2: thick length in um.
        n: number of periods.
        straight: spec in um.

    .. code::

           l1      l2
        <-----><-------->
                _________
        _______|

          w1       w2
        _______
               |_________
    """
    l1 = gf.snap.snap_to_grid(l1)
    l2 = gf.snap.snap_to_grid(l2)
    w1 = gf.snap.snap_to_grid(w1, 2)
    w2 = gf.snap.snap_to_grid(w2, 2)
    c = gf.Component()
    c1 = c << get_component(straight, length=l1, width=w1, cross_section="nitride")
    c2 = c << get_component(straight, length=l2, width=w2, cross_section="strip")
    c2.connect(port="o1", destination=c1.ports["o2"])
    c.add_port("o1", port=c1.ports["o1"])
    c.add_port("o2", port=c2.ports["o2"])
    return c


@gf.cell
def dbr() -> gf.Component:
    """Distributed Bragg Reflector.

    .. code::

    0.288um 0.288um
    <-------><------>
    ________        _______
    |       |_______|
    |       |       |
    | 0.5um | 0.65um|       ...  10 times
    |       |_______|
    |_______|       |_______
    """
    c = gf.Component()
    l1 = gf.snap.snap_to_grid(0.288)
    l2 = gf.snap.snap_to_grid(0.288)
    cell = _dbr_cell()
    c.add_array(cell, columns=10, rows=1, spacing=(l1 + l2, 100))
    starting_rect = c << gf.get_component(
        "straight", length=l2, width=0.65, cross_section="strip"
    )
    starting_rect.move(starting_rect.center, (-0.144, 0))
    c.add_port("o1", port=starting_rect.ports["o1"])
    p1 = c.add_port("o2", port=cell.ports["o2"])
    p1.center = [(l1 + l2) * 10, 0]
    return c


if __name__ == "__main__":
    import gdsfactory as gf

    c = dbr()
    c.show()
    print(c.to_yaml())
