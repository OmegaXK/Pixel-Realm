"""Open up the Free Robux website in the user's browser."""

# Imports.
import webbrowser, os

# Retrieve the absolute path of the file.
filepath = os.path.abspath('home.html')
filepath = filepath.replace('home.html', 'apps/free_robux/index.html')

# Open the website.
webbrowser.open('file://' + filepath)