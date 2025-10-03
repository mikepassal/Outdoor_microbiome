#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --time=06:00:00
#SBATCH --mem=40GB
#SBATCH --job-name=Align_plate_4
#SBATCH --mail-type=END
#SBATCH --mail-user=michael.p@nyu.edu
#SBATCH --output=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_full_plate_samples/full_plate_4_samples_proper_format.out
#SBATCH --error=/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_full_plate_samples/full_plate_4_samples_proper_format.err

module purge 
module load star/intel/2.7.11a


singularity exec --overlay /home/mp7563/Python_envs/Python_envs.ext3:ro /home/mp7563/Python_envs/ubuntu_cuda_image.sif /bin/bash -c "source /ext3/env.sh; conda activate Luke_terrace; module load star/intel/2.7.11a; python /home/mp7563/Git/Outdoor_microbiome/Align_full_plate_4.py"



