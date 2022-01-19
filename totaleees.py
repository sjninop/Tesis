# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:17:58 2022

@author: Usuario_01
"""

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
dates = []
for year in range(2018, 2022):
    for month in range(1, 13):
        dates.append(dt.datetime(year=year, month=month, day=1))