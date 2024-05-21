import json
import difflib

# Step 1: Load the JSON data into a Python dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary

# Step 2: Create a function to return the definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Handle case insensitivity
    if word in dictionary:
        return dictionary[word]
    else:
        # Step 3: Suggest the closest matching word for misspellings
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if suggestions:
            return f"Did you mean '{suggestions[0]}'? The definition is: {dictionary[suggestions[0]]}"
        else:
            return "The word is not in the dictionary."

# Main function to interact with the user
def main():
    dictionary = load_dictionary('dictionary.json')
    while True:
        word = input("Enter a word to get its definition (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
