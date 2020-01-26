from Utils import *


## Arctan
def function(x):
  return np.arctan(x)
label_function = 'arctan'
execfile('04_experiments_act_fun.py')


## Tanh
def function(x):
  return np.tanh(x)
label_function = 'tanh'
execfile('04_experiments_act_fun.py')


## Relu
def function(x):
  return max(0.0, x)
label_function = 'relu'
execfile('04_experiments_act_fun.py')


## Sigmoid
def function(x):
  return 1 / (1 + math.exp(-4*x))
label_function = 'sigmoid'
execfile('04_experiments_act_fun.py')


## Elu
def function(z,alpha = .3):
	return z if z >= 0 else alpha*(e**z -1)
label_function = 'elu'
execfile('04_experiments_act_fun.py')

