from main import get_average

def test_average():
    assert get_average([1,2,3]) == 2
    assert get_average([1,2,3,4,5]) == 3
    assert get_average([1,2,3,4,5,6,7]) == 4
