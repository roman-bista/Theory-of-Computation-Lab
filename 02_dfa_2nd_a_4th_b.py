# DFA: Accepts strings whose 2nd symbol is 'a' and 4th symbol is 'b'

string = input("Enter a string: ")

# Initialize states
q0 = "q0"
q1 = "q1"
q2 = "q2"
q3 = "q3"
q4 = "q4"      # Accept State
qd = "qd"      # Dead State

state = q0

print("\nProcessing:")

for ch in string:

    print(state, "--", ch, "-->", end=" ")

    if state == q0:

        if ch == 'a' or ch == 'b':
            state = q1

    elif state == q1:

        if ch == 'a':
            state = q2
        else:
            state = qd

    elif state == q2:

        if ch == 'a' or ch == 'b':
            state = q3

    elif state == q3:

        if ch == 'b':
            state = q4
        else:
            state = qd

    elif state == q4:

        if ch == 'a' or ch == 'b':
            state = q4

    elif state == qd:

        state = qd

    print(state)

print("\nFinal State:", state)

if len(string) >= 4 and state == q4:
    print("String", string, "is Accepted")
else:
    print("String", string, "is Rejected")