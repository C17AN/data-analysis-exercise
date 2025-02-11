import numpy as np

# 1.1 각 행(row)의 합을 구하세요.
# 1.2 각 열(column)의 평균을 구하세요.
# 1.3 배열의 최대값과 최소값을 찾아 출력하세요.
# 1.4 배열을 오름차순 정렬하세요. (각 행 기준)

arr = np.random.randint(1, 100, size=(5, 4))


sum(arr)  # 1.1
arr.mean(axis=1)  # 1.2
arr.max(), arr.min()  # 1.3
arr.sort()  # 1.4
