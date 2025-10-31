"""Open up Minecrack in the browser."""

# Imports.
import webbrowser, os, zipfile
from pathlib import Path

# Get the file paths
resource_path = os.path.join(os.path.dirname(__file__), '')
zip_file_textpath = f'{resource_path}Eaglercraft_1.12_Offline_en_US.html.zip'
zip_file_path = Path(zip_file_textpath)

eaglertextpath = f'{resource_path}Eaglercraft_1.12_Offline_en_US.html'

if Path(eaglertextpath).exists(): # Already extracted
    webbrowser.open('file://' + eaglertextpath)

else: # Need to extract
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(f'{resource_path}')

        print("Eaglercraft succsesfully extracted.")
        webbrowser.open('file://' + eaglertextpath)
