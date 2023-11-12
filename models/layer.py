from __future__ import annotations
from typing import List, Callable, Optional

import os
import yaml

from neuron import Neuron
from random import random 
from termcolor import colored



# TODO: automate the user feature 
# The next 13 lines of code are used to load the configuration file to create a symbolic link for the user name
# to Load the configuration file and import the utils folder
with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    env_user = config['user']

# Get the environment variable name from the YAML file 
# user = str(os.getenv(env_user))
print(colored(f"User: {env_user}", 'red'))

# Adding the path to the utils folder and main directory 
import sys
sys.path.append(f'/Users/{env_user}/cnm/utils')
sys.path.append(f'/Users/{env_user}/cnm')

from util import dot, sigmoid, derivative_sigmoid
print(colored("Importing Neuron class from neuron.py", 'green'))
print(colored("Util name: ", 'green'), util.__name__)