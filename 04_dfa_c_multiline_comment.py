# DFA: Accepts multiline comments of a C program

comment = input("Enter a comment: ")

# Initialize states
q0 = "q0"      # Start State
q1 = "q1"      # '/' detected
q2 = "q2"      # Inside comment
q3 = "q3"      # '*' detected
q4 = "q4"      # Accept State

state = q0

print("\nProcessing:")

for ch in comment:

    print(state, "--", ch, "-->", end=" ")

    if state == q0:

        if ch == '/':
            state = q1

    elif state == q1:

        if ch == '*':
            state = q2

    elif state == q2:

        if ch == '*':
            state = q3
        else:
            state = q2

    elif state == q3:

        if ch == '/':
            state = q4
        elif ch == '*':
            state = q3
        else:
            state = q2

    elif state == q4:

        state = q4

    print(state)

print("\nFinal State:", state)

if state == q4:
    print("Comment", comment, "is Accepted")
else:
    print("Comment", comment, "is Rejected")


    # /*Hello*/