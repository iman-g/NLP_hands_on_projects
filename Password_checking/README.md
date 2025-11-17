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

## 🧠 How the Code Works (`With_regex.py`)

The program has two main components:

---

### 1. `is_valid_password(username, password)`

This function validates a single password based on the rules.

#### **Step 1 — Regex Validation (Rules 1–5)**

It uses the following regex:

```python
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$"
```




#### Pattern Breakdown

- ^ and $ — start/end of the string

- (?=.*[a-z]) — at least one lowercase letter

- (?=.*[A-Z]) — at least one uppercase letter

- (?=.*\d) — at least one digit

- .{6,12} — length 6 to 12 characters

If the regex check fails → return False.


### Step 2 — Username Check (Rule 6)
```python
if username.lower() in password.lower():
    return False
```


- This ensures the username does not appear anywhere in the password.

- The check is case-insensitive.

If all checks pass → return True.



### 2. main()

Execution steps:

1. Read an integer n

2. Loop n times

3. For each pair:

- Read username

- Read password

- Validate

- Store "valid" or "invalid"

4. Print results line by line


## ▶️ How to Run

Save the file as:

```python
With_regex.py
```

Run:
```python
python With_regex.py
```

The script will wait for input based on the challenge format.



## 📥 Example
Input
```python
2
Omid
8omid@A9
sol
123So@So
```

Output
```python
invalid
valid
```

