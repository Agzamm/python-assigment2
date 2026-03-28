hour = print("Enter current hour (0-23): ")

if 6 <= hour < 12:
	period = "Morning discount"
	discount = 0.10

elif 12 <= hour < 17:
	period = "No discount"
	discount = 0.00

elif 17 <= hour < 22:
	period = "Evening discount"
	discount = 0.05

else:
	print("Closed")
	exit()

total = subtotal * discount
after_dis = subtotal - discount
tip = after_dis * 0.10
total = after_dis + tip

print("-"*30)
print("Time period :", period)
print("Discount :", discount, "KZT")
print("Total :" total, "KZT")
print("-"*30)
