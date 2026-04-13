import datetime

sales_data = {}

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per unit: "))
    sales_data[name] = (quantity, price)

total_revenue = sum(qty * price for qty, price in sales_data.values())

highest_product = max(sales_data.items(), key=lambda item: item[1][0])

# Display report
print("\n--- SALES REPORT ---")
print("Date:", datetime.now().strftime("%Y-%m-%d"))
print("Total Revenue:", total_revenue)
print("Highest Selling Product:", highest_product[0])
print("Units Sold:", highest_product[1][0])