import time
import os

# 
start_time = time.time()

data_directory = "/scratch/mp7563/Luke_terrace_10_job_sample/unaligned_data"
genome_directory = "~/Genomes/arabidopsis_thaliana"
output_directory = f"scratch/mp7563/Luke_terrace_10_job_sample/aligned_data"
list_of_samples_to_process = ['A2450525897_n01_LICRNA01_A01.fastq',
                              'A2450525897_n01_LICRNA01_B01.fastq',
                              'A2450525897_n01_LICRNA01_C01.fastq',
                              'A2450525897_n01_LICRNA01_D01.fastq',
                              'A2450525897_n01_LICRNA01_E01.fastq',
                              'A2450525897_n01_LICRNA01_F01.fastq',
                              'A2450525897_n01_LICRNA01_G01.fastq',
                              'A2450525897_n01_LICRNA01_H01.fastq',
                              'A2450525897_n01_LICRNA01_A02.fastq',
                              'A2450525897_n01_LICRNA01_B02.fastq']
number_of_cores_to_use = 48
os.system(f"STAR --genomeLoad LoadAndExit --genomeDir {genome_directory}")

for sample in list_of_samples_to_process:
    os.system(f"STAR --runThreadN {number_of_cores_to_use} --genomeDir {genome_directory} --readFilesIn {data_directory}/{sample} --outFileNamePrefix {data_directory}/aligned/{sample}_")
os.system(f"STAR --genomeLoad Remove --genomeDir {genome_directory}")
end_time = time.time()
change_in_time = end_time - start_time
change_in_time_minutes = change_in_time / 60
timer_file_name = "/home/mp7563/Luke_terrace_jobs/Testing_aligning_10_samples_using_48_cores.txt"
with open(timer_file_name, "w") as text_file:
    
    text_file.write(f"Time taken to align 10 samples using 48 cores: {change_in_time_minutes} minutes")