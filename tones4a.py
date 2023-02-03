#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     tones4a.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #190
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# This program uses numpy and simpleaudio to create a tone
# file that is converted into a .wav file that can be used
# to notify user of your programs.  However, this file is a
# bit long for that purpose.  It does give you the information
# to create your own note files.
# ======================================================
import numpy as np
import simpleaudio as sa
import wave

# calculate the frequencies
A_freq = 440
Ash_freq = A_freq * 2 ** (1 / 12)
B_freq = A_freq * 2 ** (2 / 12)
C_freq = A_freq * 2 ** (3 / 12)
Csh_freq = A_freq * 2 ** (4 / 12)
D_freq = A_freq * 2 ** (5 / 12)
Dsh_freq = A_freq * 2 ** (6 / 12)
E_freq = A_freq * 2 ** (7 / 12)
F_freq = A_freq * 2 ** (8 / 12)
Fsh_freq = A_freq * 2 ** (9 / 12)
G_freq = A_freq * 2 ** (10 / 12)
Gsh_freq = A_freq * 2 ** (11 / 12)
A5_freq = 880
print(
    A_freq,
    Ash_freq,
    B_freq,
    C_freq,
    Csh_freq,
    D_freq,
    Dsh_freq,
    E_freq,
    F_freq,
    Fsh_freq,
    G_freq,
    Gsh_freq,
    A5_freq,
)

sample_rate = 44100
# T is duration in seconds of the sound
T = 0.25
t = np.linspace(0, T, int(T * sample_rate), False)
# Generate sinewave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Ash_note = np.sin(Ash_freq * t * 2 * np.pi)
B_note = np.sin(B_freq * t * 2 * np.pi)
C_note = np.sin(C_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
D_note = np.sin(D_freq * t * 2 * np.pi)
Dsh_note = np.sin(Dsh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
F_note = np.sin(F_freq * t * 2 * np.pi)
Fsh_note = np.sin(Fsh_freq * t * 2 * np.pi)
G_note = np.sin(G_freq * t * 2 * np.pi)
Gsh_note = np.sin(Gsh_freq * t * 2 * np.pi)
A5_note = np.sin(A5_freq * t * 2 * np.pi)
# Concatenate notes
audio = np.hstack(
    (
        A_note,
        Ash_note,
        B_note,
        C_note,
        Csh_note,
        D_note,
        Dsh_note,
        E_note,
        F_note,
        Fsh_note,
        G_note,
        Gsh_note,
        A5_note,
    )
)
# normalize the audio object to 16 bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16 bit
audio = audio.astype(np.int16)
# play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
# play_obj.wait_done()

# save the audio object to local file for future use
with open("scale1.npy", "wb") as f:
    np.save(f, audio)

# Now save the audio object to a .wav file to eliminate
# the need for numpy later on.

obj = wave.open("scale1.wav", "w")
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(sample_rate)
obj.writeframesraw(audio)
obj.close()

# Finally, play it back to verify.
wave_obj = sa.WaveObject.from_wave_file("scale1.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
