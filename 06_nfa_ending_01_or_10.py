# NFA: Accepts strings ending with 01 or 10

string = input("Enter a binary string: ")

# Initialize states
q0 = "q0"      # Start State
q1 = "q1"
q2 = "q2"      # Accept State (ends with 01)
q3 = "q3"
q4 = "q4"      # Accept State (ends with 10)

current_states = {q0}

print("\nProcessing:")

for ch in string:

    print(current_states, "--", ch, "-->", end=" ")

    next_states = set()

    for state in current_states:

        if state == q0:

            if ch == '0':
                next_states.add(q0)
                next_states.add(q1)

            elif ch == '1':
                next_states.add(q0)
                next_states.add(q3)

        elif state == q1:

            if ch == '1':
                next_states.add(q2)

        elif state == q3:

            if ch == '0':
                next_states.add(q4)

    current_states = next_states

    print(current_states)

print("\nFinal States:", current_states)

if q2 in current_states or q4 in current_states:
    print("String", string, "is Accepted")
else:
    print("String", string, "is Rejected")