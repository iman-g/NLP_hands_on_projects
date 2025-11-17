🔐 Python Strong Password Validator

This mini-project contains a Python script that validates passwords based on a set of strict rules. It was originally created for an NLP course assignment, but it’s also a good hands-on exercise for regex, input parsing, and basic validation logic.

The program reads multiple username/password pairs and prints "valid" or "invalid" for each.

The solution uses Python’s built-in re (regular expressions) module to perform fast and efficient validation.

✅ Password Rules

A password is considered valid only if it satisfies all the rules below:

Minimum length: 6 characters

Maximum length: 12 characters

Lowercase requirement: At least one [a-z]

Uppercase requirement: At least one [A-Z]

Digit requirement: At least one [0-9]

Username exclusion:

The password must NOT contain the username

Comparison is case-insensitive

🧠 How the Code Works (password_validator.py)

The script is organized into two main components.

1. is_valid_password(username, password)

This function receives a username and password, then returns True or False.

Step 1 — Regex Validation (Rules 1–5)

The function uses the following single regex pattern:

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$"

Pattern Breakdown

^ and $ → match the start and end of the string

(?=.*[a-z]) → at least one lowercase letter

(?=.*[A-Z]) → at least one uppercase letter

(?=.*\d) → at least one digit

.{6,12} → overall length between 6 and 12 characters

If the password fails this pattern match, the function returns False immediately.

Step 2 — Username Check (Rule 6)

After the regex passes, the validator ensures the password doesn't contain the username:

if username.lower() in password.lower():
    return False


This guarantees a case-insensitive match.
If the username appears anywhere in the password, it is invalid.

If all checks pass → the function returns True.

2. main()

This is the execution workflow:

Reads an integer n (number of credential pairs)

Loops n times

For each loop:

Reads a username (line 1)

Reads a password (line 2)

Validates using is_valid_password()

Stores "valid" or "invalid"

After processing all cases, prints each result on a new line

▶️ How to Run

Save the script as:

password_validator.py


Run from your terminal:

python password_validator.py


The script will wait for input.

📥 Example
Input
2
Omid
8omid@A9
sol
123So@So

Output
invalid
valid