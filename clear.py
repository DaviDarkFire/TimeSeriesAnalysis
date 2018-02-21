#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

def clear():
    filelist = [ f for f in os.listdir(".") if (f.endswith(".pyc") or (f.endswith(".ou")))]
    for f in filelist:
        os.remove(f)
clear()
