import re

def validate_email(email: str) -> bool:
    """
    Validates email based on strict assignment rules:
    1. Username: letters, numbers, ., _, +, -
    2. Separator: @
    3. Domain: ONLY letters and numbers (no hyphens allowed by assignment)
    4. TLD: letters only, min length 2
    """

    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(pattern, email))



def validate_phone(phone: str) -> bool:
    """
    Validates phone based on Iranian formats:
    1. 09 + 9 digits (11 chars)
    2. +989 + 9 digits (13 chars)
    3. 00989 + 9 digits (14 chars)
    """

    pattern = r'^(09|\+989|00989)\d{9}$'
    
    return bool(re.match(pattern, phone))



def validate_URL(url: str) -> bool:
    """
    Validates URL:
    1. Protocol (optional): http:// or https://
    2. Prefix (optional): www.
    3. Domain: letters, numbers, ., -
    4. TLD: letters only, min length 2
    """

    pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(pattern, url))



def validate_date(date: str) -> bool:
    """
    Validates date:
    1. Formats: YYYY.MM.DD, YYYY-MM-DD, YYYY/MM/DD
    2. Year: 1900-2099
    3. Month: 01-12
    4. Day: 01-31
    """

    pattern = r'^(19\d{2}|20\d{2})([-./])(0[1-9]|1[0-2])\2(0[1-9]|[12]\d|3[01])$'
    
    return bool(re.match(pattern, date))



def validate_strong_password(password: str) -> bool:
    """
    Validates that a password is 'strong':
    1. At least 8 characters long.
    2. Contains at least one uppercase letter.
    3. Contains at least one lowercase letter.
    4. Contains at least one digit.
    5. Contains at least one special character (!@#$%^&*).
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
    return bool(re.match(pattern, password))


def validate_ipv4(ip: str) -> bool:
    """
    Validates a standard IPv4 address (e.g., 192.168.1.1).
    Must consist of 4 groups of numbers (0-255) separated by dots.
    """

    part = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    pattern = f'^{part}\.{part}\.{part}\.{part}$'
    
    return bool(re.match(pattern, ip))