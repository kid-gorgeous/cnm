
import os
import yaml
from termcolor import colored

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

# Setting global variables for the enviornment 
import numpy as np
float = np.float32

# Importing python libraries
from typing import List, Callable
from util import dot, sigmoid, derivative_sigmoid

print(colored("Importing Neuron class from neuron.py", 'green'))
print(colored("Util name: ", 'green'), util.__name__)

class Neuron:
    def __init__(self, weights: List[float], learning_rate: float, activation_function: Callable[[float], float], derivation_function: Callable[[float], float]) -> None:
        self.weights = weights
        self.activation_function: Callable[[float], float] = activation_function
        self.derivation_function: Callable[[float], float] = derivation_function

        self.learning_rate: float = learning_rate
        self.output_cache: float = 0.0
        self.delta: float = 0.0

    def output(self, inputs: List[float]) -> float:
        self.output_cache = dot(inputs, self.weights)
        return self.activation_function(self.output_cache)


if __name__ == '__main__':
    # n = Neuron([0.5, 0.3, 0.2], 0.1, sigmoid, derivative_sigmoid)
    pass

