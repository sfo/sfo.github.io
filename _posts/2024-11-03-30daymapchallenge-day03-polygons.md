---
title: "30 Day Map Challenge 2024 - Day 3: Polygons"
categories:
  - Project
tags:
  - 30daymapchallenge
  - python
  - programming
classes: wide
header:
  teaser: /assets/images/30daymapchallenge2024-day3.png
---

The theme of the third day is _Polygons_:
> A map with polygons. Regions, countries, lakes—this day is for defined shapes that fill space.

### Data

For today, I downloaded two datasets provided at the [Dresden OpenDataPortal](https://opendata.dresden.de) to visualize the number of citizens living in each of Dresden's 64 districts:

- [Citizens by District](https://opendata.dresden.de/informationsportal/?open=1&result=F2A9F96B5D2B4149A77D1F51FCCD37CA#app/mainpage)
- [Districts](https://opendata.dresden.de/informationsportal/?open=1&result=493101D03C794E9C99CD8B2BAC194FEC#app/mainpage)

## Implementation

Today, we create an interactive map again.
Therefore, the imports look similar to the ones from [day one]({% post_url 2024-11-01-30daymapchallenge-day01-points %}).
However, this day, we also need some functionality to create a colormap.

The `read_dresden_csv` function has been introduced [yesterday]({% post_url 2024-11-02-30daymapchallenge-day02-lines %}).


```python
from pathlib import Path

import branca.colormap as cm
import folium
import geopandas as gpd
import pandas as pd

from utils import read_dresden_csv
```

Now, we can load today's data sets:


```python
gdf_districts = read_dresden_csv("data/dresden/stadtteile.csv", geometry_column="shape")
df_citizens = pd.read_csv("data/dresden/bevoelkerung.csv", delimiter=",", header=0)
```

The citizens data set contains information about the number of habitants per district, differentiated along two dimensions: gender (male / female) and marital status (single, married, divorced, widowed).
Since we are interested in overall numbers only, we group records by district (_"blocknr_") and sum the column that holds the number of citizens (_"Anzahl Einwohner"_).
Furthermore, the district's ID (_"blocknr"_) is extracted from a column that contains a string that is comprised of the ID and name.

This ID is then used to assign the number of citizens to the right district.


```python
citizens = (
    df_citizens.assign(
        blocknr=df_citizens["Stadtteil zus."].str.split(" ").str[0].astype(int)
    )
    .groupby("blocknr")
    .sum()["Anzahl Einwohner"]
)

gdf_districts = gdf_districts.set_index("blocknr").assign(
    citizens=citizens,
).fillna(0)
```

Now that the data is consolidated, we can create a map that visualizes all the districts of Dresden using color-coded polygons.
The geometry information is retrieved from the WKT strings for each district (cf. [day one]({% post_url 2024-11-01-30daymapchallenge-day01-points %})).
For encoding the number of citizens, we set up a colormap that goes from white (0 inhabitants) up to red (maximum number of inhabitants per district).


```python
map = folium.Map(tiles="CartoDB positron")
cmap = cm.LinearColormap(["white", "orange", "red"], vmin=0, vmax=citizens.max())

folium.GeoJson(
    gdf_districts,
    popup=folium.GeoJsonPopup(["bez", "citizens"]),
    tooltip=folium.GeoJsonTooltip(["bez", "citizens"]),
    style_function=lambda feature: {
        "fillColor": cmap(feature["properties"]["citizens"]),
        "fillOpacity": .9,
        "color": "black",
        "weight": 1,
        # "dashArray": "5, 5",
    },

).add_to(map)

map.fit_bounds(map.get_bounds())
map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_73c37f467021ce0bdbc9e1f92f04f131 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;


                    &lt;style&gt;
                        .foliumtooltip {

                        }
                       .foliumtooltip table{
                            margin: auto;
                        }
                        .foliumtooltip tr{
                            text-align: left;
                        }
                        .foliumtooltip th{
                            padding: 2px; padding-right: 8px;
                        }
                    &lt;/style&gt;


                    &lt;style&gt;
                        .foliumpopup {
                            margin: auto;
                        }
                       .foliumpopup table{
                            margin: auto;
                        }
                        .foliumpopup tr{
                            text-align: left;
                        }
                        .foliumpopup th{
                            padding: 2px; padding-right: 8px;
                        }
                    &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_73c37f467021ce0bdbc9e1f92f04f131&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_73c37f467021ce0bdbc9e1f92f04f131 = L.map(
                &quot;map_73c37f467021ce0bdbc9e1f92f04f131&quot;,
                {
                    center: [0.0, 0.0],
                    crs: L.CRS.EPSG3857,
                    zoom: 1,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_97934ceebf691ef61dc4b8fcd407c2b1 = L.tileLayer(
                &quot;https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png&quot;,
                {&quot;attribution&quot;: &quot;\u0026copy; \u003ca href=\&quot;https://www.openstreetmap.org/copyright\&quot;\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\&quot;https://carto.com/attributions\&quot;\u003eCARTO\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 20, &quot;maxZoom&quot;: 20, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abcd&quot;, &quot;tms&quot;: false}
            );


            tile_layer_97934ceebf691ef61dc4b8fcd407c2b1.addTo(map_73c37f467021ce0bdbc9e1f92f04f131);


        function geo_json_5ae781ee2404d0a9716184d147ce2bd8_styler(feature) {
            switch(feature.id) {
                case &quot;44&quot;: case &quot;34&quot;: case &quot;33&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffffffff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;42&quot;: case &quot;55&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7a00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;13&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffb01eff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;15&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffcf77ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;24&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff9500ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;32&quot;: case &quot;2&quot;: case &quot;96&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffbf4aff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;90&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffb122ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;5&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7700ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;62&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff6d00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;72&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffa200ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;82&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffa603ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;43&quot;: case &quot;47&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffdea1ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;71&quot;: case &quot;64&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc14eff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;61&quot;: case &quot;7&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff6500ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;14&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff5200ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;11&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff0000ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;1&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffe4b3ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;12&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffa500ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;23&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc861ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;41&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc65cff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;56&quot;: case &quot;54&quot;: case &quot;6&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff5800ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;91&quot;: case &quot;76&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7900ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;74&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffb62fff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;86&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7800ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;53&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff6700ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;97&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffbc42ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;22&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff4b00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;95&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffa706ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;3&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffa90bff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;21&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff6c00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;93&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7200ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;51&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff9100ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;83&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff9c00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;46&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffd78eff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;35&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc456ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;75&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff4a00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;85&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc863ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;45&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc862ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;84&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffb52dff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;57&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff5f00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;25&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff6300ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;4&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff8900ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;94&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff9a00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;63&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffac14ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;77&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc75eff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;31&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff3600ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;81&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff4200ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;98&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff7d00ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;36&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffd484ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;92&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff9600ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;73&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffc354ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                case &quot;52&quot;:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ff3200ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
                default:
                    return {&quot;color&quot;: &quot;black&quot;, &quot;fillColor&quot;: &quot;#ffd485ff&quot;, &quot;fillOpacity&quot;: 0.9, &quot;weight&quot;: 1};
            }
        }

        function geo_json_5ae781ee2404d0a9716184d147ce2bd8_onEachFeature(feature, layer) {
            layer.on({
            });
        };
        var geo_json_5ae781ee2404d0a9716184d147ce2bd8 = L.geoJson(null, {
                onEachFeature: geo_json_5ae781ee2404d0a9716184d147ce2bd8_onEachFeature,

                style: geo_json_5ae781ee2404d0a9716184d147ce2bd8_styler,
        });

        function geo_json_5ae781ee2404d0a9716184d147ce2bd8_add (data) {
            geo_json_5ae781ee2404d0a9716184d147ce2bd8
                .addData(data);
        }



    geo_json_5ae781ee2404d0a9716184d147ce2bd8.bindTooltip(
    function(layer){
    let div = L.DomUtil.create(&#x27;div&#x27;);

    let handleObject = feature=&gt;typeof(feature)==&#x27;object&#x27; ? JSON.stringify(feature) : feature;
    let fields = [&quot;bez&quot;, &quot;citizens&quot;];
    let aliases = [&quot;bez&quot;, &quot;citizens&quot;];
    let table = &#x27;&lt;table&gt;&#x27; +
        String(
        fields.map(
        (v,i)=&gt;
        `&lt;tr&gt;
            &lt;th&gt;${aliases[i]}&lt;/th&gt;

            &lt;td&gt;${handleObject(layer.feature.properties[v])}&lt;/td&gt;
        &lt;/tr&gt;`).join(&#x27;&#x27;))
    +&#x27;&lt;/table&gt;&#x27;;
    div.innerHTML=table;

    return div
    }
    ,{&quot;className&quot;: &quot;foliumtooltip&quot;, &quot;sticky&quot;: true});


    geo_json_5ae781ee2404d0a9716184d147ce2bd8.bindPopup(
    function(layer){
    let div = L.DomUtil.create(&#x27;div&#x27;);

    let handleObject = feature=&gt;typeof(feature)==&#x27;object&#x27; ? JSON.stringify(feature) : feature;
    let fields = [&quot;bez&quot;, &quot;citizens&quot;];
    let aliases = [&quot;bez&quot;, &quot;citizens&quot;];
    let table = &#x27;&lt;table&gt;&#x27; +
        String(
        fields.map(
        (v,i)=&gt;
        `&lt;tr&gt;
            &lt;th&gt;${aliases[i].toLocaleString()}&lt;/th&gt;

            &lt;td&gt;${handleObject(layer.feature.properties[v]).toLocaleString()}&lt;/td&gt;
        &lt;/tr&gt;`).join(&#x27;&#x27;))
    +&#x27;&lt;/table&gt;&#x27;;
    div.innerHTML=table;

    return div
    }
    ,{&quot;className&quot;: &quot;foliumpopup&quot;});


            geo_json_5ae781ee2404d0a9716184d147ce2bd8.addTo(map_73c37f467021ce0bdbc9e1f92f04f131);


            map_73c37f467021ce0bdbc9e1f92f04f131.fitBounds(
                [[50.97493161584745, 13.579341275490068], [51.177686351029934, 13.966058781450718]],
                {}
            );

&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>