# basic.py 用法
```
python basic.py <basic-train.txt的路徑> <basic-test.txt的路徑>
```
> 請自行填寫basic.py中的pick函式，並回傳shape為(test_data中的商品數目, k)的list

## basic_best_pick.py
> 選出能將Evaluation的值最大化的10人 

## basic_most_bid_winners.py
> 選出在basic-train當中得標次數前10多的人

# advanced.py 用法
```
python advanced.py <advanced-train.txt的路徑> <advanced-test.txt的路徑> <train-category.txt的路徑> <test-category.txt的路徑>
```
> 請自行填寫advanced.py中的pick函式，並回傳shape為(test_data中的商品數目, k)的list

## advanced_best_pick.py
> 依據分類選出每個類別中能將Evaluation的值最大化的10人

## advanced_most_bid_winners.py
> 選出每個類別在advanced-train當中得標次數前10多的人

# Warning
> basic-test.txt、advanced-test.txt和advanced-test-category.txt只有999個paintings。

# run.sh

> Unix-based system only! 
>
> K = 10

# Experiments

**All the data need to be put under ../prob_data/**

## K

```
./run_experiment.sh
```

> Iterate k from 1 to 500 and plot the hit-rate curve.
>
> **The code is not optimized and may have bad performance.**

## Bound of Evaluation

```
python3 experiment_bound.py
```

> Use basic_highest_average.py algorithm as default.