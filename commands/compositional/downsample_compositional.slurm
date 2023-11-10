#!/bin/bash
#SBATCH --job-name=job        # create a short name for your job
#SBATCH -p cryoem
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=512         # memory per cpu-core (4G per cpu-core is default)
#SBATCH --time=6:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=mj7341@princeton.edu

module purge
module load anaconda3/2023.3

conda activate tomodrgn
for pdb in 1tjg 4kht 7che 7m6d 8i5i
do
    for i in {1..87}
    do 
        cryodrgn downsample /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/256/$pdb.$i.particle.mrc -D 128 --is-vol -o /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/128/$pdb.$i.particles.128.mrcs
    done
done