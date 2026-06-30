# ε-NFA: Accepts strings of the language L = {0^n1^m | n,m >= 0}

string = input("Enter a binary string: ")

# Initialize states
q0 = "q0"      # Reading 0's
q1 = "q1"      # Reading 1's

# ε-transition from q0 to q1
current_states = {q0, q1}

print("\nProcessing:")

for ch in string:

    print(current_states, "--", ch, "-->", end=" ")

    next_states = set()

    for state in current_states:

        if state == q0:

            if ch == '0':
                next_states.add(q0)
                next_states.add(q1)     # ε-transition

        elif state == q1:

            if ch == '1':
                next_states.add(q1)

    current_states = next_states

    print(current_states)

print("\nFinal States:", current_states)

if len(current_states) > 0:
    print("String", string, "is Accepted")
else:
    print("String", string, "is Rejected")