from collections import namedtuple
from dataclasses import dataclass

# TODO replace the class with a named tuple

ModelParameters = namedtuple("ModelParameters", ["learning_rate", "batch_size", "epoch_max_num", "hidden_layers_num"])
params = ModelParameters(0.001, 256, 1000, 4)
try:
    params.epoch_max_num = 1500
except AttributeError:
    print("Tuples are immutable!")

# TODO bonus - what is the disadvantage with named tuples? Find out and use the dataclass decorator to implement a dataclass instead

@dataclass
class ModelParameters:
    learning_rate: float
    batch_size: int
    epoch_max_num: int
    hidden_layers_num: int


params = ModelParameters(0.001, 256, 1000, 4)
params.epoch_max_num = 1500
