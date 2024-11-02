from pathlib import Path

import geopandas as gpd
import pandas as pd


def read_dresden_csv(
    file_path: str | Path, geometry_column: str, srid: int = 4326
) -> gpd.GeoDataFrame:
    df = pd.read_csv(file_path, delimiter=";", header=0)
    df[geometry_column] = gpd.GeoSeries.from_wkt(
        df[geometry_column].str.removeprefix(f"SRID={srid};")
    )
    return gpd.GeoDataFrame(
        df,
        geometry=geometry_column,
        crs=f"EPSG:{srid}",
    )
