# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of entries in the phone book
n = int(input())

# Create an empty phone book dictionary
phone_book = {}

# populate the dictionary
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number


while True:
    try:
        # Read query
        query = input().strip()
        
        # Check if exists in the dictionary
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
