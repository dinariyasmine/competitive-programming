# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of entries in the phone book
n = int(input())


phone_book = {}


for _ in range(n):
    name, number = input().split()
    phone_book[name] = number


while True:
    try:
        
        query = input().strip()
        
        
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
