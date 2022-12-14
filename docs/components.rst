This PDK has a library of photonic components that can be customized and readily used.

## Photonic Components

### adiabatic_bend_90

.. autofunction:: sky130ph.components.adiabatic_bend_90

.. plot::
    :include-source:
    import sky130ph.components as skyc
    c = skyc.adiabatic_bend_90(radius=5)
    c.plot()

### coupler

.. autofunction:: sky130ph.components.coupler
.. plot::
    :include-source:
    import sky130ph.components as skyc
    c = skyc.coupler(gap=0.2, power_ratio=0.5)
    c.plot()

### dbr

.. autofunction:: sky130ph.components.dbr
.. plot::
    :include-source:
    import sky130ph.components as skyc
    c = skyc.dbr()
    c.plot()
