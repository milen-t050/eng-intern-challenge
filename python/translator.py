import sys

# Dictionaries
braille_to_english_main = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",   # space
    ".....O": "capital",  # Indicates the next letter is capital
    ".O.OOO": "number",   # Indicates numbers follow
    ".O...O": "decimal"  # Indicates decimal follows
}

braille_to_number = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

braille_to_punctuation = {
    "..O.OO": ".",
    "..O...": ",",
    "..OO.O": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "..O..O": "-",
    "..O.O.": "/",
    ".O..OO": "(",
    ".O.OO.": ")",
    ".OO..O": "<",
    "O..OO." : ">",
    " ": "......",  # space
}


english_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..O.OO",
    ",": "..O...",
    "?": "..OO.O",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "..O..O",
    "/": "..O.O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": ".O..OO",
    ")": ".O.OO.",
    " ": "......",  # space
    "capital": ".....O",  # Indicates the next letter is capital
    "number": ".O.OOO",  # Indicates numbers follow
    "decimal": ".O...O"  # Indicates decimal follows
}


def Braille_to_English(input):
    output = ""
    i = 0
    capatlize = False
    number = False
    decimal = False

    while i < len(input):
        # Grab current 6 braille characters
        current_set = input[i:i+6]

        # Convert them
        character = braille_to_english_main.get(current_set, "")

        # Check if next character needs to be capitalized
        if character == "capital":
            capatlize = True
        # Check if next character is a number
        elif character == "number":
            number = True
        # Check if next character is a decimal
        elif character == "decimal":
            decimal = True
        else:
            # Add character based on if it needs to be capitalized or not
            if capatlize:
                output += character.upper()
                capatlize = False  # Reset capitalize flag
            # If it's a space, reset the number flag (end of number sequence)
            elif character == " ":
                number = False
                output += character
            elif number:
                # If it's a number, use the number mapping
                output += braille_to_number.get(current_set, "")
            elif decimal:
                # If it's a decimal, use the punctuation mapping
                output += braille_to_punctuation.get(current_set, "")
            else:
                output += character

            

        # Start again with the next 6 characters
        i += 6

    return output

        

def English_to_Braille(input):
    
    output = ""
    number = False
    
    i = 0
    while i < len(input):
        character = input[i]
        
        # Handle uppercase letters
        if character.isupper():
            output += english_to_braille["capital"]
            output += english_to_braille[character.lower()]
        
        # Handle numeric characters
        elif character.isnumeric():
            if not number:
                output += english_to_braille["number"]
                number = True
            output += english_to_braille[character]
        
        # Handle spaces explicitly
        elif character == " ":
            output += english_to_braille[character]
            number = False
            
        # Handle punctuation and other non-alphabetic characters
        elif not character.isalpha() and character != " ":
            output += english_to_braille["decimal"]
            output += english_to_braille[character]
    
        # Handle lowercase letters
        else:
            output += english_to_braille[character]
        
        i += 1
    
    return output
        

def Start(input):
    # Check if input is Braille or English
    if len(input) == input.count("O") + input.count("."):
        return Braille_to_English(input)
    else:
        return English_to_Braille(input)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])  # Join all arguments into one string
        result = Start(input_string)
        print(result)  # Ensure the result is printed to the console
    else:
        print("No input provided.")
