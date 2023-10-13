#!/bin/bash
#SBATCH --job-name=job        # create a short name for your job
#SBATCH -p cryoem
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=128G         # memory per cpu-core (4G per cpu-core is default)
#SBATCH --time=1:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=mj7341@princeton.edu

module purge
module load anaconda3/2023.3

conda activate tomodrgn
python project3d.py /scratch/gpfs/ZHONGE/mj7341/MoML/padded_volume/padded_opt1_90rot.mrc -N 10000 -o generated/projected/opt1_90rot_projected_extent5.mrcs --out-pose generated/projected/opt1_90rot_pose_extent5.pkl --out-png generated/projected/projected_opt1_90rot_extent5.png --t-extent 5