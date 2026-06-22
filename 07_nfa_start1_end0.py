# NFA for strings starting with 1 and ending with 0

string = input("Enter a binary string: ")

print("\nProcessing:")

for ch in string:
    print("Read:", ch)

if len(string) > 0 and string[0] == '1' and string[-1] == '0':
    print("\nString Accepted")
else:
    print("\nString Rejected")