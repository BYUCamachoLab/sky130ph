"""Photonic component library."""


import gdsfactory as gf
import gdsfactory.components as gc
from gdsfactory import Component, cell
from gdsfactory.snap import snap_to_grid
from gdsfactory.types import ComponentSpec

# coupler_lengths = {
#   power_ratio: {
#       gap: coupling_length
#   }
# }
coupler_lengths = {
    0.1: {0.15: 3.74, 0.2: 6.03, 0.25: 13.66, 0.3: 21.24},
    0.2: {0.15: 5.39, 0.2: 8.68, 0.25: 19.68, 0.3: 30.61},
    0.3: {0.15: 6.74, 0.2: 10.85, 0.25: 24.61, 0.3: 38.27},
    0.4: {0.15: 7.96, 0.2: 12.82, 0.25: 29.07, 0.3: 45.2},
    0.5: {0.15: 9.14, 0.2: 14.71, 0.25: 33.34, 0.3: 51.85},
    0.6: {0.15: 10.31, 0.2: 16.59, 0.25: 37.61, 0.3: 58.49},
    0.7: {0.15: 11.53, 0.2: 18.56, 0.25: 42.07, 0.3: 65.43},
    0.8: {0.15: 12.88, 0.2: 20.73, 0.25: 47.0, 0.3: 73.09},
    0.9: {0.15: 14.53, 0.2: 23.39, 0.25: 53.02, 0.3: 82.46},
    1.0: {0.15: 18.27, 0.2: 29.42, 0.25: 66.68, 0.3: 103.7},
}


adiabatic_bend_90_p_values = {1.0: 0.2, 2.0: 0.8, 3.0: 0.2, 4.0: 0.8, 5.0: 0.8}


@cell
def _dbr_cell(
    w1: float = 0.5,
    w2: float = 0.65,
    l1: float = 0.288,
    l2: float = 0.288,
    straight: ComponentSpec = gc.straight,
) -> Component:
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
    _________
    """
    l1 = snap_to_grid(l1)
    l2 = snap_to_grid(l2)
    w1 = snap_to_grid(w1, 2)
    w2 = snap_to_grid(w2, 2)
    c = Component()
    c1 = c << gf.get_component(straight, length=l1, width=w1, cross_section="nitride")
    c2 = c << gf.get_component(straight, length=l2, width=w2, cross_section="strip")
    c2.connect(port="o1", destination=c1.ports["o2"])
    c.add_port("o1", port=c1.ports["o1"])
    c.add_port("o2", port=c2.ports["o2"])
    return c


@cell
def dbr() -> Component:
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
    c = Component()
    l1 = snap_to_grid(0.288)
    l2 = snap_to_grid(0.288)
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


@cell
def coupler(gap: float = 0.2, power_ratio: float = 0.5) -> Component:
    r"""Return a symmetric coupler.

    .. code::

         o2 ________                           ______o3
                    \                         /
                     \                       /
                      ======================= gap
                     /                       \
            ________/                         \_______
         o1                                          o4


    Args:
        gap: coupling gap (um) (0.15, 0.2, 0.25, 0.3)
        power_ratio: float (0.1, 0.2, 0.3, ... 1)
    """
    return gc.coupler(gap, coupler_lengths[round(power_ratio, 2)][round(gap, 2)])


@cell
def adiabatic_bend_90(radius: float = 1):
    """Returns adiabatic bend 90 degrees.add().

    Args:
        radius: bend radius. (From [1, 2, 3, 4, 5])
    """
    return gc.bend_euler(radius=radius, p=adiabatic_bend_90_p_values[radius])


if __name__ == "__main__":
    c = adiabatic_bend_90()
    c.show()
