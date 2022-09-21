import gdsfactory as gf
from gdsfactory.types import Layer, LayerStack
from gdsfactory.pdk import LAYER_STACK
from pydantic import BaseModel

from sky130ph.config import PATH

print(LAYER_STACK)
class LayerMap(BaseModel):
    WG: Layer = (1, 0),
    WGCLAD: Layer = (111, 0),
    SLAB150: Layer = (2, 0),
    SLAB90: Layer = (3, 0),
    DEEPTRENCH: Layer = (4, 0),
    GE: Layer = (5, 0),
    WGN: Layer = (34, 0),
    WGN_CLAD: Layer = (36, 0),
    N: Layer = (20, 0),
    NP: Layer = (22, 0),
    NPP: Layer = (24, 0),
    P: Layer = (21, 0),
    PP: Layer = (23, 0),
    PPP: Layer = (25, 0),
    GEN: Layer = (26, 0),
    GEP: Layer = (27, 0),
    HEATER: Layer = (47, 0),
    M1: Layer = (41, 0),
    M2: Layer = (45, 0),
    M3: Layer = (49, 0),
    VIAC: Layer = (40, 0),
    VIA1: Layer = (44, 0),
    VIA2: Layer = (43, 0),
    PADOPEN: Layer = (46, 0),
    DICING: Layer = (100, 0),
    NO_TILE_SI: Layer = (71, 0),
    PADDING: Layer = (67, 0),
    DEVREC: Layer = (68, 0),
    FLOORPLAN: Layer = (64, 0),
    TEXT: Layer = (66, 0),
    PORT: Layer = (1, 10),
    PORTE: Layer = (1, 11),
    PORTH: Layer = (70, 0),
    SHOW_PORTS: Layer = (1, 12),
    LABEL: Layer = (201, 0),
    LABEL_SETTINGS: Layer = (202, 0),
    TE: Layer = (203, 0),
    TM: Layer = (204, 0),
    DRC_MARKER: Layer = (205, 0),
    LABEL_INSTANCE: Layer = (206, 0),
    ERROR_MARKER: Layer = (207, 0),
    ERROR_PATH: Layer = (208, 0),
    SOURCE: Layer = (110, 0),
    MONITOR: Layer = (101, 0)

    class Config:
        frozen = True
        extra = "forbid"


LAYER = LayerMap()


nm = 1e-3
poly_spacer_width = 0.03


def get_layer_stack_generic() -> LayerStack:
    """Returns skyph LayerStack."""
    return LayerStack()


LAYER_STACK = get_layer_stack_generic()
LAYER_COLORS = gf.layers.load_lyp(PATH.lyp)


if __name__ == "__main__":
    # print(PATH.lyp)
    # print(lyp_to_dataclass(PATH.lyp))
    print(LAYER_STACK.get_klayout_3d_script())
