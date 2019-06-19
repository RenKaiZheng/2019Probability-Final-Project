#! /bin/bash

basic_path='../prob_data/basic-train.txt ../prob_data/basic-test.txt'
advanced_path='../prob_data/advanced-train.txt ../prob_data/advanced-test.txt  ../prob_data/advanced-train-category.txt  ../prob_data/advanced-test-category.txt'

echo -e "\nbasic_most_bid_winners.py"
python3 ./basic_most_bid_winners.py $basic_path
echo -e "\nbasic_best_pick.py"
python3 ./basic_best_pick.py $basic_path
echo -e "\nbasic_highest_average.py"
python3 ./basic_highest_average.py $basic_path

echo -e "\nadvanced_most_bid_winners.py"
python3 advanced_most_bid_winners.py $advanced_path
echo -e "\nadvanced_best_pick.py"
python3 advanced_best_pick.py $advanced_path
echo -e "\nadvanced_highest_average.py"
python3 advanced_highest_average.py $advanced_path
