import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

target=Path(Path.home() / ".pyenv/versions/")
dirs = [str(target / e / "bin") for e in os.listdir(target) if not isfile(join(target, e))]
path_str = ':'.join(dirs)
print(f"PATH=$PATH:{path_str}")
