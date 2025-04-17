# then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

from bank_alt import value

def test_value_hello():
    assert value("Hello") == 0


def test_value_h():
    assert value("h") == 20


def test_value_else():
    assert value("cat") == 100


# AI written test...
#   from bank_alt import value  # Assuming your file is named bank_alt.py

#   def test_hello_greeting():
#       assert value("hello") == 0
#       assert value("hello world") == 0
#       assert value("Hello") == 0
#       assert value("Hello World") == 0

#   def test_h_greeting():
#       assert value("hi") == 20
#       assert value("Hi") == 20
#       assert value("hey") == 20
#       assert value("Hey there") == 20
#       assert value("h") == 20
#       assert value("H") == 20

#   def test_other_greeting():
#       assert value("good morning") == 100
#       assert value("Good Morning") == 100
#       assert value("what's up") == 100
#       assert value("What is up") == 100
#       assert value("yo") == 100
#       assert value("Yo!") == 100
#       assert value("any") == 100
#       assert value("") == 100  # empty string

#   def test_edge_cases():
#       #  These might be important depending on how strict you want to be
#       assert value("hello!") == 0
#       assert value("Hello?") == 0
#       assert value("h!") == 20
#       assert value("H.") == 20
