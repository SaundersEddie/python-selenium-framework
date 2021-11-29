# Playing with pytest

def test_firstTest():
    print("First Test")

def test_secondTest():
    print("Second Test")

def test_thirdTest():
    print("Third Test")


def test_FirstDoubleAssert():
    a = 2
    b = 3
    assert a + b == 5, "Learn to add nub"
    assert a + 1 == b, "Learn to add nub"