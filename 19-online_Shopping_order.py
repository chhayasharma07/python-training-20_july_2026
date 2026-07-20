# Problem Statement: Online Shopping Order Management System (Dictionary with List of Dictionaries)
# Objective
# Develop an Online Shopping Order Management System using Python Dictionaries where a list of dictionaries is stored inside another dictionary. This intermediate-level problem helps learners understand nested dictionaries, lists, searching, updating, and data manipulation.

# Scenario
# An e-commerce company wants to maintain customer order details.
# Each customer is represented by a dictionary, and all purchased products are stored as a list of dictionaries inside that customer dictionary.
# Data Structure
# customer = {
#     "CustomerId": 101,
#     "CustomerName": "Rahul Sharma",
#     "City": "Noida",
#     "Orders": [
#         {
#             "ProductId": 1,
#             "ProductName": "Laptop",
#             "Quantity": 1,
#             "Price": 65000
#         },
#         {
#             "ProductId": 2,
#             "ProductName": "Mouse",
#             "Quantity": 2,
#             "Price": 800
#         }
#     ]
# }
# The application should maintain multiple customers using a list.
# customers = [
#     customer1,
#     customer2,
#     customer3
# ]

# Requirements
# Create a menu-driven application that performs the following operations.

# Operation 1 – Add New Customer
# Accept the following details:
# Customer ID 
# Customer Name 
# City 
# Initially, the customer will have no orders.

# Operation 2 – Add Product Order
# Ask the user for:
# Customer ID 
# Product ID 
# Product Name 
# Quantity 
# Price 
# Create a product dictionary and add it to the customer's Orders list.

# Operation 3 – View All Customers and Their Orders
# Display all customer details along with every ordered product.
# Example Output
# Customer ID : 101
# Customer Name : Rahul Sharma
# City : Noida

# Orders

# Product ID : 1
# Product Name : Laptop
# Quantity : 1
# Price : 65000

# Product ID : 2
# Product Name : Mouse
# Quantity : 2
# Price : 800

# ----------------------------------------

# Operation 4 – Search Customer
# Search using Customer ID.
# Display complete customer information including all orders.
# If not found:
# Customer not found.

# Operation 5 – Update Product Quantity
# Input:
# Customer ID 
# Product ID 
# New Quantity 
# Update only the product quantity.

# Operation 6 – Remove a Product
# Input:
# Customer ID 
# Product ID 
# Delete the selected product from the customer's order list.

# Operation 7 – Calculate Total Order Value
# Ask the user for a Customer ID.
# Calculate:
# Total Amount = Quantity × Price
# for every product and display the final bill.
# Example
# Laptop  : 65000
# Mouse   : 1600

# ------------------------
# Total Bill : 66600

# Operation 8 – Display Customer with Maximum Order Value
# Find the customer whose total purchase amount is highest.
# Display:
# Customer Name 
# Total Amount 

# Operation 9 – Exit
# Terminate the application.

# Constraints
# Store customers using a list. 
# Each customer must be stored as a dictionary. 
# Product details must be stored as a list of dictionaries inside the customer dictionary. 
# Do not use classes. 
# Validate Customer ID before performing operations. 
# Display meaningful messages for invalid operations. 

# Sample Data
# customers = [
#     {
#         "CustomerId": 101,
#         "CustomerName": "Rahul Sharma",
#         "City": "Noida",
#         "Orders": [
#             {
#                 "ProductId": 1,
#                 "ProductName": "Laptop",
#                 "Quantity": 1,
#                 "Price": 65000
#             },
#             {
#                 "ProductId": 2,
#                 "ProductName": "Mouse",
#                 "Quantity": 2,
#                 "Price": 800
#             }
#         ]
#     },
#     {
#         "CustomerId": 102,
#         "CustomerName": "Priya Singh",
#         "City": "Delhi",
#         "Orders": [
#             {
#                 "ProductId": 3,
#                 "ProductName": "Keyboard",
#                 "Quantity": 1,
#                 "Price": 2500
#             }
#         ]
#     }
# ]

customers=[]

def add_customer(customers):
    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:
        if customer["CustomerId"]==customer_id:
            print("Customer ID already exists.")
            return

    customer_name=input("Enter Customer Name:")
    city=input("Enter City:")

    customer={
        "CustomerId":customer_id,
        "CustomerName":customer_name,
        "City":city,
        "Orders":[]
    }

    customers.append(customer)
    print("Customer added successfully.")


