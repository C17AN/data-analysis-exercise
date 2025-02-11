import pandas as pd
import numpy as np

# 5.1 이 데이터를 이름을 행(index), 과목을 열(columns)로 하는 피벗 테이블로 변환하세요.
# 5.2 수학과 영어 점수의 평균을 구하세요.
# 5.3 영어 점수가 90점 이상인 학생만 출력하세요.

df = pd.DataFrame(
    {
        "이름": ["철수", "영희", "민수", "철수", "영희", "민수"],
        "과목": ["수학", "수학", "수학", "영어", "영어", "영어"],
        "점수": [80, 90, 85, 70, 95, 88],
    }
)

# 5.1
pivot_df = df.pivot_table(columns="이름", index="과목", values="점수")
pivot_df

df

# # 5.2
# df.groupby("과목")["점수"].mean()

# # 5.3
# df.loc[(df["점수"] >= 90) & (df["과목"] == "영어")]
