import pandas as pd

# q1
df = pd.read_csv(
    "https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv", delimiter="\t"
)

# q2
df.head()

# q3
df.shape
row = df.shape[0]
col = df.shape[1]
print(row, col)


# q4
df.columns

# q5
df.columns[5]

# q6
df.iloc[:, 5].dtype
