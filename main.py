def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            print("✅ File read successfully.")
            
            # Example modification: convert to uppercase
            modified_content = content.upper()

            new_filename = f"modified_{filename}"
            with open(new_filename, 'w') as outfile:
                outfile.write(modified_content)
                print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read or write the file '{filename}'.")

# Run the function
read_and_write_file()
