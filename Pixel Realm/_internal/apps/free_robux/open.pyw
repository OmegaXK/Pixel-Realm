"""Open up the Free Robux website in the user's browser."""

# Imports.
import webbrowser, os

# Get the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
filepath = f'{resource_path}/index.html'

# Open the website.
webbrowser.open('file://' + filepath)