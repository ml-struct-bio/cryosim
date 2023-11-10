#!/bin/bash
#SBATCH --job-name=job        # create a short name for your job
#SBATCH -p cryoem
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=256G         # memory per cpu-core (4G per cpu-core is default)
#SBATCH --time=36:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=mj7341@princeton.edu

module purge
module load anaconda3/2023.3

conda activate cryodrgn_2.3
cryodrgn train_vae /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/conformational/add_noise/mrcs/sorted_particles.128.txt --ctf /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/integrated_ctf.pkl --poses /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/integrated_poses.pkl --zdim 8 -n 50 --enc-dim 1024 --enc-layers 3 --dec-dim 1024 --dec-layers 3 -o results/conformational/newctf_addnoise_real_conformation_vae128 > cryodrgn_newctf_addnoise_real_conformation_0_128.log