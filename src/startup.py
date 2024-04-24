"""Start Pixel Realm."""

# Imports.
import os, platform, subprocess
from pathlib import Path

# Load in the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
path = Path(f'{resource_path}/operating_system/home.pyw')

# Open the home page.
if platform.system() == 'Darwin':       # macOS
    subprocess.run(('python3', path))
elif platform.system() == 'Windows':    # Windows
    cwd = os.getcwd()
    file_path = os.path.join(cwd, path)
    os.startfile(file_path)
else:                                   # linux variants
    subprocess.call(('xdg-open', path))