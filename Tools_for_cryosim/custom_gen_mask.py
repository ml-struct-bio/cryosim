'''Skeleton script'''

import argparse
import numpy as np
import sys, os
import pickle
from scipy.ndimage.morphology import distance_transform_edt
from scipy.ndimage.morphology import binary_dilation

import matplotlib.pyplot as plt

from cryodrgnai.cryodrgn import utils
from cryodrgnai.cryodrgn import mrc
from cryodrgn.cryodrgn.source import ImageSource

log = print
# input: /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/newang_128/
# python custom_gen_mask.py /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/128_chimera_resample/ --dilate 25 --dist 15 -o /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/initial_vol/128/chimera_resample_128_init_conf_mask.mrc
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Input (directory of all volumes)')
    parser.add_argument('--thresh', type=float, help='Density value to threshold for masking (default: half of max density value)')
    parser.add_argument('--dilate', type=int, default=3, help='Dilate initial mask by this amount (default: %(default)s pixels)')
    parser.add_argument('--dist', type=int, default=10, help='Width of cosine edge (default: %(default)s pix)')
    parser.add_argument('-o', help='Output')
    return parser

def view_slices(y,D):
    fig,ax = plt.subplots(1,3, figsize=(10,8))
    ax[0].imshow(y[D//2,:,:])
    ax[1].imshow(y[:,D//2,:])
    ax[2].imshow(y[:,:,D//2])

def main(args):
    lst = os.listdir(args.input)
    N = len(lst)
    empty_array = np.empty((N, 128, 128, 128))
    if args.thresh is None:
        thresh = []
        for i in range(N):
            vol, header = mrc.parse_mrc(args.input+lst[i])
            thresh.append(np.percentile(vol, 99.99) / 2)
            empty_array[i] = vol
        thresh = np.mean(thresh)
    else:
        for i in range(N):
            vol, header = mrc.parse_mrc(args.input+lst[i])
        thresh = args.thresh
        empty_array[i] = vol

    max_vol = np.max(empty_array, axis=0)


    # thresh = np.percentile(vol,99.99)/2 if args.thresh is None else args.thresh
    log(f'Threshold: {thresh}')
    

    x = (max_vol>=thresh).astype(bool)
    if args.dilate:
        log(f'Dilate initial mask by: {args.dilate}')
        x = binary_dilation(x, iterations=args.dilate)
    dist = args.dist
    log(f'Width of cosine edge: {dist}')
    if dist:
        y = distance_transform_edt(~x.astype(bool))
        y[y>dist] = dist
        z = np.cos(np.pi*y/dist/2)
    else:
        z=x
    mrc.write(args.o,z.astype(np.float32), header=header)

    view_slices(z, max_vol.shape[0])
    plt.show()
    

if __name__ == '__main__':
    main(parse_args().parse_args())
