# 🔐 Python Strong Password Validator

This mini-project contains a Python script that validates passwords based on a set of strict rules.  
It reads multiple username/password pairs and prints `"valid"` or `"invalid"` for each.

The solution uses Python’s built-in **`re`** (regular expressions) module.

---

## ✅ Password Rules

A password is valid **only if all** the following conditions are met:

- **Minimum length:** 6 characters  
- **Maximum length:** 12 characters  
- **Lowercase requirement:** at least one `[a-z]`  
- **Uppercase requirement:** at least one `[A-Z]`  
- **Digit requirement:** at least one `[0-9]`  
- **Username exclusion:**  
  - Password must **NOT** contain the username  
  - Check must be **case-insensitive**

---

## 🧠 How the Code Works (`password_validator.py`)

The program has two main components:

---

### ### 1. `is_valid_password(username, password)`

This function validates a single password based on the rules.

#### **Step 1 — Regex Validation (Rules 1–5)**

It uses the following regex:

```python
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$"
Pattern Breakdown

^ and $ — start/end of the string

(?=.*[a-z]) — at least one lowercase letter

(?=.*[A-Z]) — at least one uppercase letter

(?=.*\d) — at least one digit

.{6,12} — length 6 to 12 characters

If the regex check fails → return False.

Step 2 — Username Check (Rule 6)
python
Copy code
if username.lower() in password.lower():
    return False
This ensures the username does not appear anywhere in the password.

The check is case-insensitive.

If all checks pass → return True.

2. main()
Execution steps:

Read an integer n

Loop n times

For each pair:

Read username

Read password

Validate

Store "valid" or "invalid"

Print results line by line

▶️ How to Run
Save the file as:

Copy code
password_validator.py
Run:

bash
Copy code
python password_validator.py
The script will wait for input based on the challenge format.

📥 Example
Input
graphql
Copy code
2
Omid
8omid@A9
sol
123So@So
Output
nginx
Copy code
invalid
valid
yaml
Copy code

---

### ✅ Why this one will render beautifully?

- Proper markdown headings (`#`, `##`, `###`)
- Blank lines between sections  
- Code blocks wrapped in triple backticks  
- Lists use dashes  
- Extra spacing so GitHub doesn't merge paragraphs  

---

If you want, I can also help you add:

✔ project structure  
✔ badges  
✔ a section for the non-regex script  
✔ or turn this into a full mini NLP project README  

Just say the word.






