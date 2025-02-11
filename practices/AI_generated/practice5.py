# 다음과 같은 배열을 Pandas DataFrame으로 변환한 뒤, 데이터를 변형하세요.

# import numpy as np
# import pandas as pd

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# 5.1 이 배열을 DataFrame으로 변환하세요. (컬럼 이름: A, B, C)
# 5.2 컬럼 'A'의 값을 모두 제곱하세요.
# 5.3 컬럼 'B'의 평균을 구하세요.


import pandas as pd
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

df = pd.DataFrame(data=arr, index=["A", "B", "C"])
np.pow(df.loc["A"], 2)
df.loc["B"].mean()
