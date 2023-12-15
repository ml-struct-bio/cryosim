for i in {1..87}
do
    python /scratch/gpfs/ZHONGE/mj7341/cryodrgn_internal/analysis_scripts/psnr.py /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/128_chimera_resample/1_vol_128.mrc /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/add_noise/backprojected_for_fsc/backproject_vol_${i}.mrc 
done
