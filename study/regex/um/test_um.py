from um import count

def test_count():
    # Test cases based on the logic of the count function
    assert count("hello world") == 0
    assert count("this is a test with um") == 1
    assert count("umbrella") == 1
    assert count("umbilical") == 1
    assert count("humdrum") == 0
    assert count("um") == 1 # The word "um" itself
    assert count("Um, thanks for the album.") == 1 # Case sensitive, counts "Um," and "album."
    assert count("Um, thanks for the album. um...") == 2 # Includes punctuation
    assert count("UM") == 1 # Case sensitive
    assert count("") == 0 # Empty string
    assert count(" um ") == 1 # Leading and trailing spaces
    assert count("um um um") == 3 # Multiple instances as separate words
    assert count("lorem ipsum dolor sit amet") == 0 # "ipsum" contains "um"
