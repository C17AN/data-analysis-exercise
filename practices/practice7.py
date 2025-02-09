import pandas as pd

# 2.1 고객별 총 구매 금액을 계산하세요.
# 2.2 상품별 평균 구매 금액을 구하세요.
# 2.3 각 고객이 구매한 상품의 개수를 계산하세요.

data = {
    "고객명": ["김철수", "이영희", "박민수", "김철수", "이영희", "박민수", "김철수"],
    "상품명": ["A", "B", "A", "C", "A", "B", "C"],
    "구매금액": [5000, 12000, 7000, 15000, 8000, 11000, 9000],
}

df = pd.DataFrame(data)

# groupby를

df["구매금액"].sum()  # 2.1
total_purchase = df.groupby("고객명")["구매금액"].sum()

avg_purchase = df.groupby("상품명")["구매금액"].mean()  # 2.2

product_purchage = df.groupby("고객명")["상품명"].count()  # 2.3
