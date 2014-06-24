from numpy.random import RandomState
import matplotlib.pyplot as plt
random_generator = RandomState(seed=55)
r = random_generator.uniform(0., 1., size=200)
