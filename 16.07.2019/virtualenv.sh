# Source: https://www.youtube.com/watch?v=nnhjvHYRsmM

# Virtualenv
# Example of g4hunter.py

# virtualenv is a tool to create isolated Python environment. In this way, we can contain all the packages and
# dependencies needed within one workspace in a folder in your computer.

pip install virtualenv

# Create a virtual environment
virtualenv data_science_demo

# activate the virtual environment
source data_science_demo/bin/activate

# check python version
python --version

# Create a python environment with a different version of
# python

# Deactivate the running virtual env
virtualenv -p python2.7 data_science_python2

source data_science_python2/bin/activate

# create an alias for the virtual environment
# in the bash profile create an alias:
alias dstuesday='source /Users/homa/Documents/data_science/16.07.2019/data_science_demo/bin/activate'

# you can do all your python stuff in your environment. If you need specific configurations for a given project, you can put it in a box like this so anything else you do to your python packages will not affect this specific project. 

# with python3
python3 -m venv data_science_demo_again
source data_science_demo_again/bin/activate