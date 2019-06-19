import numpy as np 
import sys
import os
from time import time
import matplotlib.pyplot as plt
import basic
import advanced
import basic_highest_average
import basic_most_bid_winners
import advanced_highest_average
import advanced_most_bid_winners

if __name__ == "__main__":
    print('Experimenting on bound...')
    experiments = range(1, 51, 2)

    training_data, testing_data = basic.reading_data()

    print('\nbasic_highest_average: ')
    picked_people = basic_highest_average.pick(training_data, testing_data)
    for bound in experiments:
        print(f'[bound: {bound}]', end='')
        basic.evaluate(picked_people, training_data, testing_data, bound)

    print('\nbasic_most_bid_winners: ')
    picked_people = basic_most_bid_winners.pick(training_data, testing_data)
    for bound in experiments:
        print(f'[bound: {bound}]', end='')
        basic.evaluate(picked_people, training_data, testing_data, bound)


    training_data, testing_data, training_labels, testing_labels = advanced.reading_data()

    print('\nadvanced_highest_average')
    picked_people = advanced_highest_average.pick(training_data, testing_data, training_labels, testing_labels)
    for bound in experiments:
        print(f'[bound: {bound}]', end='')
        basic.evaluate(picked_people, training_data, testing_data, bound)

    print('\nadvanced_most_bid_winners')
    picked_people = advanced_most_bid_winners.pick(training_data, testing_data, training_labels, testing_labels)
    for bound in experiments:
        print(f'[bound: {bound}]', end='')
        basic.evaluate(picked_people, training_data, testing_data, bound)