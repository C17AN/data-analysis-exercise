# 주어진 리스트를 NumPy 배열로 변환하고, 다음 연산을 수행하세요.

# data = [10, 20, 30, 40, 50]
# 1.1 배열의 모든 원소에 2를 곱하세요.
# 1.2 배열의 평균을 구하세요.
# 1.3 배열의 최대값과 최소값을 구하세요.

import numpy as np

data = [10, 20, 30, 40, 50]
arr = np.array(data)
data_multiplied = arr * 2
data_mean = arr.mean()
data_max = arr.max()
data_min = arr.min()

data_multiplied
data_mean
data_min
data_max
