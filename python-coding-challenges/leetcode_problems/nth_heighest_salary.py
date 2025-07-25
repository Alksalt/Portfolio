import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].dropna().drop_duplicates().sort_values(ascending=False)
    column = f'getNthHighestSalary({N})'
    value = [salaries.iloc[N-1] if len(salaries) >= N else None]
    if N >= 1:
        return pd.DataFrame({column:value})
    else:
        return pd.DataFrame({column: [None]})
data1 = {
    "id": [1, 2, 3],
    "salary": [100, 200, 300]
}
df1 = pd.DataFrame(data1)

# Example 2
data2 = {
    "id": [1],
    "salary": [100]
}
df2 = pd.DataFrame(data2)

print(nth_highest_salary(df1, 2))