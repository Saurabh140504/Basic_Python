# Step 1: Ask the user to enter a string
text = input("Enter a string: ")

# Step 2: Loop over each character in the string
for index, char in enumerate(text, start=1):
    # Step 3: Check if the character is a digit
    if char.isdigit():
        print(f"{index}. '{char}' -> Digit")

    # Step 4: Check if the character is an alphabet letter
    elif char.isalpha():
        print(f"{index}. '{char}' -> Alphabet")

    # Step 5: Check if the character is whitespace (space, tab, newline)
    elif char.isspace():
        # show readable name for whitespace
        if char == " ":
            ws_name = "Space"
        elif char == "\t":
            ws_name = "Tab"
        elif char == "\n":
            ws_name = "Newline"
        else:
            ws_name = "Whitespace"
        print(f"{index}. (whitespace) -> {ws_name}")

    # Step 6: Everything else is a symbol (punctuation, special character)
    else:
        print(f"{index}. '{char}' -> Symbol")
