import pytest

# function
def f(x):
    return x+1

#test; write each test as a function
def test_answer():
    assert f(3) == 5

# if this works correctly, script will say that it ran 1 test and it worked correctly
# after creating the testfile, go to command line and run pytest

def read_file(filename):
    f = open(filename, 'r')

# calling a function that is supposed to open the file, and checking that the exception is being raised
def test_ioerror():
    with pytest.raises(IOError):
        read_file('asdf')
