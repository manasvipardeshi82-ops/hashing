# Hash Table using Linear Probing

SIZE = 10
table = [None] * SIZE

# Hash Function - Division Method
def hash_function(key):
    return key % SIZE


# Insert
def insert(key):
    index = hash_function(key)
    start = index

    while table[index] is not None and table[index] != "DELETED":
        index = (index + 1) % SIZE

        if index == start:
            print("Hash table is full")
            return

    table[index] = key
    print("Key inserted at index", index)


# Search
def search(key):
    index = hash_function(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            print("Key found at index", index)
            return

        index = (index + 1) % SIZE

        if index == start:
            break

    print("Key not found")


# Delete
def delete(key):
    index = hash_function(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            table[index] = "DELETED"
            print("Key deleted")
            return

        index = (index + 1) % SIZE

        if index == start:
            break

    print("Key not found")


# Display
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", table[i])


# Menu
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
