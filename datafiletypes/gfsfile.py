"""Importing GFS files for Ensemble creation.
"""
import os
import pdb

import pandas as pd
import numpy as np
import xarray as xr
import metpy

import ensempy.utils.utils as utils

class GFSFile:
    def __init__(self,fpath):
        self.fpath = fpath
        self.ds = xr.open_dataset(fpath)

        self.get()

    def get(self,utc=None,level=None,lats=None,lons=None,units=None):
        data = self.ds.metpy.parse_cf()
        pdb.set_trace()

