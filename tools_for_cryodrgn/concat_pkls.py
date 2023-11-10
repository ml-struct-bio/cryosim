# python concat_pkls.py $(for i in {1..87}; do cat /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/ctfs/1hzh.ctf.${i}.pkl; done) -o /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/combined_ctf.pkl

'''Skeleton script'''

import argparse
import numpy as np
import sys, os
import pickle

log = print

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='+', help='Input')
    parser.add_argument('-o', help='Output')
    return parser

def main(args):
    x = [pickle.load(open(f,'rb')) for f in args.input]
    if type(x[0]) == tuple: # pose tuples
        r = [xx[0] for xx in x]
        t = [xx[1] for xx in x]
        r2 = np.concatenate(r)
        t2 = np.concatenate(t)
        log(r2.shape)
        log(t2.shape)
        x2 = (r2,t2)
    else:
        for i in x:
            log(i.shape)
        x2 = np.concatenate(x)
        log(x2.shape)
    pickle.dump(x2, open(args.o,'wb'))

if __name__ == '__main__':
    main(parse_args().parse_args())