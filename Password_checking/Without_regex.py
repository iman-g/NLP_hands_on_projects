def is_valid_password(username, password):
    """
    This function checks the password based on the specified rules and does not use regular expressions (regex).
    """
    
    # Rule 1: Minimum length 6
    # Rule 2: Maximum length 12
    if not (6 <= len(password) <= 12):
        return False

    # Variables to check for the existence of character types
    has_lower = False
    has_upper = False
    has_digit = False

    # Iterate through all characters in the password
    for char in password:
        # Rule 3: At least 1 letter between [a-z]
        if char.islower():
            has_lower = True
        # Rule 4: At least 1 letter between [A-Z]
        elif char.isupper():
            has_upper = True
        # Rule 5: At least 1 number between [0-9]
        elif char.isdigit():
            has_digit = True

    # Check if all rules 3, 4, and 5 are met
    if not (has_lower and has_upper and has_digit):
        return False

    # Rule 6: Should not contain the username (case-insensitive)
    # Convert both strings to lowercase for case-insensitive comparison
    if username.lower() in password.lower():
        return False

    # If the password passes all checks
    return True

def main():
    """
    Main function to read inputs and print outputs.
    """
    try:
        # Read n (number of username and password pairs)
        n = int(input())

        # A list to store the results
        results = []
        
        # Loop to read n pairs of inputs
        for _ in range(n):
            # Read the username
            username = input()
            # Read the password
            password = input()
            
            # Validate the password and add the result to the list
            if is_valid_password(username, password):
                results.append("valid")
            else:
                results.append("invalid")
                
        # Print all results on separate lines
        for result in results:
            print(result)

    except ValueError:
        # Handle the error that might occur when converting n to an integer
        print("Invalid input for n. Please enter an integer.")
    except EOFError:
        # Handle end-of-file for empty input
        pass

# Run the main function of the program
if __name__ == "__main__":
    main()