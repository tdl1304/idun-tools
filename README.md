# idun-tools
Tools and scripts for experimenting with NeRF on NTNUs supercomputer IDUN
Running the tool will generate a lot of logs, use clearlogs.sh to delete all .txt and .err files in current directory.

## Configure
- Your own user name in cancel.sh
- Experiments in generate_slurms.py

## How to do
- Login to idun login cluster (ssh recommended `ssh user@idun-login1.hpc.ntnu.no`)
- Modify generate_slurms.py with your custom datasets and models
- Run run.sh `sh run.sh`
- Render a completed NeRF run and predefined camera path with `sh run.sh`
