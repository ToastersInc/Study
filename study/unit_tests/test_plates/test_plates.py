#   Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:


from alt_plates import is_valid

def test_valid_plates():
    """Tests valid license plate formats."""
    assert is_valid("AA2222") == True
    assert is_valid("AA222") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AA22") == True

def test_invalid_plates_length():
    """Tests invalid license plates due to length constraints."""
    assert is_valid("A") == False  # Too short
    assert is_valid("AAAAAAA") == False  # Too long
    assert is_valid("") == False # empty string

def test_invalid_plates_start():
    """Tests invalid license plates that don't start with two letters."""
    assert is_valid("1A2345") == False
    assert is_valid("A12345") == False
    assert is_valid("112345") == False

def test_invalid_plates_format():
    """Tests invalid license plates due to incorrect format."""
    assert is_valid("AA22B2") == False  # Numbers not at the end
    assert is_valid("AA0234") == False  # Number cannot start with 0
    assert is_valid("AA.234") == False  # Punctuation
    assert is_valid("AA 234") == False  # Spaces
    assert is_valid("AA23.4") == False  # punctuation in the middle
    assert is_valid("AA23 4") == False  # space in the middle

def test_invalid_empty_string():
    """Tests invalid input with empty string"""
    assert is_valid("") == False
