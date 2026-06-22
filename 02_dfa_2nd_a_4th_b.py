# DFA: 2nd symbol = a and 4th symbol = b

string = input("Enter a string: ")

state = "q0"

print("\nProcessing:")

for ch in string:

    print(state, "--", ch, "-->", end=" ")

    if state == "q0":

        if ch in ['a', 'b']:
            state = "q1"

    elif state == "q1":

        if ch == 'a':
            state = "q2"
        else:
            state = "qd"

    elif state == "q2":

        if ch in ['a', 'b']:
            state = "q3"

    elif state == "q3":

        if ch == 'b':
            state = "q4"
        else:
            state = "qd"

    elif state == "q4":

        if ch in ['a', 'b']:
            state = "q4"

    elif state == "qd":

        state = "qd"

    print(state)

if len(string) >= 4 and state == "q4":
    print("\nString Accepted")
else:
    print("\nString Rejected")