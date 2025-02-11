# 다음 데이터에서 특정 조건을 만족하는 데이터를 찾아보세요.

# df = pd.DataFrame({
#     '이름': ['철수', '영희', '민수', '지현'],
#     '점수': [85, 92, 78, 95]
# })
# 4.1 점수를 기준으로 내림차순 정렬하세요.
# 4.2 점수가 90 이상인 사람만 출력하세요.

import pandas as pd
import numpy as np

df = pd.DataFrame({"이름": ["철수", "영희", "민수", "지현"], "점수": [85, 92, 78, 95]})

df.sort_values(by="점수", ascending=False)[df["점수"] >= 90]
