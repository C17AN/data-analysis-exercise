import pandas as pd
import numpy as np

# 4.1 이메일에서 도메인(naver.com, gmail.com 등)만 추출하여 새로운 컬럼 ‘도메인’에 저장하세요.
# 4.2 이름이 ‘철수’인 경우만 ‘이름’을 ‘Mr. 철수’로 변경하세요.

df = pd.DataFrame(
    {
        "이름": ["철수", "영희", "민수", "지현"],
        "이메일": [
            "chulsoo@gmail.com",
            "younghee@naver.com",
            "minsu@kakao.com",
            "jihyun@gmail.com",
        ],
    }
)

# # 4.1
email_row = df["이메일"]
domain_row = email_row.map(lambda x: x.split("@")[1])
df["도메인"] = domain_row

# # 4.2
df.loc[df["이름"] == "철수", "이름"] = "Mr. 철수"
