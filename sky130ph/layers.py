import gdsfactory as gf
from gdsfactory.types import Layer, LayerLevel, LayerStack
from pydantic import BaseModel

from sky130ph.config import PATH


class LayerMap(BaseModel):
    """Draft LayerMap for the Skywater photonics PDK.

    TODO Decide on layer "numbers". Do we need to keep electronics layers?
    """

    # photonic components layers
    WG: Layer = (1, 0)
    WGCLAD: Layer = (111, 0)
    SLAB150: Layer = (2, 0)
    SLAB90: Layer = (3, 0)
    DEEPTRENCH: Layer = (4, 0)
    GE: Layer = (5, 0)
    WGN: Layer = (34, 0)
    WGN_CLAD: Layer = (36, 0)

    # do we need these layers?
    N: Layer = (20, 0)
    NP: Layer = (22, 0)
    NPP: Layer = (24, 0)
    P: Layer = (21, 0)
    PP: Layer = (23, 0)
    PPP: Layer = (25, 0)
    GEN: Layer = (26, 0)
    GEP: Layer = (27, 0)
    HEATER: Layer = (47, 0)
    M1: Layer = (41, 0)
    M2: Layer = (45, 0)
    M3: Layer = (49, 0)
    VIAC: Layer = (40, 0)
    VIA1: Layer = (44, 0)
    VIA2: Layer = (43, 0)
    PADOPEN: Layer = (46, 0)

    DICING: Layer = (100, 0)
    NO_TILE_SI: Layer = (71, 0)
    PADDING: Layer = (67, 0)
    DEVREC: Layer = (68, 0)
    FLOORPLAN: Layer = (64, 0)
    TEXT: Layer = (66, 0)
    PORT: Layer = (1, 10)
    PORTE: Layer = (1, 11)
    PORTH: Layer = (70, 0)
    SHOW_PORTS: Layer = (1, 12)
    LABEL: Layer = (201, 0)
    LABEL_SETTINGS: Layer = (202, 0)
    TE: Layer = (203, 0)
    TM: Layer = (204, 0)
    DRC_MARKER: Layer = (205, 0)
    LABEL_INSTANCE: Layer = (206, 0)
    ERROR_MARKER: Layer = (207, 0)
    ERROR_PATH: Layer = (208, 0)

    SOURCE: Layer = (110, 0)
    MONITOR: Layer = (101, 0)

    class Config:
        """Config for LayerMap."""
        frozen = True
        extra = "forbid"


LAYER = LayerMap()

nm = 1e-3


def get_layer_stack_generic() -> LayerStack:
    """Returns skyph LayerStack."""

    # return LayerStack(
    #     layers=dict(
    #         poly=LayerLevel(
    #             layer=poly,
    #             thickness=poly_thickness,
    #             zmin=0.0,
    #             material="psi",
    #         ),
    #         dnwell=LayerLevel(
    #             layer=dnwell,
    #             zmin=-dnwell_depth,
    #             material="n",
    #             thickness=dnwell_depth,
    #         ),
    #         nwell=LayerLevel(
    #             layer=nwell,
    #             zmin=-thickness_nwell,
    #             material="n",
    #             thickness=thickness_nwell,
    #         ),
    #         pwell=LayerLevel(
    #             layer=pwbm,
    #             zmin=-pwell_depth,
    #             material="p",
    #             thickness=pwell_depth,
    #         ),
    #         nsdm=LayerLevel(
    #             layer=nsdm,
    #             zmin=-sd_impl_depth,
    #             material="n",
    #             thickness=sd_impl_depth,
    #         ),
    #         hvtp=LayerLevel(
    #             layer=hvtp,
    #             zmin=-sd_impl_depth,
    #             material="p",
    #             thickness=sd_impl_depth,
    #         ),
    #         licon1=LayerLevel(
    #             layer=licon1,
    #             zmin=0,
    #             material="metal",
    #             thickness=licon1_thickness,
    #         ),
    #         li1=LayerLevel(
    #             layer=li1,
    #             zmin=licon1_thickness,
    #             material="metal",
    #             thickness=li_thickness,
    #         ),
    #         mcon=LayerLevel(
    #             layer=mcon,
    #             zmin=licon1_thickness + li_thickness,
    #             material="metal",
    #             thickness=mcon_thickness,
    #         ),
    #         met1=LayerLevel(
    #             layer=met1,
    #             zmin=zmin_m1,
    #             material="metal",
    #             thickness=m1_thickness,
    #         ),
    #         via1=LayerLevel(
    #             layer=via,
    #             zmin=zmin_m1 + m1_thickness,
    #             material="metal",
    #             thickness=via1_thickness,
    #         ),
    #         met2=LayerLevel(
    #             layer=met2,
    #             zmin=zmin_m2,
    #             material="metal",
    #             thickness=m2_thickness,
    #         ),
    #         via2=LayerLevel(
    #             layer=via2,
    #             zmin=zmin_m2 + m2_thickness,
    #             material="metal",
    #             thickness=via2_thickness,
    #         ),
    #         met3=LayerLevel(
    #             layer=met3,
    #             zmin=zmin_m3,
    #             material="metal",
    #             thickness=m3_thickness,
    #         ),
    #         via3=LayerLevel(
    #             layer=via3,
    #             zmin=zmin_m3 + m3_thickness,
    #             material="metal",
    #             thickness=via3_thickness,
    #         ),
    #         met4=LayerLevel(
    #             layer=met4,
    #             zmin=zmin_m4,
    #             material="metal",
    #             thickness=m4_thickness,
    #         ),
    #         via4=LayerLevel(
    #             layer=via4,
    #             zmin=zmin_m4 + m4_thickness,
    #             material="metal",
    #             thickness=via4_thickness,
    #         ),
    #         met5=LayerLevel(
    #             layer=met5,
    #             zmin=zmin_m5,
    #             material="metal",
    #             thickness=m5_thickness,
    #         ),
    #     )
    # )


LAYER_STACK = get_layer_stack_generic()
LAYER_COLORS = gf.layers.load_lyp(PATH.lyp)


if __name__ == "__main__":
    # print(PATH.lyp)
    # print(lyp_to_dataclass(PATH.lyp))
    print(LAYER_STACK.get_klayout_3d_script())
