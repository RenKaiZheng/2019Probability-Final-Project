import numpy as np 
import sys
import os
from time import time

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

def pick(training_data, testing_data, training_labels, testing_labels):
	bid_winners = np.argmax(training_data, axis = 0)
	win_bid_cnt1 = np.zeros((training_data.shape[1], ), dtype=int)
	win_bid_cnt2 = np.zeros((training_data.shape[1], ), dtype=int)
	win_bid_cnt3 = np.zeros((training_data.shape[1], ), dtype=int)
	for winner, label in zip(bid_winners, training_labels):
		if label == '001':
			win_bid_cnt1[winner] += 1
		elif label == '002':
			win_bid_cnt2[winner] += 1
		elif label == '003':
			win_bid_cnt3[winner] += 1

	best_winners1 = np.argsort(win_bid_cnt1)[::-1][:10:]
	best_winners2 = np.argsort(win_bid_cnt2)[::-1][:10:]
	best_winners3 = np.argsort(win_bid_cnt3)[::-1][:10:]

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

	print("Evaluation :", cnt_correct_pick/testing_data.shape[1])
	return

if __name__ == '__main__':
	training_data, testing_data, training_labels, testing_labels = reading_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	picked_people = pick(training_data, testing_data, training_labels, testing_labels)
	evaluate(picked_people, training_data, testing_data, training_labels, testing_labels)