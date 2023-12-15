import numpy as np
import os
import pickle

from Bio import PDB
from scipy.spatial.distance import pdist, squareform, cdist
from Bio.SVDSuperimposer import SVDSuperimposer


_verbose = False

def log(msg):
    print(msg)

def vlog(msg):
    if _verbose:
        print(msg)

########### GEOMETRY FUNCTIONS #############

def bond(A,B):
    raise NotImplementedError

def angle(A,B,C):
    raise NotImplementedError

def dihedral(A,B,C,D):
    raise NotImplementedError

def align(ref_coord, mod_coord):
    sup = SVDSuperimposer()
    sup.set(ref_coord, mod_coord)
    sup.run()
    A, b = sup.get_rotran()
    return A, b

def apply(atom_list, A, b):
    for atom in atom_list:
        atom.transform(A,b)

############ PDB I/O FUNCTIONS #################

def load_pdb(infile):
    '''Return a PDB.Model object'''
    p = PDB.PDBParser()
    s = p.get_structure('5jhf',infile)
    assert len(s) == 1, "More than 1 model present"
    return s[0]

def write_bio_pdb(structure, out_pdb):
    io = PDB.PDBIO()
    io.set_structure(structure)
    f = open(out_pdb,'w')
    f.write('HEADER    {}\n'.format(os.path.splitext(os.path.basename(out_pdb))[0]))
    io.save(f)
    f.close()

def combine_pdbs(pdbs, out_pdb):
    outf = open(out_pdb,'w')
    for pdb in pdbs:
        with open(pdb,'r') as f:
            outf.write(f.read())
    outf.close()

def load_pkl(pkl):
    with open(pkl,'rb') as f:
        coord  = pickle.load(f)
    return coord

def write_pkl(out_pkl, coord):
    with open(out_pkl,'wb') as f:
        pickle.dump(coord, f)

########### OTHER HELPER FUNCTIONS ################

def compute_min_dist(coord):
    '''Compute the minimum pairwise distance between atoms in coord, ignoring 8 wneighboring atoms'''
    # 8 neighboring atoms is roughly the 1-2 and 1-3 neighboring amino acids
    d = squareform(pdist(coord))
    d = np.triu(d,9) 
    dists = d[np.where(d)]
    return np.min(dists)

def compute_min_cdist(coordA, coordB):
    '''Compute the minimum pairwise distance between two sets of coordinates'''
    dists = cdist(coordA, coordB)
    return np.min(dists)


