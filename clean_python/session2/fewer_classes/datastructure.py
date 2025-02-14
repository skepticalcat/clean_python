
# TODO replace the class with a named tuple


class ModelParameters:

    def __init__(self, learning_rate, batch_size, epoch_max_num, hidden_layers_num):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.epoch_max_num = epoch_max_num
        self.hidden_layers_num = hidden_layers_num

# TODO bonus - what is the disadvantage with named tuples? Find out and use the dataclass decorator to implement a dataclass instead