"""Startup Pixel Realm."""

# Imports.
import os, platform, subprocess

# Define the file path.
filepath = os.path.join(os.path.dirname(__file__), 'operating_system')
filepath = f'{filepath}/home.pyw'

# Run the file.
if platform.system() == 'Darwin':       # macOS
    subprocess.run(('python3', filepath))
elif platform.system() == 'Windows':    # Windows
    cwd = os.getcwd()
    file_path = os.path.join(cwd, filepath)
    os.startfile(file_path)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))