#! /usr/bin/bash
#SBATCH --job-name="naplab-rendering0_20240609"
#SBATCH --partition=GPUQ
#SBATCH --account=share-ie-idi
#SBATCH --time=6:00:00
#SBATCH --mem=10G
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --output=output_carla-render0.txt
#SBATCH --error=output_carla-render0.err

cd ${SLURM_SUBMIT_DIR}
echo "Jobbnummer: ${SLURM_JOB_ID}"
echo "Jobbnavn: ${SLURM_JOB_NAME}"
echo "Job nodes: ${SLURM_JOB_NODELIST}"

module load Anaconda3/2023.09-0
module load CUDA/11.8.0
module load FFmpeg/6.0-GCCcore-12.3.0

conda activate nerfstudio
ns-render camera-path --load-config outputs/gnss+hloc-disk_mfnerf4x4_200k_20240609_hotfix/mfnerf/2024-06-09_060208/config.yml --camera-path-filename data/gnss+hloc-disk/camera_paths/2024-06-09-14-15-13.json --output-path renders/naplab/gnss+hloc_mfnerf4x4_200k.mp4