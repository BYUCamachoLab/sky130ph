"""Store configuration."""

__all__ = ["PATH"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
cwd_config = cwd / "config.yml"

module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Path:
    module = module_path
    repo = repo_path
    lyp = module_path / "klayout" / "sky130ph" / "layers.lyp"
    sparameters = module_path / "sparameters"


PATH = Path()

if __name__ == "__main__":
    print(PATH)
