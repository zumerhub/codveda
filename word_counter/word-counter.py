"""In this function a file is opened and read, and the number of words in the file is counted. 
The function handles file not found errors and other exceptions gracefully, returning 0 in case of an error.
The function is called in the main block, where the user is prompted to enter the file path.
The word count is printed to the console.
The function uses a try-except block to handle potential errors, such as file not found or other exceptions.
The function reads the content of the file, splits it into words, and counts the number of words.
The function returns the word count, which is printed in the main block.

TO test the fuction promt the user to enter the file path. example.txt
and the user is prompted to enter the file path.
"""

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            # print(f"Word count: {word_count}")
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    updated_word_count = count_words(file_path) # Call the function to count words in a file name example.txt
    print(f"File contains {updated_word_count} words.")