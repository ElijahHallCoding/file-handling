# Task 1: Directory Inspector 

import os

def list_directory_contents(path):
    try:
        # Get a list of everything in the given path
        items = os.listdir(path)
        print(f"Contents of '{path}':")
        
        # Loop through the list and print each item
        for item in items:
            print(item)
    
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Prompt User for the directory path
    directory_path = input("Enter the directory path you want to inspect: ")
    
    # Call the function to list the contents of the directory
    list_directory_contents(directory_path)