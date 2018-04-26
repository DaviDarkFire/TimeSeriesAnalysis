#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastdtw import fastdtw
import numpy as np
from scipy.spatial.distance import euclidean


def dtw(array1,array2):
	# x = np.array([1,2,3,4,5,6,7,8,9,10])
	# y = np.array([2,4,1,22,5,8,3,5,7,2])
	distance, path = fastdtw(array1, array2, dist=euclidean)
	return distance