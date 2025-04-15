from twttr import strip_vowel

def test_strip_vowel():
    assert strip_vowel("twitter") == "twttr"


if __name__ == "__main__":
    main()
