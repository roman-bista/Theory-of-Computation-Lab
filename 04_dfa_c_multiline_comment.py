# DFA for multiline comments in C

comment = input("Enter a comment: ")

state = "q0"

print("\nProcessing:")

for ch in comment:

    old_state = state

    if state == "q0":

        if ch == '/':
            state = "q1"

    elif state == "q1":

        if ch == '*':
            state = "q2"

    elif state == "q2":

        if ch == '*':
            state = "q3"
        else:
            state = "q2"

    elif state == "q3":

        if ch == '/':
            state = "q4"
        elif ch == '*':
            state = "q3"
        else:
            state = "q2"

    print(old_state, "--", ch, "-->", state)

if state == "q4":
    print("\nComment Accepted")
else:
    print("\nComment Rejected")