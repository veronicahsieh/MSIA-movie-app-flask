import sys

sys.path.append('../')
from develop. import

def test_columns():
    data = d.read_data(inputfile,yaml_data) #read data is a function in cloud file
    assert len(data.columns) == 10

#unit test to check that raise exception is actually being raised

def test_ioError():
    with pytest.raises(SystemExit):
        d.read_data(inputfile,yaml_data)

# this test succeeds if the file does not exist
# not ioerror because systemexit is the final action
