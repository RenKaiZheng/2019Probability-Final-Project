import numpy as np 
import sys
import os
from time import time
import matplotlib.pyplot as plt
import basic
import basic_highest_average

if __name__ == "__main__":
    training_data, testing_data = basic.reading_data()
    picked_people = basic_highest_average.pick(training_data, testing_data)
    print('Experimenting on bound...')
    for bound in range(1, 51):
        print(f'[bound: {bound}]', end='')
        basic.evaluate(picked_people, training_data, testing_data, bound)