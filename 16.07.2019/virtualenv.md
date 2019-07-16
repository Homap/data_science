[For more information regarding virtualenv, check this youtube video](https://www.youtube.com/watch?v=nnhjvHYRsmM)

## Virtualenv

virtualenv is a tool to create isolated python environment. In this way, we can contain all the packages and
dependencies needed within one workspace in a folder in your computer.

`pip install virtualenv`

Create a virtual environment\
`virtualenv data_science_demo`

Activate the virtual environment\
`source data_science_demo/bin/activate`

Check python version\
`python --version`

### Create a python environment with a different version of python

Deactivate the running virtual env\
`virtualenv -p python2.7 data_science_python2`

`source data_science_python2/bin/activate`

Create an alias for the virtual environment in the bash profile create an alias:\
`alias dstuesday='source /path_to/data_science_demo/bin/activate'`

You can do all your python stuff in your environment. If you need specific configurations for a given project, you can put it in a box like this so anything else you do to your python packages will not affect this specific project. 

You can also use the command below in python3 to create virtual environment:\
`python3 -m venv data_science_demo_again`

`source data_science_demo_again/bin/activate`