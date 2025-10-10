import os
list_of_folders_to_run_STAR_in = [
  #                                '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite/ERR10962770',
  #                                '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite/SRR30593421',
   #                               '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite/SRR31112633',
   #                               '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_lite/SRR34697341',
                                  '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_reg/ERR10962770',
                                  '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_reg/SRR30593421',
                                  '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_reg/SRR31112633',
                                  '/scratch/mp7563/Luke_terrace_10_job_sample/SRA_lite_vs_reg/sra_reg/SRR34697341']
genome_dir = "~/Genomes/arabidopsis_thaliana"


os.system(f"STAR --genomeLoad LoadAndExit --genomeDir {genome_dir}")

for file in list_of_folders_to_run_STAR_in:
    print(file)
    accession = file.split('/')[-1]
    current_files = os.listdir(file)
    num_files = len(current_files)
    if num_files ==2:
            matched_file = [s for s in current_files if '.fastq' in s]
            print(f'Running {file}')
            os.system(f'STAR --runThreadN 24 --genomeDir {genome_dir} --readFilesIn {file}/{matched_file[0]}  --outFileNamePrefix {file}/{accession} --outSAMtype None --quantMode GeneCounts')
    elif num_files == 3:
                matched_read_1 = [s for s in current_files if '_1.fastq' in s]
                matched_read_2 = [s for s in current_files if '_2.fastq' in s]  
                os.system(f'STAR --runThreadN 24 --genomeDir {genome_dir} --readFilesIn {file}/{matched_read_1[0]} {file}/{matched_read_2[0]}  --outFileNamePrefix {file}/{accession} --outSAMtype None --quantMode GeneCounts')
os.system(f"STAR --genomeLoad Remove --genomeDir {genome_dir}")
