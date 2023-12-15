# num_class="0"
directory_path="/scratch/gpfs/ZHONGE/mj7341/MoML/cryosim/fscs/backproject_w_mask/fscs"
input_files=("$directory_path"/*)

python /scratch/gpfs/ZHONGE/mj7341/cryodrgn_internal/analysis_scripts/plotfsc.py -a 3.0 -o fscs/backproject_w_mask/figs/fsc_class0_w_mask2.png -i "${input_files[@]}"