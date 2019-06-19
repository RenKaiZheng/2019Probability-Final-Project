import numpy as np 
import sys
import os
from time import time

def reading_data(path1='../prob_data/advanced-train.txt', 
				path2='../prob_data/advanced-test.txt', 
				path3='../prob_data/advanced-train-category.txt', 
				path4='../prob_data/advanced-test-category.txt'):
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

	training_labels = []
	with open(path3, 'r') as fp:
		line = fp.read()
		categories = line.split()
		for category in categories:
			training_labels.append(category)

	testing_labels = []
	with open(path4, 'r') as fp:
		line = fp.read()
		categories = line.split()
		for category in categories:
			testing_labels.append(category)

	return np.array(training_data), np.array(testing_data), np.array(training_labels), np.array(testing_labels)

def pick(training_data, testing_data, training_labels, testing_labels):
	#TODO
	return [[] for i in range(testing_data.shape[1])]	#Please return a array with shape = (testing_data.shape[1], k)

def evaluate(picked_people, training_data, testing_data, training_labels, testing_labels):
	cnt_correct_pick = 0.0
	for i in range(testing_data.shape[1]):
		max_bid = 0
		for j in range(testing_data.shape[0]):
			if testing_data[j][i] > testing_data[max_bid][i]:
				max_bid = j
		if max_bid in picked_people[i]:
			cnt_correct_pick += 1

	print("Evaluation :", cnt_correct_pick/testing_data.shape[1])
	return

if __name__ == '__main__':
	training_data, testing_data, training_labels, testing_labels = reading_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	picked_people = pick(training_data, testing_data, training_labels, testing_labels)
	evaluate(picked_people, training_data, testing_data, training_labels, testing_labels)