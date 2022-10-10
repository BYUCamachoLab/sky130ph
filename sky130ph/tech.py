""" technology definitions."""
import sys

import gdsfactory as gf
from gdsfactory.cross_section import get_cross_section_factories, strip

from sky130ph.layers import LAYER

cross_sections = get_cross_section_factories(sys.modules[__name__])


if __name__ == "__main__":
    print(cross_sections.keys())
