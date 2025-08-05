def read_and_modify_file():
    """Reads a file, modifies its content, and writes to a new file with error handling."""
    while True:
        try:
            # Ask user for input filename
            input_filename = input("Enter the filename to read: ")
            
            # Read the file
            with open(input_filename, 'r') as file:
                content = file.read()
            
            # Modify the content (convert to uppercase)
            modified_content = content.upper()
            
            # Ask user for output filename
            output_filename = input("Enter the filename to save the modified content: ")
            
            # Write to the new file
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            
            print(f"Success! Modified content saved to '{output_filename}'.")
            break  # Exit loop if successful
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}'. Try another file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
