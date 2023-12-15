for i in {1..87}
do
    python /scratch/gpfs/ZHONGE/mj7341/cryodrgn_internal/analysis_scripts/fsc.py /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/128_chimera_resample/1_vol_128.mrc /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/add_noise/backprojected_for_fsc/backproject_vol_${i}.mrc --plot --Apix 3.0 -o /scratch/gpfs/ZHONGE/mj7341/MoML/cryosim/fscs/backproject_w_mask/fscs/masked_backproj_fsc_class1_${i}.txt --mask /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/Fabs/masks/128_chimera_conform_fab_mask.mrc
done
