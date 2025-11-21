import unittest
from string_checker import (
    validate_email, 
    validate_phone, 
    validate_URL, 
    validate_date,
    validate_strong_password,
    validate_ipv4
)

class TestValidatorFunctions(unittest.TestCase):

    def test_validate_email(self):
        # Valid cases
        self.assertTrue(validate_email("example.user@domain.com"))
        self.assertTrue(validate_email("user+name@sub.co"))
        # Invalid cases
        self.assertFalse(validate_email("user@domain-with-dash.com")) # Assignment rule: domain alphabets/nums only
        self.assertFalse(validate_email("user@domain")) # No TLD
        self.assertFalse(validate_email("@domain.com")) # No username

    def test_validate_phone(self):
        # Valid cases (Iranian formats)
        self.assertTrue(validate_phone("09123456789"))       # 11 chars
        self.assertTrue(validate_phone("+989123456789"))     # 13 chars
        self.assertTrue(validate_phone("00989123456789"))    # 14 chars
        # Invalid cases
        self.assertFalse(validate_phone("0912345678"))       # Too short
        self.assertFalse(validate_phone("07123456789"))      # Wrong prefix
        self.assertFalse(validate_phone("abc12345678"))      # Letters

    def test_validate_url(self):
        # Valid cases
        self.assertTrue(validate_URL("https://www.example.com"))
        self.assertTrue(validate_URL("http://site.org"))
        self.assertTrue(validate_URL("www.google.com"))      # Protocol optional
        self.assertTrue(validate_URL("example.net"))         # Minimal
        # Invalid cases
        self.assertFalse(validate_URL("ftp://example.com"))  # Only http/s allowed
        self.assertFalse(validate_URL("example.c"))          # TLD too short

    def test_validate_date(self):
        # Valid cases
        self.assertTrue(validate_date("2024-11-17"))
        self.assertTrue(validate_date("1990.05.01"))
        self.assertTrue(validate_date("2099/12/31"))
        # Invalid cases
        self.assertFalse(validate_date("1899-11-17"))        # Year out of range (<1900)
        self.assertFalse(validate_date("2100-01-01"))        # Year out of range (>2099)
        self.assertFalse(validate_date("2022-13-01"))        # Month 13
        self.assertFalse(validate_date("2022-01-32"))        # Day 32
        self.assertFalse(validate_date("2022-05.05"))        # Mixed separators


    def test_validate_strong_password(self):
        # Valid
        self.assertTrue(validate_strong_password("StrongP@ss1"))
        # Invalid
        self.assertFalse(validate_strong_password("weakpass"))       # No numbers/Upper/Symbol
        self.assertFalse(validate_strong_password("NoSymbol123"))    # Missing symbol
        self.assertFalse(validate_strong_password("Sh0rt!"))         # Too short (<8)


    def test_validate_ipv4(self):
        # Valid
        self.assertTrue(validate_ipv4("192.168.1.1"))
        self.assertTrue(validate_ipv4("0.0.0.0"))
        self.assertTrue(validate_ipv4("255.255.255.255"))
        # Invalid
        self.assertFalse(validate_ipv4("256.1.1.1"))         # 256 > 255
        self.assertFalse(validate_ipv4("192.168.1"))         # Missing octet
        self.assertFalse(validate_ipv4("abc.def.ghi.jkl"))   # Not numbers


if __name__ == '__main__':
    unittest.main()