customer = input("Enter customer name: ")

count = 0
subtotal = 0 

while True:
	item = input("Enter item name (or 'done' to finish): ")

	if item == "done":
		break
	count +=1

	price = int(input("Enter price: "))
	subtotal += price

print("="*30)
print("Customer: ", customer)
print("Items: ", count)
print("Subtotal: ", subtotal, "KZT")
print("="*30)


hour = int(input("Enter current hour (0-23): "))

if 6 <= hour < 12:
	period = "Morning discount"
	discount = 0.10

elif 12 <= hour < 17:
	period = "No discount"
	discount = 0

elif 17 <= hour < 22:
	period = "Evening discount"
	discount = 0.05

else:
	print("Closed")
	exit()

amount = subtotal * discount
after_dis = subtotal - amount
tip = after_dis * 0.10
total = after_dis + tip

print("="*30)
print("Time period :", period)
print("Discount :", discount, "KZT")
print("Total :", total, "KZT")
print("="*30)

print("Name uppercase :", customer.upper())
print("Name lowercase :", customer.lower())
print("Name length :", len(customer))
print("-"*30)
if customer[0].upper() == 'A' or customer[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
print("="*30)