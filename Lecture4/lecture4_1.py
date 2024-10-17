
S = "milk 18.20, butter 65.00, cheese cake 125.00"


goods = []
items = S.split(", ")

for item in items:
    name_price = item.rsplit(" ", 1) 
    goods.append({"name": name_price[0], "price": float(name_price[1])})

cheapest_product = ""
cheapest = float('inf')
for product in goods:
    if product["price"]<cheapest:
        cheapest = product["price"]
        cheapest_product = product["name"]

most_expensive_product = ""
most_expensive = 0
for good in goods:
    if product["price"]>most_expensive:
        most_expensive = product["price"]
        most_expensive_product = product["name"]

total_price = sum(item["price"] for item in goods)
average_price = total_price / len(goods)

total_sum = total_price

print("Cheapest product:", cheapest_product)
print("Most expensive product:", most_expensive_product)
print("Average price:", average_price)
print("Total sum:", total_sum)