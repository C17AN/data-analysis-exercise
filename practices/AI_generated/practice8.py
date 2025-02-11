import pandas as pd
import numpy as np

# 3.1 ‘나이’의 **이상치(비정상적인 값)**를 찾아 제거하세요. (나이 범위를 0~100으로 제한)
# 3.2 ‘나이’의 결측치는 평균 나이로 채우세요.
# 3.3 ‘점수’의 결측치는 **중앙값(median)**으로 채우세요.

data = {
    "이름": ["철수", "영희", "민수", "지현", "수진", "도윤"],
    "나이": [23, 21, 22, np.nan, 130, 25],  # 130은 이상치
    "점수": [85, 92, np.nan, 95, 88, 77],
}

df = pd.DataFrame(data)

# df.loc은 단일 행을 찾는 용도가 아니라, 조건과 일치하는 모든 행을 찾는다.
# loc["행", "열"]
mean_age = df.loc[df["나이"].between(0, 100), "나이"].mean()

df[df["나이"].between(0, 100)]  # 3.1

df.loc[~df["나이"].between(0, 100), "나이"] = mean_age

df["나이"].fillna(df["나이"].mean(), inplace=True)  # 3.2
df["점수"].fillna(df["점수"].mean(), inplace=True)  # 3.3
