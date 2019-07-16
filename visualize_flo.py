#!/usr/bin/env python

import cvbase as cvb
import glob
import argparse
import os
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('arg1', type=str, help='Input dir')
args = parser.parse_args()

path = args.arg1
outdir = os.path.split(path)
print(outdir)
outdir = os.path.join(outdir[0],outdir[1] + '_vis')
if not os.path.exists(outdir):
    os.mkdir(outdir)

flos = glob.glob(os.path.join(path,'*flo'))
print(len(flos),'flo files found.')
for flo in flos:
    flow=cvb.read_flow(flo)
    img = cvb.flow2rgb(flow)
    plt.imsave(os.path.join(outdir, os.path.basename(flo)+'.png'), img)
    