name = input("Enter your name:")
answer = " "
while answer != "no":
    product_name =input("Enter product name:")
    quantity1 = int(str(input("Enter quantiy of " + product_name + ':' )))
    price1 = int(input("Enter price of " + product_name + ':' ))
    add_product = bool(input("Add another product (yes or no): "))  
    total1 = quantity1 * price1
    #total2 = quantity2 * price2
    #answer = " "

    #if answer != "no":
    product_name =input("Enter product name:")
    quantity2 = int(str(input("Enter quantiy of " + product_name + ':' )))
    price2 = int(input("Enter price of " + product_name + ':' ))
    answer = str(input("Add another product (yes or no): "))
    total2 = quantity2 * price2
 
    break      
print("Total bill is ", total1 + total2)
