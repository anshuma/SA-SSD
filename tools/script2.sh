#!/bin/bash                                                                                                                                
#SBATCH --job-name=anshuma_run_SASSD_SGD	# Job name                                                                                          
#SBATCH --ntasks=4                	# Run on a single CPU                                                                       
#SBATCH --time=50:20:00           	# Time limit hrs:min:sec                                                                           
#SBATCH --output=test_sample_%j.out   # Standard output and error log                                                                    
#SBATCH --cpus-per-task=1                                                                                                                
#SBATCH --partition=cse-gpu-all  

#SBATCH --output=/u/student/2021/cs21resch15003/cs21mds14030/mca/SA-SSD/tools/result-%j.txt
                                                                                                                                                                                                                                                                                  
echo "SLURM_JOBID="$SLURM_JOBID                                                                                                          
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST                                                                                            
echo "SLURM_NNODES"=$SLURM_NNODES                                                                                                        
echo "SLURMTMPDIR="$SLURMTMPDIR                                                                                                          
echo "Date          	= $(date)"                                                                                                       
echo "Hostname      	= $(hostname -s)"                                                                                               
echo ""                                                                                                                                  
echo "Number of Nodes Allocated  	= $SLURM_JOB_NUM_NODES"
echo "Number of Tasks Allocated  	= $SLURM_NTASKS"
echo "Number of Cores/Task Allocated = $SLURM_CPUS_PER_TASK"
echo "Working Directory = $(pwd)"
echo "working directory = "$SLURM_SUBMIT_DIR

pwd; hostname
echo $CUDA_VISIBLE_DEVICES
#python3 -c 'print("hello world")'
source /u/student/2021/cs21resch15003/.bashrc
conda activate py3.7
#python3 train.py ../configs/car_cfg.py
python3 train1.py ../configs/car_cfg_SGD.py
sleep 20
exit 0
echo "== End of Job =="


