# NFA for strings starting with 1 and ending with 0

string = input("Enter a binary string: ")

print("\nProcessing:")

for i in range(len(string)):
    print("Read:", string[i])

if len(string) > 0:

    print("\nFirst Symbol =", string[0])
    print("Last Symbol =", string[-1])

    if string[0] == '1' and string[-1] == '0':
        print("String Accepted")
    else:
        print("String Rejected")

else:
    print("String Rejected")