customer = input("Enter customer name: ")

item = []
count = 0
subtotal = 0 

while True:
	item = input("Enter item name (or 'done' to finish): ")
	count +=1

	if item == "done":
		break

	price = int(input("Enter price: "))
	subtotal += price


print("Customer: ", customer)
print("Items: ", count)
print("Subtotal: ", subtotal, "KZT")