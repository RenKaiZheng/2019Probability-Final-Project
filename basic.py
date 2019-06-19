import numpy as np 
import sys
import os
from time import time

def reading_data(path1='../prob_data/basic-train.txt', path2='../prob_data/basic-test.txt'):
	training_data = []
	with open(path1, 'r') as fp:
		for line in open(path1, 'r'):
			line = fp.readline()
			bid_record = list(map(float, line.split()))
			training_data.append(bid_record)

	testing_data = []
	with open(path2, 'r') as fp:
		for line in open(path2, 'r'):
			line = fp.readline()
			bid_record = list(map(float, line.split()))
			testing_data.append(bid_record)

	return np.array(training_data), np.array(testing_data)

def pick(training_data, testing_data):
	#TODO
	return [[] for i in range(testing_data.shape[1])]	#Please return a array with shape = (testing_data.shape[1], k)

def evaluate(picked_people, training_data, testing_data, bound=1):
	cnt_correct_pick = 0.0
	for i in range(testing_data.shape[1]):
		current_round = testing_data[:, i]
		max_bid_list = np.argsort(current_round)[::-1][:bound]
		
		for max_bid in max_bid_list:
			if max_bid in picked_people[i]:
				cnt_correct_pick += 1
				break

	result = cnt_correct_pick/testing_data.shape[1]
	print("Evaluation :", result)
	return result


if __name__ == '__main__':
	training_data, testing_data = reading_data(sys.argv[1], sys.argv[2])
	picked_people = pick(training_data, testing_data)
	evaluate(picked_people, training_data, testing_data)