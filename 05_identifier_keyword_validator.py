# Program to validate C identifiers and keywords

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

if word in keywords:
    print("Keyword")

else:

    valid = True

    # First character check
    if not (word[0].isalpha() or word[0] == '_'):
        valid = False

    # Remaining characters check
    for ch in word:

        if not (ch.isalnum() or ch == '_'):
            valid = False

    if valid:
        print("Valid Identifier")
    else:
        print("Invalid Identifier")