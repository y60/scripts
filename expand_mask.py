#!/usr/bin/env python

# 指定したフォルダ内のマスクを指定したピクセルだけ拡大する

import cvbase as cvb
import glob
import argparse
import os
from PIL import Image
import numpy as np
from scipy import signal

parser = argparse.ArgumentParser()
parser.add_argument('arg1', type=str, help='Input dir')
parser.add_argument('arg2', type=int, help='Pixel to expand')
args = parser.parse_args()

path = args.arg1
d = args.arg2
outdir = os.path.split(path)
print(outdir)
outdir = os.path.join(outdir[0],outdir[1] + '_expanded_'+str(d))
if not os.path.exists(outdir):
    os.mkdir(outdir)

files = glob.glob(os.path.join(path,'*.png'))
print(len(files),'pngs found.')
k = np.ones(shape=(1+2*d,1+2*d))
for f in files:
    image = np.asarray(Image.open(f))
    if len(image.shape)==3:
        image = image[:,:,0]
    image = signal.correlate(image,k,'same')
    image = np.minimum(image,255)
    Image.fromarray(np.uint8(image)).save(os.path.join(outdir, os.path.basename(f)))
    