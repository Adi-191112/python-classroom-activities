selling_price = int(input("Enter the selling price"))
actual_price = int(input("Enter the actual price"))
if(selling_price > actual_price):
    profit = selling_price - actual_price
    print("profit is",  profit)
else:
    print("loss")