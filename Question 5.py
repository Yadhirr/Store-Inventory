import os
from collections import defaultdict

FILENAME = 'inventory.txt'

def load_inventory():
    
    # Load inventory from file

    if not os.path.exists(FILENAME):
        # Sample data
        sample_data = [
            {'id': 1, 'name': 'Apple', 'category': 'Fruit', 'quantity': 10, 'price': 50.0},
            {'id': 2, 'name': 'Banana', 'category': 'Fruit', 'quantity': 20, 'price': 100.0},
            {'id': 3, 'name': 'Shirt', 'category': 'Clothing', 'quantity': 5, 'price': 500.0},
            {'id': 4, 'name': 'Pants', 'category': 'Clothing', 'quantity': 3, 'price': 600.0},
            {'id': 5, 'name': 'Orange', 'category': 'Fruit', 'quantity': 15, 'price': 75.0},
            {'id': 6, 'name': 'Bread', 'category': 'Bakery', 'quantity': 100, 'price': 15.0},
            {'id': 7, 'name': 'Milk', 'category': 'Dairy', 'quantity': 50, 'price': 30.0},
            {'id': 8, 'name': 'Eggs', 'category': 'Dairy', 'quantity': 200, 'price': 100.0},
            {'id': 9, 'name': 'Chicken', 'category': 'Meat', 'quantity': 25, 'price': 150.0},
            {'id': 10, 'name': 'Beef', 'category': 'Meat', 'quantity': 15, 'price': 300.0},
        ]
        save_inventory(sample_data)
        print("Inventory file created with sample data.")
        return sample_data
    else:
        inventory = []
        try:
            with open(FILENAME, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        product = {
                            'id': int(parts[0]),
                            'name': parts[1].strip(),
                            'category': parts[2].strip(),
                            'quantity': int(parts[3]),
                            'price': float(parts[4])
                        }
                        inventory.append(product)
        except Exception as e:
            print(f"Error loading inventory: {e}")
        return inventory

def save_inventory(inventory):
    
    # Save inventory to file.
    
    try:
        with open(FILENAME, 'w') as file:
            for product in inventory:
                file.write(f"{product['id']},{product['name']},{product['category']},{product['quantity']},{product['price']}\n")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def print_product(product):
    
    # Print a single product's details.
    
    print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Quantity: {product['quantity']}, Price: {product['price']:.2f}")

def add_product(inventory):
    
    # Add a new product.
    
    try:
        product_id = int(input("Enter product ID: "))
        if any(p['id'] == product_id for p in inventory):
            print("Product ID already exists. Please choose a unique ID.")
            return
        name = input("Enter product name: ").strip()
        category = input("Enter product category: ").strip()
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        if quantity < 0 or price < 0:
            print("Quantity and price must be non-negative.")
            return
        inventory.append({'id': product_id, 'name': name, 'category': category, 'quantity': quantity, 'price': price})
        save_inventory(inventory)
        print("Product added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")

def update_product(inventory):
    
    # Update an existing product.
    
    try:
        product_id = int(input("Enter product ID to update: "))
        for product in inventory:
            if product['id'] == product_id:
                print("Current details:")
                print_product(product)
                field = input("Enter field to update (name/category/quantity/price): ").strip().lower()
                if field == 'name':
                    product['name'] = input("Enter new name: ").strip()
                elif field == 'category':
                    product['category'] = input("Enter new category: ").strip()
                elif field == 'quantity':
                    new_quantity = int(input("Enter new quantity: "))
                    if new_quantity < 0:
                        print("Quantity must be non-negative.")
                        return
                    product['quantity'] = new_quantity
                elif field == 'price':
                    new_price = float(input("Enter new price: "))
                    if new_price < 0:
                        print("Price must be non-negative.")
                        return
                    product['price'] = new_price
                else:
                    print("Invalid field.")
                    return
                save_inventory(inventory)
                print("Product updated successfully.")
                return
        print("Product ID not found.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")

def delete_product(inventory):
    
    # Delete a product.
    
    try:
        product_id = int(input("Enter product ID to delete: "))
        for i, product in enumerate(inventory):
            if product['id'] == product_id:
                del inventory[i]
                save_inventory(inventory)
                print("Product deleted successfully.")
                return
        print("Product ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def sort_products_by_price(inventory):
    
    # Sort and display products by price.
    
    if not inventory:
        print("No products in inventory.")
        return
    sorted_inventory = sorted(inventory, key=lambda p: p['price'])
    print("Products sorted by price:")
    for product in sorted_inventory:
        print_product(product)

def filter_products_by_category(inventory):
    
    # Filter and display products by category.
    
    category = input("Enter category to filter: ").strip()
    filtered = [p for p in inventory if p['category'].lower() == category.lower()]
    if not filtered:
        print("No products found in this category.")
        return
    print(f"Products in category '{category}':")
    for product in filtered:
        print_product(product)

def generate_inventory_summary(inventory):
    
    # Inventory summary report.
    
    if not inventory:
        print("No products in inventory.")
        return
    print("Inventory Summary Report:")
    for product in inventory:
        print_product(product)

def generate_category_summary(inventory):
    
    # Category summary report.
    
    if not inventory:
        print("No products in inventory.")
        return
    category_summary = defaultdict(lambda: {'count': 0, 'total_value': 0.0})
    for product in inventory:
        cat = product['category']
        category_summary[cat]['count'] += 1
        category_summary[cat]['total_value'] += product['quantity'] * product['price']
    
    print("Category Summary Report:")
    for cat, data in category_summary.items():
        print(f"Category: {cat}, Number of Products: {data['count']}, Total Value: {data['total_value']:.2f}")

def display_menu():
    
    # Display the console menu.
    
    print("\nInventory Management System")
    print("1. Add a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Sort products by price")
    print("5. Filter products by category")
    print("6. Generate inventory summary report")
    print("7. Generate category summary report")
    print("8. Exit")

def main():
    inventory = load_inventory()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-8): "))
            if choice == 1:
                add_product(inventory)
            elif choice == 2:
                update_product(inventory)
            elif choice == 3:
                delete_product(inventory)
            elif choice == 4:
                sort_products_by_price(inventory)
            elif choice == 5:
                filter_products_by_category(inventory)
            elif choice == 6:
                generate_inventory_summary(inventory)
            elif choice == 7:
                generate_category_summary(inventory)
            elif choice == 8:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()