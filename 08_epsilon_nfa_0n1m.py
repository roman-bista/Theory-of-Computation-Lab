# ε-NFA for L = {0^n 1^m | n,m >= 0}

string = input("Enter a binary string: ")

state = "q0"

print("\nProcessing:")

valid = True

for ch in string:

    print(state, "--", ch, "-->", end=" ")

    if state == "q0":

        if ch == '0':
            state = "q0"

        elif ch == '1':
            state = "q1"

        else:
            valid = False

    elif state == "q1":

        if ch == '1':
            state = "q1"

        elif ch == '0':
            valid = False
            break

        else:
            valid = False

    print(state)

if valid:
    print("\nString Accepted")
else:
    print("\nString Rejected")