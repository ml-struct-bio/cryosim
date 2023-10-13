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
python add_noise.py generated/ctf_added/opt4_particles_extent5_w_ctf.mrcs -o generated/noise_added/opt4_extent5_output_noisy_particles.mrcs --snr .1 --out-png generated/noise_added/opt4_extent5_noise_added.png