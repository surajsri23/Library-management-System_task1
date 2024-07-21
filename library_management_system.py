from datetime import datetime, timedelta

class Item:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} [{self.category}]"

class Library:
    def __init__(self):
        self.items = []
        self.checked_out_items = {}
        self.fines = {}

    def add_item(self, title, author, category):
        self.items.append(Item(title, author, category))
        print(f"Added: {title} by {author} [{category}]")

    def checkout_item(self, title, user, due_date):
        for item in self.items:
            if item.title == title and not item.is_checked_out:
                item.is_checked_out = True
                item.due_date = due_date
                self.checked_out_items[title] = user
                print(f"{title} checked out by {user} until {due_date}")
                return
        print(f"{title} is not available for checkout")

    def return_item(self, title, return_date):
        if title in self.checked_out_items:
            item = next(i for i in self.items if i.title == title)
            user = self.checked_out_items.pop(title)
            item.is_checked_out = False
            overdue_days = (return_date - item.due_date).days if return_date > item.due_date else 0
            fine = overdue_days * 1  # ₹1 fine per day
            if fine > 0:
                self.fines[user] = self.fines.get(user, 0) + fine
                print(f"{title} returned late by {user}. Fine: ₹{fine}")
            else:
                print(f"{title} returned on time by {user}")
        else:
            print(f"{title} was not checked out")

    def search(self, keyword):
        results = [item for item in self.items if keyword.lower() in item.title.lower() or keyword.lower() in item.author.lower() or keyword.lower() in item.category.lower()]
        if results:
            for item in results:
                print(item)
        else:
            print("No items found")

    def display_fines(self):
        if self.fines:
            for user, fine in self.fines.items():
                print(f"{user} owes ₹{fine}")
        else:
            print("No fines")

def main():
    library = Library()
    
    # Predefined books
    library.add_item("Python Programming", "Erric Matthes", "Book")
    library.add_item("National Geographic", "Various", "Magazine")
    library.add_item("Inception", "Christopher Nolan", "DVD")
    library.add_item("The Great Gatsby", "F. Scott Fitzgerald", "Book")
    library.add_item("Time Magazine", "Various", "Magazine")
    library.add_item("Interstellar", "Christopher Nolan", "DVD")
    library.add_item("Gunaho ka Devta", "Dharmveer Bharti", "Novel")
    library.add_item("Mushafir Cafe", "Divya Prakash Duvey", "Novel")

    while True:
        print("\nLibrary Management System")
        print("1. Add Item")
        print("2. Checkout Item")
        print("3. Return Item")
        print("4. Search Items")
        print("5. Display Fines")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            library.add_item(title, author, category)
        
        elif choice == "2":
            title = input("Enter title of the item to checkout: ")
            user = input("Enter user name: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            library.checkout_item(title, user, due_date)
        
        elif choice == "3":
            title = input("Enter title of the item to return: ")
            return_date_str = input("Enter return date (YYYY-MM-DD): ")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
            library.return_item(title, return_date)
        
        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            library.search(keyword)
        
        elif choice == "5":
            library.display_fines()
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
