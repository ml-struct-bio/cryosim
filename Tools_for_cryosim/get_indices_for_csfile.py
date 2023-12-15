import os, sys
import os.path
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cryodrgn
from cryodrgn import analysis, utils, config
from cryodrgn.starfile import Starfile
import pandas as pd
from cryodrgn.source import ImageSource

from sklearn import metrics
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
import pickle
import re
import argparse

# python get_indices_for_csfile.py /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/add_noise/128_chimera_resample/snr01/snr01_star.star /scratch/gpfs/ZHONGE/mj7341/cryosparc/CS-chimera-resample-data/J25/ --task 3dcls -o /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/cryosparc --num_classes 5

log = print
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('star_path', help='starfile path')
    parser.add_argument('cs_path', help='cs file path in cryosparc')
    parser.add_argument("--task", type=str, default='3dcls', choices=("3dcls", "3dva"), help="choose cryosparc task")
    parser.add_argument('-o', type=os.path.abspath, required=True, help='Output projection stack (.mrcs)')
    parser.add_argument('--num_classes', type=int, default=5, help='Number of random projections')

    return parser

def natural_sort_key(s):
    # Convert the string to a list of text and numbers
    parts = re.split('([0-9]+)', s)
    
    # Convert numeric parts to integers for proper numeric comparison
    parts[1::2] = map(int, parts[1::2])
    
    return parts

def get_inds_dict_3dclass(cs_path, ori_df, num_classes, out_dir):
    for num_class in range(num_classes):
        path = cs_path+cs_path.split('/')[-2]+'_passthrough_particles_class_'+str(num_class)+'.cs'
        cs_file = np.load(path)
        
        particle_inds_dict = {}
        for i in range(len(cs_file)):
            num_vol = cs_file[i][1].split(b'_')[1].decode('utf-8')
            cs_vol_names = num_vol+ '_' + cs_file[i][1].split(b'_')[2].decode('utf-8') + '_'
            condition = (ori_df['_rlnDefocusU'] == str(cs_file[i][12])) & (ori_df['_rlnImageName'].str.contains(cs_vol_names, case=False, na=False))
            idx = ori_df.loc[condition].index[0]

            if num_vol in particle_inds_dict:
                # Increment the count if the string is already a key
                particle_inds_dict[num_vol].append(idx)
            else:
                # Add the string as a new key with count 1 if it's not already in the dictionary
                particle_inds_dict[num_vol] = [idx]
        
        with open(out_dir+"/3dcls/3dcls_cs"+str(num_class)+".pkl", "wb") as file:
            pickle.dump(particle_inds_dict, file)
            print('saved!')

def get_inds_dict_3dva(cs_path, ori_df, num_classes, out_dir):
    for num_class in range(num_classes):
        path = cs_path+cs_path.split('/')[-2]+'_cluster_00'+str(num_class)+'_particles.cs'
        cs_file = np.load(path)
        
        particle_inds_dict = {}
        for i in range(len(cs_file)):
            num_vol = cs_file[i][1].split(b'_')[1].decode('utf-8')
            cs_vol_names = num_vol+ '_' + cs_file[i][1].split(b'_')[2].decode('utf-8') + '_'
            condition = (ori_df['_rlnImageName'].str.contains(cs_vol_names, case=False, na=False))
            idx = ori_df.loc[condition].iloc[cs_file[i][2]-1].name

            if num_vol in particle_inds_dict:
                # Increment the count if the string is already a key
                particle_inds_dict[num_vol].append(idx)
            else:
                # Add the string as a new key with count 1 if it's not already in the dictionary
                particle_inds_dict[num_vol] = [idx]
        
        with open(f"{out_dir}/3dva/3dva_cs"+str(num_class)+".pkl", "wb") as file:
            pickle.dump(particle_inds_dict, file)
            print('saved!')
        

def main(args):
    ori_s = Starfile.load(args.star_path)
    ori_df = ori_s.df
    
    if args.task == '3dcls':
        # 3D Classification
        print('3D Classification!')
        get_inds_dict_3dclass(args.cs_path, ori_df, num_classes=args.num_classes, out_dir=args.o)

    elif args.task == '3dva':
        # 3DVA
        print('3DVA!')
        get_inds_dict_3dva(args.cs_path, ori_df, num_classes=args.num_classes, out_dir=args.o)    


if __name__ == '__main__':
    args = parse_args().parse_args()
    main(args)
