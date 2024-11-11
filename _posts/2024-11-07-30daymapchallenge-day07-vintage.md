---
title: "30 Day Map Challenge 2024 - Day 7: Vintage"
categories:
  - Project
tags:
  - 30daymapchallenge
  - python
  - programming
classes: wide
header:
  teaser: /assets/images/30daymapchallenge2024-day7.png
---

For day seven , the theme _Vintage_:
> Map something modern in a vintage aesthetic. Create a map that captures the look and feel of historical cartography but focuses on a contemporary topic. Use muted colors, fonts, and classic elements.

### Data
 
I'm not the most talented person when it comes to creating aesthetically pleasing graphics or designs.
So today I'm going to focus on some technical details again and take the chance to learn something new.
Specifically, I will take a look at how images can be georeferenced in order to place them correctly in a coordinate system.

To do this, I first downloaded a nearly 100 years old map of [Dresden (1926)](https://www.deutschefotothek.de/documents/obj/70302465/) from the _Deutsche Fotothek_.

Since the dataset should reflect "something modern", I chose to visualize locations of charging stations for electric cars.
This dataset is obtained from OpenStreetMap via the [overpass turbo](https://overpass-turbo.eu/) webtool, using the following query:
```
node[amenity=charging_station](51.0, 13.6, 51.1, 13.83);
out geom;
```

I exported the result as a GeoJSON file, which I will import later using `geopandas`.

## Implementation

First, we will of course need some imports.
Today, there is nothing new to it:


```python
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
```

Next, we need to georeference the map image.
Opening the file in a somewhat advanced image editor (I use [GIMP](https://www.gimp.org/)), allows to find the pixel coordinates of some very remarkable features, like crossings, buildings, or special features of the landscape.
The same features have to be located using a mapping service, like Google Maps.
This allows to find the real-world coordinates of those points and setup a list of so-called _ground control points_, form which a transformation can be calculated.
The `rasterio` library already implements this functionality:


```python
gcps = [
    rasterio.control.GroundControlPoint(col= 307, row= 332, y=51.08368419427998, x=13.686551101853567),
    rasterio.control.GroundControlPoint(col= 151, row=1202, y=51.01389086947117, x=13.665240136707837),
    rasterio.control.GroundControlPoint(col=1273, row=1231, y=51.01168185051654, x=13.808524372827599),
    rasterio.control.GroundControlPoint(col=1340, row= 263, y=51.08922315122832, x=13.818753999574017),
]
transformation = rasterio.transform.from_gcps(gcps)

with rasterio.open("data/map_dresden_1926.jpg", "r") as image_file:
    image_raw = image_file.read()
```

Furthermore, we need to load the locations of all charging stations exported from overpass turbo:


```python
gdf_charging_stations = gpd.read_file("data/osm/charging_stations_dresden.geojson")
```

With the image loaded, the transformation set up, as well as the charging station data, we can finally create a nice visualization based on the old map of Dresden:


```python
fig, ax = plt.subplots(1, 1, figsize=(15, 15))

show(
    image_raw,
    ax=ax,
    transform=transformation,
)

gdf_charging_stations["geometry"].plot(
    ax=ax,
    markersize=256,
    color="black",
    marker="$⚡$",
)

ax.set_axis_off()
plt.show()
```


    
![png](/assets/2024-11-07-30daymapchallenge-day07-vintage_files/2024-11-07-30daymapchallenge-day07-vintage_11_0.png)
    

