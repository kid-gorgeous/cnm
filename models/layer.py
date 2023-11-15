from __future__ import annotations
from typing import List, Callable, Optional

import os
import yaml
import numpy as np

from math import exp
from typing import List
from neuron import Neuron
from random import random 
from termcolor import colored

float = np.float32

# Helpers becuase they didnt work in the util directory
# dot product of two vectors
def dot(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))

# sigmoid function
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)

# Importing python libraries 
from typing import List, Callable, Optional
from random import random
from neuron import Neuron
# from util import dot, sigmoid, derivative_sigmoid

# Class model
class Layer: 
    def __init__(self, previous_layer: Optional[Layer], num_neurons: int,
                 learning_rate: float, activation_function: Callable[[float], float],
                 derivation_activation_function: Callable[[float], float]) -> None:
        self.previous_layer: Optional[Layer] = previous_layer
        self.neurons: List[Neuron] = []

        

        
