#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --time=04:00:00
#SBATCH --mem=40GB
#SBATCH --job-name=Align_plate_5
#SBATCH --mail-type=END,FAIL,BEGIN
#SBATCH --account=torch_pr_121_general
#SBATCH --mail-user=michael.p@nyu.edu
#SBATCH --output=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_full_plate_samples/full_plate_5_samples_proper_format.out
#SBATCH --error=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_full_plate_samples/full_plate_5_samples_proper_format.err


stdbuf -o0 echo "Script Started"

singularity exec --nv --overlay \
    /home/mp7563/Python_envs/Torch_miniforge_env.ext3:ro /home/mp7563/Python_envs/ubuntu_cuda_image.sif \
    /bin/bash -c "source /ext3/env.sh; conda activate Luke_terrace; \
    python /home/mp7563/Git/Outdoor_microbiome/Cluster_analysis/Align_full_plate_5.py"