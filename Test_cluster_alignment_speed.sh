#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --time=00:45:00
#SBATCH --mem=40GB
#SBATCH --job-name=Test_cluster_alignment_speed
#SBATCH --mail-type=END
#SBATCH --mail-user=michael.p@nyu.edu
#SBATCH --output=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_10_samples/slurm_testing_10_samples_proper_format.out
#SBATCH --error=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_10_samples/slurm_testing_10_samples_proper_format.err
.err

module purge 


bash /home/mp7563/Python_envs/Start_Python_singularity.sh
source /home/mp7563/Python_envs/Initialize_singularity.sh

module load star/intel/2.7.11a

conda activate Luke_terrace
/ext3/miniconda/envs/Luke_terrace/bin/python Test_cluster_alignment_speed.py