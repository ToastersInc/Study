# Assuming your original file is named numb3rs.py
from numb3rs import validate

# Pytest test functions typically start with 'test_'

def test_valid_ips():
    """Tests for valid IPv4 addresses."""
    assert validate("192.168.1.1") # Standard private IP
    assert validate("10.0.0.255")  # Edge case within a private range
    assert validate("0.0.0.0")     # The zero address
    assert validate("255.255.255.255") # The broadcast address
    assert validate("172.16.200.100") # Another standard private IP
    assert validate("1.1.1.1")     # Simple public IP

def test_invalid_ips():
    """Tests for invalid IPv4 addresses."""
    # Test cases with numbers out of range (0-255)
    assert not validate("256.1.1.1") # Number > 255
    assert not validate("1.256.1.1") # Number > 255
    assert not validate("1.1.256.1") # Number > 255
    assert not validate("1.1.1.256") # Number > 255
    assert not validate("-1.1.1.1")  # Negative number
    assert not validate("1.-1.1.1")  # Negative number

    # Test cases with incorrect number of octets
    assert not validate("192.168.1")      # Less than 4 octets
    assert not validate("192.168.1.1.1")  # More than 4 octets

    # Test cases with incorrect format (non-numeric parts, extra dots, etc.)
    assert not validate("abc.def.ghi.jkl") # Non-numeric input
    assert not validate("192.168.1..1")   # Consecutive dots
    assert not validate(".192.168.1.1")   # Starting with a dot
    assert not validate("192.168.1.1.")   # Ending with a dot
    assert not validate(" 192.168.1.1")   # Leading space
    assert not validate("192.168.1.1 ")   # Trailing space
    assert not validate("192.168.1.1a")   # Trailing characters
    assert not validate("a192.168.1.1")   # Leading characters

    # Test cases with leading zeros on non-zero numbers (your regex handles this)
    assert not validate("192.168.01.1") # Leading zero on non-zero number
    assert not validate("192.168.1.01") # Leading zero on non-zero number
