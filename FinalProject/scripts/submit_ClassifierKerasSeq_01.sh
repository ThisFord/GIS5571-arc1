#!/bin/bash -l        

#SBATCH --time=0:20:00 #time requested
#SBATCH -p k40 #node id
#SBATCH --gres=gpu:k40:1 #node id
#SBATCH --ntasks=4 
#SBATCH --mem=32g
#SBATCH --tmp=16g
#SBATCH --mail-type=ALL  
#SBATCH --mail-user=ford0161@umn.edu 

# Change directory to home directory
# This makes sure we ALWAYS start in home directory and then navigate from there.
cd ~

# Using E.Shook's access and the pre assigned geocomp directory for this script
# Change directory to advgeocomp2022

cd advgeocomp2022


# install tensorflow
module load tensorflow #this is the recommended way to install keras on MSI per documentation

pip install --user matplotlib keras numpy # must include --user or admin privaleges will error out

# Run the test python script 
python3 kerassequentialadjustedmodel.py
