"""Compute FSC between two volumes"""

import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np
from cryodrgn import fft
from cryodrgn.source import ImageSource
import os
import numpy as np

log = print
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vol1", help="Input")
    parser.add_argument("vol2", help="Input")
    parser.add_argument("--Apix", type=float, default=1)
    parser.add_argument('-o', type=os.path.abspath, required=True, help='Output projection stack (.mrcs)')

    return parser

def calculate_psnr(img1, img2, max_value=255):
    """"Calculating peak signal-to-noise ratio (PSNR) between two images."""
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    if mse == 0:
        return 100
    return 20 * np.log10(max_value / (np.sqrt(mse)))

def main(args):
    vol1 = ImageSource.from_file(args.vol1)
    vol2 = ImageSource.from_file(args.vol2)
    calculate_psnr()

if __name__ == "__main__":
    args = parse_args().parse_args()
    main(args)

