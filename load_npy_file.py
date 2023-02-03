#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     load_npy_file.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #190
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
import numpy as np
import simpleaudio as sa

# load the file from disk…
with open("scale1.npy", "rb") as f:
    audio_data = np.load(f)
# now play it back
play_obj = sa.play_buffer(audio_data, 1, 2, 44100)
play_obj.wait_done()
