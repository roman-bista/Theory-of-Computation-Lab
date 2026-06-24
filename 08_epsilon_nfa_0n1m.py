# ε-NFA for L = {0^n1^m | n,m >= 0}

string = input("Enter a binary string: ")

state = "q0"
valid = True

print("\nProcessing:")

for ch in string:

    old_state = state

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

    print(old_state, "--", ch, "-->", state)

    if not valid:
        break

if valid:
    print("\nFinal State:", state)
    print("String Accepted")
else:
    print("\nString Rejected")