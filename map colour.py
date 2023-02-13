import matplotlib.pyplot as plt
import geopandas as gpd

# Load a shapefile containing the geographical information
map_df = gpd.read_file("path/to/shapefile.shp")

# Plot the map
map_df.plot(color='red')

# Show the plot
plt.show()
