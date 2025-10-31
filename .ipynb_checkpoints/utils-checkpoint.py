import numpy as np
import pandas as pd
import xarray as xr
from odc.geo import GeoBox
from odc.stac import load
from pystac_client import Client

catalog = "https://earth-search.aws.element84.com/v1/"
client = Client.open(catalog)

def load_data(collection, year, bbox): 
    
    items = client.search(
        collections=[collection],
        bbox=bbox,
        datetime=year,
    ).item_collection()

    chunks = dict(x=2048, y=2048)
    geom = GeoBox.from_bbox(bbox, crs="EPSG:4326", resolution=0.0001)

    
    if collection == "sentinel-2-l2a":
        measurements = ["red", "blue", "green", "nir08", "swir16", "scl"]
        groupby = "solar_day"
    elif collection == "sentinel-1-grd":
        measurements = ["vh", "vv"]
        groupby = "solar_day"
    elif collection == "cop-dem-glo-30":
        measurements = None
        groupby = None
        chunks = None
    else:
        measurements = None
        groupby = None

    # Load data
    data = load(
        items,
        chunks=chunks,
        like=geom,
        groupby=groupby,
        measurements=measurements,
    )

    data = data.rename({"latitude": "y", "longitude": "x"})

    return data


def mask_cloud(data, collection):
    
    if collection == "sentinel-2-l2a":
        scl_included_classes = [4, 5, 6, 7]
        low_cloud = data.scl.isin(scl_included_classes)
        data = data.where(low_cloud)

    data = data.median(dim="time").compute()
    data = data.expand_dims("time")
    data = data.assign_coords(time=[pd.Timestamp("2024-01-01")])

    return data

def add_indices(data: xr.Dataset) -> xr.Dataset:
    """
    Add common spectral indices to a Sentinel-2 xarray Dataset.
    Works with bands: red, green, blue, nir08, swir16.
    """
    spectral_bands = data[["red", "green", "blue", "nir08", "swir16"]]
    nodata = spectral_bands.red == 0

    # Do index calculation on scaled float values
    scaled = (spectral_bands / 10000).clip(0, 1).astype("float32")
    scaled = scaled.where(~nodata, np.nan)

    # NDVI = (NIR - Red) / (NIR + Red)
    data["ndvi"] = (scaled["nir08"] - scaled["red"]) / (scaled["nir08"] + scaled["red"])

    # NDBI (Normalized Difference Built-up Index) = (SWIR - NIR) / (SWIR + NIR)
    data["ndbi"] = (scaled["swir16"] - scaled["nir08"]) / (scaled["swir16"] + scaled["nir08"])

 
    del scaled

    return data