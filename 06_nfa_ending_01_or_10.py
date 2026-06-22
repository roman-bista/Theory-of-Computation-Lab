# NFA for strings ending with 01 or 10

string = input("Enter a binary string: ")

print("\nProcessing:")

for ch in string:
    print("Read:", ch)

if len(string) >= 2 and (
    string[-2:] == "01" or
    string[-2:] == "10"
):
    print("\nString Accepted")
else:
    print("\nString Rejected")