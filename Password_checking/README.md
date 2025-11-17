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
