# Numpy Exercises

import numpy as np
from numpy import random

def exercise_1():
    """
    Select all even numbers from the np  array [1, 2, 3, 4, 5, 6, 7, 8].
    Output: [2, 4, 6, 8]
    """
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    return a[a % 2 == 0]

b = exercise_1()
print(b)

def exercise_2():
    x = random.randint(100, size=100)
    # print(x)
    print("Mean: ", np.mean(x))
    print("Sum: ", np.sum(x))
    print("STD: ", np.std(x))
    pass

exercise_2()

def exercise_3():

    x = random.randint(100, size= 12)
    matrix = x.reshape(3, 4)
    print(matrix)
    pass

exercise_3()

def exercise_4():
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    position = np.unravel_index(np.argmax(matrix), matrix.shape)
    print(position)
    pass

exercise_4()

def exercise_5():

    a1 = np.array([[1, 2], [3, 4]])
    a2 = np.array([[5, 6], [7, 8]])
    arr = a1 * a2
    print(arr)

    pass

exercise_5()

# Pandas

import pandas as pd

sales = pd.read_csv("week8_dataset/Sales.csv", sep="\t")

sales["Sales"] = (
    sales["Sales"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

sales["Cost"] = (
    sales["Cost"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# print(sales[["Sales", "Cost"]].head())
# print(sales.dtypes)

sales["Margin"] = (sales["Sales"] - sales["Cost"])

# print(sales.dtypes)

sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])
sales["OrderMonth"] = sales["OrderDate"].dt.month

# print(sales[["OrderDate", "OrderMonth"]].head())

monthly_margin = sales.groupby("OrderMonth")["Margin"].mean().sort_values(ascending=False).reset_index()

# print(monthly_margin)

most_profit = monthly_margin.iloc[0]

print(most_profit)

# Exercice 2

sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])
sales["OrderYear"] = sales["OrderDate"].dt.year

sales_2020 = sales[sales["OrderYear"] == 2020]

sales_person = pd.read_csv("week8_dataset/Salesperson.csv", sep="\t")

sales_average = pd.merge(sales_2020, sales_person, how="inner", on = "EmployeeKey")

sales_by_person = (
    sales_average
    .groupby("Salesperson", as_index=False)["Sales"]
    .sum()
)

top5 = (
    sales_by_person
    .sort_values("Sales", ascending=False)
    .head(5)
)

print(top5)

# Exercice 3

sales["Date"] = pd.to_datetime(sales["OrderDate"])
sales["Year"] = sales["Date"].dt.year
sales_2020 = sales[sales["Year"] == 2020]

product = pd.read_csv(
    "week8_dataset/Product.csv", sep="\t")

sales_product = pd.merge(sales_2020, product, how="inner", on = "ProductKey")

product_count = (sales_product.groupby("Category")["Quantity"].sum())

print(product_count)

#Exercice 4

target = pd.read_csv("week8_dataset/Targets.csv", sep="\t")

target["Target"] = (
    target["Target"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float))

target["Date"] = pd.to_datetime(target["TargetMonth"])
target["Year"] = target["Date"].dt.year

revenue = (sales.groupby("Year")[["Sales", "Margin"]].sum())
print(revenue)

target_year = (target.groupby("Year")["Target"].sum())

print(target_year)

rev_margin = pd.merge(revenue, target, how="inner", on="Year")
print(rev_margin)








