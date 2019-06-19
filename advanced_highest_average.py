import numpy as np 
import sys
import os
from time import time
import matplotlib.pyplot as plt

EXPERIMENT = False


def reading_data(path1, path2, path3, path4):
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

def pick(training_data, testing_data, training_labels, testing_labels, K=10):
	sums1 = np.zeros((training_data.shape[0], ), dtype=np.float64)
	sums2 = np.zeros((training_data.shape[0], ), dtype=np.float64)
	sums3 = np.zeros((training_data.shape[0], ), dtype=np.float64)
	for i, label in enumerate(training_labels):
		if label == '001':
			sums1 += training_data[:, i]
		elif label == '002':
			sums2 += training_data[:, i]
		elif label == '003':
			sums3 += training_data[:, i]

	best_winners1 = np.argsort(sums1)[::-1][:K:]
	best_winners2 = np.argsort(sums2)[::-1][:K:]
	best_winners3 = np.argsort(sums3)[::-1][:K:]

	out_array = []
	for label in testing_labels:
		if label == '001':
			out_array.append(best_winners1)
		elif label == '002':
			out_array.append(best_winners2)
		elif label == '003':
			out_array.append(best_winners3)

	return out_array	#Please return a array with shape = (testing_data.shape[1], k)

def evaluate(picked_people, training_data, testing_data, training_labels, testing_labels):
	cnt_correct_pick = 0.0
	for i in range(testing_data.shape[1]):
		max_bid = 0
		for j in range(testing_data.shape[0]):
			if testing_data[j][i] > testing_data[max_bid][i]:
				max_bid = j
		if max_bid in picked_people[i]:
			cnt_correct_pick += 1

	result = cnt_correct_pick/testing_data.shape[1]
	print("Evaluation :", result)
	return result

if __name__ == '__main__':
	training_data, testing_data, training_labels, testing_labels = reading_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	if sys.argv[len(sys.argv)-1] == '-e':
		EXPERIMENT = True
		
	if EXPERIMENT:
		var = range(1, 500)
	else:
		var = [10]

	results = []
	for k in var:
		print(f'[K = {k}]', end='')
		picked_people = pick(training_data, testing_data, training_labels, testing_labels, k)
		results.append(evaluate(picked_people, training_data, testing_data, training_labels, testing_labels))

	if EXPERIMENT:
		plt.plot(range(1, 500), results)
		plt.xlabel('K')
		plt.ylabel('hit rate')
		plt.show()