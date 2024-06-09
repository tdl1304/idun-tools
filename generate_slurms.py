from pathlib import Path
from datetime import datetime

data_dir = Path("./data/")
default_args = "--vis wandb --steps-per-eval-all-images 1000 --project-name naplab-experiments"

datasets = ["gnss","gnss+hloc-disk", "gnss+hloc-disk-masked", "gnss-masked"]#, "ns-processed", "ns-processed-masked"]
datasets = ["gnss+hloc-disk"]#, "gnss-masked"]

# model, args, mem, time
modeldict = {
    "nerfacto_30k": ["nerfacto", "--max-num-iterations 30000", "12G", "1:30:00"],
    "nerfacto_200k": ["nerfacto", "--max-num-iterations 200000", "12G", "5:30:00"],
    "mfnerf3x3_30k": ["mfnerf", "--pipeline.model.blocks-x 3 --pipeline.model.blocks-y 3 --max-num-iterations 30000", "16G", "3:15:00"],
    "mfnerf4x4_30k": ["mfnerf", "--pipeline.model.blocks-x 4 --pipeline.model.blocks-y 4 --max-num-iterations 30000", "16G", "3:15:00"],
    "mfnerf3x3_200k": ["mfnerf", "--pipeline.model.blocks-x 3 --pipeline.model.blocks-y 3 --max-num-iterations 200000", "16G", "9:30:00"],
    "mfnerf4x4_200k": ["mfnerf", "--pipeline.model.blocks-x 4 --pipeline.model.blocks-y 4 --max-num-iterations 200000", "16G", "13:30:00"],
}

affix = "hotfix"
date = "20240609"

Path.mkdir(Path("./slurms/"), exist_ok=True)
for i, dataset in enumerate(datasets):
    for j, model in enumerate(modeldict.keys()):
        modelobject = modeldict[model]
        with open(f"./slurms/{dataset}_{model}.slurm", "+w") as f:
            f.write("#! /usr/bin/bash\n")
            f.write(f"#SBATCH --job-name=\"{dataset}_{model}_{date}\"\n")
            f.write("#SBATCH --partition=GPUQ\n")
            f.write("#SBATCH --account=share-ie-idi\n")
            f.write(f"#SBATCH --time={modelobject[3]}\n") # change as needed
            f.write(f"#SBATCH --mem={modelobject[2]}\n") # change as needed
            f.write("#SBATCH --nodes=1\n")
            f.write("#SBATCH --cpus-per-task=4\n")
            f.write("#SBATCH --gres=gpu:1\n")
            f.write(f"#SBATCH --output=output_{dataset}_{model}.txt\n")
            f.write(f"#SBATCH --error=output_{dataset}_{model}.err\n")
            f.write("\ncd ${SLURM_SUBMIT_DIR}\n")
            f.write("echo \"Jobbnummer: ${SLURM_JOB_ID}\"\n")
            f.write("echo \"Jobbnavn: ${SLURM_JOB_NAME}\"\n")
            f.write("echo \"Job nodes: ${SLURM_JOB_NODELIST}\"\n")
            f.write("\nmodule load Anaconda3/2023.09-0\n")
            f.write("module load CUDA/11.8.0\n")
            f.write("\nconda activate nerfstudio\n")
            f.write(f"ns-train {modelobject[0]} {default_args} --experiment-name {dataset}_{model}_{date}_{affix} {modelobject[1]} nerfstudio-data --data {data_dir / dataset}")
