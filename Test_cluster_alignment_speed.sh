#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --time=01:00:00
#SBATCH --mem=40GB
#SBATCH --job-name=Test_cluster_alignment_speed
#SBATCH --mail-type=END
#SBATCH --mail-user=michael.p@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err

module purge 


source ~/Python_envs/Start_Python_singularity.sh
source ~/Python_envs/Initialize_singlularity.sh

module load star/intel/2.7.11a

conda activate Luke_terrace
python Test_cluster_alignment_speed.py