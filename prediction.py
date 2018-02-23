#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def main():
    x = []
    y = []
    for i in range(0,10,1):
        x.append(i)
        y.append(i)
    x = np.array(x)
    y = np.array(y)
    distance, path = fastdtw(x, y, dist=euclidean)
    print(distance)
main()
