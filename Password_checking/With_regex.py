import re

def is_valid_password(username, password):
    """
    This function checks the password based on the specified rules using regular expressions (regex).
    """
    
    
    # Compile the regex pattern
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$"
    
    # re.match() checks for a match only at the beginning of the string.
    # Since we used ^ and $, it's perfect for validating the whole string.
    if not re.match(pattern, password):
        return False

    # Rule 6: Should not contain the username (case-insensitive)
    # This rule is still simpler and more readable to check with standard
    # string methods than with a complex regex.
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