# Dictionary of color names and their corresponding codes
color = {
    'absolute zero': '#0048ba', 'acid green': '#b0bf1a', 'aliceblue': '#f0f8ff',
    'alizarin crimson': '#e32636', 'amaranth': '#e52b50', 'amber': '#ffbf00',
    'amethyst': '#9966cc', 'antiquewhite': '#faebd7',
    'antiquewhite1': '#ffefdb',
    'antiquewhite2': '#eedfcc',
    'antiquewhite4': '#8b8378',
    'apricot': '#fbceb1',
    'aqua': '#00ffff'
}

# Get user input for color name
color_name = input("Enter a color name: ").lower()

# Loop until an empty input is provided
while color_name != "":
    color_code = color.get(color_name, "Invalid color name")  # Get color code from dictionary or show "Invalid color name"
    print(color_code)  # Print the color code
    color_name = input("Enter a color name: ").lower()  # Get the next color name

# End of the program





