# DFA to accept strings that do not contain substring "00"

string = input("Enter a binary string: ")

state = "q0"

print("\nProcessing:")

for ch in string:

    print(state, "--", ch, "-->", end=" ")

    if state == "q0":

        if ch == '0':
            state = "q1"
        elif ch == '1':
            state = "q0"
        else:
            print("\nInvalid Input")
            exit()

    elif state == "q1":

        if ch == '0':
            state = "qd"
        elif ch == '1':
            state = "q0"
        else:
            print("\nInvalid Input")
            exit()

    elif state == "qd":

        state = "qd"

    print(state)

if state == "qd":
    print("\nString Rejected")
else:
    print("\nString Accepted")