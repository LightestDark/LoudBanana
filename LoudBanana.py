#ALL LIBRARIES ARE NEEDED
import sys
import subprocess

need = ["numpy", "Pillow"]
for x in need:
    try:
        __import__(x if x != "Pillow" else "PIL")
    except:
        subprocess.check_call([sys.executable, "-m", "pip", "install", x])

import os
import wave
import numpy as np
from PIL import Image
from tkinter import Tk, filedialog
import winsound
import time

Tk().withdraw()
file_pick = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
if not file_pick:
    exit()

root = os.path.dirname(file_pick)
banana = os.path.join(root, "LoudBanana")
os.makedirs(banana, exist_ok=True)

img = Image.open(file_pick).convert("RGB")
arr = np.array(img, dtype=np.uint8)
size = arr.shape
raw = arr.flatten()

audio = (raw.astype(np.int16) - 128) * 256
wav_path = os.path.join(banana, "banana.wav")

with wave.open(wav_path, "w") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    w.writeframes(audio.tobytes())

del img, arr, raw, audio

winsound.PlaySound(wav_path, winsound.SND_FILENAME)
time.sleep(0.2)
os.utime(wav_path, None)

with wave.open(wav_path, "r") as w:
    data = w.readframes(w.getnframes())

nums = np.frombuffer(data, dtype=np.int16)
back = (nums // 256 + 128).astype(np.uint8)

rebuilt = back.reshape(size)

Image.fromarray(rebuilt, "RGB").save(os.path.join(banana, "banana_full.png"))

red = rebuilt.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0
Image.fromarray(red, "RGB").save(os.path.join(banana, "banana_red.png"))

green = rebuilt.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0
Image.fromarray(green, "RGB").save(os.path.join(banana, "banana_green.png"))

blue = rebuilt.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0
Image.fromarray(blue, "RGB").save(os.path.join(banana, "banana_blue.png"))
