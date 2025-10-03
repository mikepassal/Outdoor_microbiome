import time
import os

# 
start_time = time.time()

data_directory = "/scratch/cgsb/bergelson/bergelson-lab/LH_LIC2024/rnaseq/licrna3"
genome_directory = "~/Genomes/arabidopsis_thaliana"
output_directory = "/scratch/mp7563/Luke_terrace_10_job_sample/aligned_data/plate_3"
list_of_samples_to_process = os.listdir(data_directory)
number_of_cores_to_use = 48
os.system(f"STAR --genomeLoad LoadAndExit --genomeDir {genome_directory}")

for sample in list_of_samples_to_process:
    os.system(f"STAR --runThreadN {number_of_cores_to_use} --genomeDir {genome_directory} --readFilesIn {data_directory}/{sample} --outFileNamePrefix {output_directory}/{sample}_  --quantMode GeneCounts --outSAMtype None --readFilesCommand gunzip -c")
os.system(f"STAR --genomeLoad Remove --genomeDir {genome_directory}")
end_time = time.time()
change_in_time = end_time - start_time
change_in_time_minutes = change_in_time / 60
timer_file_name = "/home/mp7563/Jobs_logs/Luke_terrace_jobs/Testing_aligning_10_samples/Testing_aligning_full_plate_number_3_samples_using_48_cores.txt"
with open(timer_file_name, "w") as text_file:
    
    text_file.write(f"Time taken to align full plate of samples using 48 cores: {change_in_time_minutes} minutes")