# DFA: Accepts strings that do not contain substring "00"

string = input("Enter a binary string: ")

# Initialize states
q0 = "q0"      # Start State
q1 = "q1"      # Previous symbol is 0
q2 = "q2"      # Dead State (00 found)

state = q0

print("\nProcessing:")

for ch in string:

    print(state, "--", ch, "-->", end=" ")

    if state == q0:

        if ch == '0':
            state = q1
        elif ch == '1':
            state = q0

    elif state == q1:

        if ch == '0':
            state = q2
        elif ch == '1':
            state = q0

    elif state == q2:

        state = q2

    print(state)

print("\nFinal State:", state)

if state != q2:
    print("String", string, "is Accepted")
else:
    print("String", string, "is Rejected")