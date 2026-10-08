import pandas as pd

sales_data = [
    {"product": "Laptop", "quantity": 5, "price": 50000},
    {"product": "Mouse", "quantity": 15, "price": 500},
    {"product": "Keyboard", "quantity": 10, "price": 1500}
]

df = pd.DataFrame(sales_data )
# print(df)

df["total_price"] = df["quantity"] * df["price"]
# print(df["total_price"])

total_revenue = df["total_price"].sum()
# print(total_revenue )

average = df["price"].mean()
# print(average)

top_product = df.loc[df["total_price"].idxmax()]
print(top_product)