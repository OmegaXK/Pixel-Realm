"""Open up Minecrack in the browser."""

# Imports.
import webbrowser, os

# Get the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
filepath = f'{resource_path}/Eaglercraft_1.12_Offline_en_US.html'

# Open the website.
webbrowser.open('file://' + filepath)
