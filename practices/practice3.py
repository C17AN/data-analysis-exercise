# 다음 데이터가 포함된 pandas DataFrame이 있다고 가정합니다.

# import pandas as pd
# import numpy as np

# data = {
#     '이름': ['철수', '영희', '민수', '지현'],
#     '나이': [23, 21, np.nan, 20],
#     '점수': [85, 92, 78, np.nan]
# }

# df = pd.DataFrame(data)
# 3.1 ‘나이’ 또는 ‘점수’에 결측치(NaN)가 있는 행을 제거하세요.
# 3.2 ‘나이’의 결측치는 평균 나이로 채우세요.
# 3.3 ‘점수’의 결측치는 0으로 채우세요.

import pandas as pd
import numpy as np

data = {
    "이름": ["철수", "영희", "민수", "지현"],
    "나이": [23, 21, np.nan, 20],
    "점수": [85, 92, 78, np.nan],
}

df = pd.DataFrame(data)

df.dropna(
    axis="index",
)

df["나이"].fillna(df["나이"].mean(), inplace=True)

df["점수"].fillna(0, inplace=True)

df
