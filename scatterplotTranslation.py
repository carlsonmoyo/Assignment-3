import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, file_path, delimiter=','):
        self.file_path = file_path
        self.delimiter = delimiter
        self.x_coordinates = []
        self.y_coordinates = []

    def read_data(self):
        """reading coordinates from my text file."""
        with open(self.file_path, 'r') as my_file:
            my_file.readline()  # Skip the header
            for line in my_file:
                x, y = map(float, line.split(self.delimiter))
                self.x_coordinates.append(x)
                self.y_coordinates.append(y)

    def coordinate_translation(self, x_translation, y_translation):
        """Translating the coordinates by the given amounts."""
        self.translated_x = [x + x_translation for x in self.x_coordinates]
        self.translated_y = [y + y_translation for y in self.y_coordinates]

    def plot_data(self):
        """Plots the original and translated coordinates."""
        # Original scatter plot
        plt.scatter(self.x_coordinates, self.y_coordinates, color='blue', label='Original Points')

        # Translated scatter plot
        plt.scatter(self.translated_x, self.translated_y, color='purple', label='Translated Points')

        # Adding the labels and title to my figure
        plt.ylabel('Y Coordinates')
        plt.xlabel('X Coordinates')
        plt.title('SCATTER PLOT OF POINTS USING THE HORIZONTAL COORDINATES')
        plt.grid(True)
        plt.legend()
        plt.show()

# Driver code
if __name__ == "__main__":
    file_path = 'C:/Users/USER/Documents/x_y_coordinates.txt'
    plotter = ScatterPlot(file_path)
   # reading the above data
    plotter.read_data()

    # translation factor
    x_translation = 1.5
    y_translation = 1.5
    # Translating my coordinates
    plotter.coordinate_translation(x_translation, y_translation)

    # Plot the data
    plotter.plot_data()