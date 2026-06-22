 # Python Program to Find Prefixes, Suffixes, and Substrings

# Input string from user
s = input("Enter a string: ")

# Prefixes

print("\nPrefixes:")
print("ε")   # Empty string

for i in range(1, len(s) + 1):
    print(s[:i])

# Suffixes

print("\nSuffixes:")
print("ε")   # Empty string

for i in range(len(s)):
    print(s[i:])


# Substrings

print("\nSubstrings:")

unique_substrings = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substring = s[i:j]

        if substring not in unique_substrings:
            unique_substrings.add(substring)
            print(substring)