def add_product(customers):
    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:
        if customer["CustomerId"]==customer_id:

            product_id=int(input("Enter Product ID:"))

            for product in customer["Orders"]:
                if product["ProductId"]==product_id:
                    print("Product ID already exists.")
                    return

            product_name=input("Enter Product Name:")
            quantity=int(input("Enter Quantity:"))
            price=int(input("Enter Price:"))

            product={
                "ProductId":product_id,
                "ProductName":product_name,
                "Quantity":quantity,
                "Price":price
            }

            customer["Orders"].append(product)
            print("Product added successfully.")
            return

    print("Customer not found.")


def view_customers(customers):

    if len(customers)==0:
        print("No customers found.")

    else:
        for customer in customers:

            print("----------------------------------------")
            print("Customer ID :",customer["CustomerId"])
            print("Customer Name :",customer["CustomerName"])
            print("City :",customer["City"])

            print("\nOrders")

            if len(customer["Orders"])==0:
                print("No Orders")

            else:
                for product in customer["Orders"]:

                    print("Product ID :",product["ProductId"])
                    print("Product Name :",product["ProductName"])
                    print("Quantity :",product["Quantity"])
                    print("Price :",product["Price"])
                    print()


def search_customer(customers):

    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:

        if customer["CustomerId"]==customer_id:

            print("Customer ID :",customer["CustomerId"])
            print("Customer Name :",customer["CustomerName"])
            print("City :",customer["City"])

            print("\nOrders")

            if len(customer["Orders"])==0:
                print("No Orders")

            else:

                for product in customer["Orders"]:

                    print("Product ID :",product["ProductId"])
                    print("Product Name :",product["ProductName"])
                    print("Quantity :",product["Quantity"])
                    print("Price :",product["Price"])
                    print()

            return

    print("Customer not found.")


def update_quantity(customers):

    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:

        if customer["CustomerId"]==customer_id:

            product_id=int(input("Enter Product ID:"))

            for product in customer["Orders"]:

                if product["ProductId"]==product_id:

                    qty=int(input("Enter New Quantity:"))

                    product["Quantity"]=qty

                    print("Quantity updated successfully.")
                    return

            print("Product not found.")
            return

    print("Customer not found.")
    
def remove_product(customers):

    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:

        if customer["CustomerId"]==customer_id:

            product_id=int(input("Enter Product ID:"))

            for product in customer["Orders"]:

                if product["ProductId"]==product_id:

                    customer["Orders"].remove(product)

                    print("Product removed successfully.")
                    return

            print("Product not found.")
            return

    print("Customer not found.")


def total_order_value(customers):

    customer_id=int(input("Enter Customer ID:"))

    for customer in customers:

        if customer["CustomerId"]==customer_id:

            total=0

            for product in customer["Orders"]:

                amount=product["Quantity"]*product["Price"]

                print(f'{product["ProductName"]} : {amount}')

                total=total+amount

            print("------------------------")
            print("Total Bill :",total)
            return

    print("Customer not found.")


def max_order_value(customers):

    if len(customers)==0:
        print("No customers found.")
        return

    max_customer=None
    max_total=0

    for customer in customers:

        total=0

        for product in customer["Orders"]:

            total=total+(product["Quantity"]*product["Price"])

        if total>max_total:
            max_total=total
            max_customer=customer

    if max_customer!=None:
        print("Customer Name :",max_customer["CustomerName"])
        print("Total Amount :",max_total)


while True:

    print("\n========== Online Shopping Order Management System ==========")
    print("1. Add New Customer")
    print("2. Add Product Order")
    print("3. View All Customers and Their Orders")
    print("4. Search Customer")
    print("5. Update Product Quantity")
    print("6. Remove Product")
    print("7. Calculate Total Order Value")
    print("8. Display Customer with Maximum Order Value")
    print("9. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        add_customer(customers)

    elif choice==2:
        add_product(customers)

    elif choice==3:
        view_customers(customers)

    elif choice==4:
        search_customer(customers)

    elif choice==5:
        update_quantity(customers)

    elif choice==6:
        remove_product(customers)

    elif choice==7:
        total_order_value(customers)

    elif choice==8:
        max_order_value(customers)

    elif choice==9:
        print("Thank you for using Online Shopping Order Management System.")
        break

    else:
        print("Invalid Choice")