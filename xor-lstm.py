import tensorflow as tf
import numpy as np
from tf.nn.rnn_cell import *

multi_rnn_cell = MultiRNNCell([LSTMCell(size) for size in [10, 10, 10]])
outputs, state = tf.nn.dynamic_rnn(cell=multi_rnn_cell, inputs=data, dtype=tf.float32)

initial_state = state = 
