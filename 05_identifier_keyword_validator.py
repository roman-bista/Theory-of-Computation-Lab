# Program to Validate C Identifiers and Keywords

word = input("Enter an identifier or keyword: ")

keywords = [
    "auto", "break", "case", "char", "const",
    "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for",
    "goto", "if", "int", "long", "register",
    "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef",
    "union", "unsigned", "void", "volatile",
    "while"
]

print("\nProcessing:")

valid = True

# Check if it is a keyword
if word in keywords:
    print(word, "is found in the keyword list.")
    print("\nResult:")
    print(word, "is a C Keyword")

else:

    # Check first character
    print("Checking first character:", word[0])

    if not (word[0].isalpha() or word[0] == "_"):
        valid = False

    # Check remaining characters
    for ch in word:

        print("Checking:", ch)

        if not (ch.isalnum() or ch == "_"):
            valid = False

    print("\nResult:")

    if valid:
        print(word, "is a Valid Identifier")
    else:
        print(word, "is an Invalid Identifier")