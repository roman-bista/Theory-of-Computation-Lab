# NFA for strings ending with 01 or 10

string = input("Enter a binary string: ")

print("\nProcessing:")

for i in range(len(string)):
    print("Read:", string[i])

if len(string) >= 2:
    last_two = string[-2:]

    print("\nLast two symbols =", last_two)

    if last_two == "01" or last_two == "10":
        print("String Accepted")
    else:
        print("String Rejected")
else:
    print("String Rejected")