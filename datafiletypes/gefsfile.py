"""Importing GEFS member files for Ensemble creation.
"""
import os
import pdb

import pandas as pd
import numpy as np
import xarray as xr
import metpy

import ensempy.utils.utils as utils

class GEFSFile:
    def __init__(self,fpath):
        self.fpath = fpath
        self.ds = xr.open_dataset(fpath,engine="cfgrib")

    def get(self,utc=None,level=None,lats=None,lons=None,units=None):
        # data = self.ds.metpy.parse_cf()
        return

if __name__ == "__main__":
    level_types = ["surface","meanSea","depthBelowLandLayer",
                    "heightAboveGround","atmosphereSingleLayer",
                    "heightAboveGroundLayer","pressureFromGroundLayer"]
    # data = dict()
    data = dict()
    all_vars = []
    for lt in level_types:
        print(f"Checking level type {lt}")
        data[lt] = dict()
        key_dict = {"typeOfLevel":lt}
        data[lt]["parsed"] = xr.open_dataset("/storage/jlawson4/GEFS_20220207_12Z/"
                            "gec00.t12z.pgrb2s.0p25.f000",engine="cfgrib",
                            filter_by_keys=key_dict).metpy.parse_cf()
        # data_info = data[lt].info()
        data[lt]["shortname_list"] = list(data[lt]["parsed"].data_vars)
        all_vars.extend(data[lt]["shortname_list"])
    # pdb.set_trace()

    # Some have two entries - cape and cin
    # [721,1440]
    # arr = data["surface"]["parsed"]["gust"].values



