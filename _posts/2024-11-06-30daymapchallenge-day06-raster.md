---
title: "30 Day Map Challenge 2024 - Day 6: Raster"
categories:
  - Project
tags:
  - 30daymapchallenge
  - python
  - programming
classes: wide
header:
  teaser: /assets/images/30daymapchallenge2024-day6.png
---

The theme for day six is _Raster_:
> A map using raster data. Rasters are everywhere, but today’s focus is purely on grids and pixels - satellite imagery, heatmaps, or any continuous surface data. 

### Data

Today, I will again use data from [Dresden OpenDataPortal](https://opendata.dresden.de/informationsportal/), specifically the data of the [digital terrain model](https://opendata.dresden.de/informationsportal/?open=1&result=9F7A6477F63840F791F7CCD50C6CD9CF#app/mainpage) with a resolution of 1 meter.
The data is provided in GeoTIFF format, a special kind of the TIF image format with additional georeferencing information embedded, like projection, coordinate system, ellipsoids, etc.

## Implementation

Besides the well-known data handling and plotting libraries, we will use `rasterio` for loading the GeoTIFF file:


```python
import rasterio
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from utils import read_dresden_csv
```

The whole area of Dresden city lays more than 100 meters above mean sea level.
Any point of the rectangular raster in the GeoTIFF image that is beyond the city's boundary has a height value of 0.
Therefore we can use this value to mask the data array and thus exclude these points from further calculations, especially for the colorbar scaling.

Again we also load the city's boundary, as well as street data to add some background information to the map and improve orientation.
This time, we have to adapt the coordinate reference system (CRS), ensuring all data uses the same map projection.


```python
dataset = rasterio.open("data/dresden/DGM1_geotiff/DGM1_Dresden.tif")
data = dataset.read()
data_masked = np.ma.masked_values(data[0], 0.0)

gdf_city_boundary = read_dresden_csv("data/dresden/city_boundary.csv", geometry_column="shape").to_crs(dataset.crs)
gdf_streets = read_dresden_csv("data/dresden/verkehrswege.csv", geometry_column="shape").to_crs(dataset.crs)
```

Mapping of the data is straight forward and the code should be rather self-explanatory.
Since pyplot's image plot function `imshow` uses array indices for x and y coordinates, the `extent` parameter has to be set to reflect the actual bounds of the image in terms of real coordinates.
After plotting the image, we clip it to the city's boundary and add additional information by plotting the road network.


```python
cmap = plt.get_cmap("gist_ncar")
cmap.set_under(alpha=0)

fig, ax = plt.subplots(1, 1, figsize=(20, 20))

image = plt.imshow(
    data_masked,
    cmap=cmap,
    extent=(
        dataset.bounds.left,
        dataset.bounds.right,
        dataset.bounds.bottom,
        dataset.bounds.top,
    ),
)
image.set_clip_path(
    patches.Polygon(
        np.array(gdf_city_boundary["shape"][0].exterior.xy).T,
        closed=False,
        transform=ax.transData,
    )
)

gdf_city_boundary["shape"].plot(
    edgecolor="black",
    facecolor="none",
    ax=ax,
)

gdf_streets["shape"].plot(edgecolor="white", lw=0.5, ax=ax)

plt.colorbar(
    shrink=0.5, label=r"height above mean sea level ($\it{Normalhöhennull}$) [m]"
)
ax.axis("off")

plt.show()
```


    
![png](/assets/2024-11-06-30daymapchallenge-day06-raster_files/2024-11-06-30daymapchallenge-day06-raster_9_0.png)
    

