
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
float = np.float32 # this could break things but it's worth a shot

# Importing python libraries
from typing import List, Callable
from util import dot, sigmoid, derivative_sigmoid
print(colored("Importing Neuron class from neuron.py", 'green'))

# This is my first attempt at creating a neural network from scratch for our 
# project. I will be testing a handcrafted approach, and a packeged approach in parallel
# This model is from a Python book im using, I'm only going to test it for a week.
class Neuron:
        # This is the constructor for the Neuron class.
        # The constructor takes in the following parameters:
        #   weights: a list of weights for the neuron
        #   learning_rate: a float value for the learning rate
        #   activation_function: a function for the activation function
        #   derivation_function: a function for the derivation of the activation function

        # The constructor returns the following:
        #   None

        # The constructor initializes the following:
        #   self.weights: a list of weights for the neuron
        #   self.activation_function: a function for the activation function
        #   self.derivation_function: a function for the derivation of the activation function
        #   self.learning_rate: a float value for the learning rate
        #   self.output_cache: a float value for the output cache
        #   self.delta: a float value for the delta

        # The constructor does the following:
        #   1. Initializes the weights, learning_rate, activation_function, and derivation_function
        #   2. Initializes the output_cache and delta to 0.0


    def __init__(self, weights: List[float], learning_rate: float, activation_function: Callable[[float], float], derivation_function: Callable[[float], float]) -> None:
        self.weights = weights
        self.activation_function: Callable[[float], float] = activation_function
        self.derivation_function: Callable[[float], float] = derivation_function

        self.learning_rate: float = learning_rate
        self.output_cache: float = 0.0
        self.delta: float = 0.0

    def output(self, inputs: List[float]) -> float:
        self.output_cache = dot(inputs, self.weights) # im not sure if im importing this right yet
        return self.activation_function(self.output_cache)

   

if __name__ == '__main__':
    # n = Neuron([0.5, 0.3, 0.2], 0.1, sigmoid, derivative_sigmoid)
    pass

