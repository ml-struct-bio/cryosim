#!/bin/bash
#SBATCH --job-name=job        # create a short name for your job
#SBATCH -p cryoem
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=128G         # memory per cpu-core (4G per cpu-core is default)
#SBATCH --time=1:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=mj7341@princeton.edu

module purge
module load anaconda3/2023.3

conda activate tomodrgn

for i in {1..100}
do 
    python add_ctf.py /home/mj7341/dev/MoML/data/igg_prepost_frame100/3d_projected/projs/$i.256.projs.mrcs --ctf-pkl all.ctf.pkl --Apix 3 --s1 0 --s2 0 -o /home/mj7341/dev/MoML/data/igg_prepost_frame100/ctf_added/mrcs/$i.256_ctf.mrcs --out-png /home/mj7341/dev/MoML/data/igg_prepost_frame100/ctf_added/pngs/$i.256_ctf.png
done