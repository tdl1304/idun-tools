rm -rf slurms
python generate_slurms.py
echo "slurms generated"
for i in slurms/*.slurm; do sbatch $i; done
