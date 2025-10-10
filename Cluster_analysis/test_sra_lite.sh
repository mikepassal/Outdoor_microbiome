#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=24
#SBATCH --time=1:00:00
#SBATCH --mem=40GB
#SBATCH --job-name=Align_plate_4
#SBATCH --mail-type=END
#SBATCH --mail-user=michael.p@nyu.edu
#SBATCH --output=/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite.out
#SBATCH --error=/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite.err

module purge 
module load star/intel/2.7.11a


singularity exec --overlay /home/mp7563/Python_envs/Python_envs.ext3:ro /home/mp7563/Python_envs/ubuntu_cuda_image.sif /bin/bash -c "source /ext3/env.sh; conda activate Luke_terrace; module load star/intel/2.7.11a; python /home/mp7563/Git/Outdoor_microbiome/Align_full_plate_4.py"

