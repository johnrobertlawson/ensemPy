import os
import pdb

import numpy as np
import pandas as pd

def determine_filetype(f):
    all_grib1 = ["grb","grib",]
    all_grib2 = ["grb2","grib2"]
    if f.endswith("nc"):
        return "netcdf"
    else:
        for ext in all_grib1:
            if f.endswith(ext):
                return "grib1"
        for ext in all_grib2:
            if f.endswith(ext):
                return "grib2"
    # Can't identify from file type.
    raise Exception
