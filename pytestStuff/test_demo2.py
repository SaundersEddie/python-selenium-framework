# Playing with pytest

def test_fourthTest():
    msg ="Fourth Test"
    assert msg == "Fourth Test", "Test failed because strings do not match"

@pytest.mark.tier1
def test_SecondDoubleAssert():
    a = 4
    b = 6
    assert a + b == 10, "Learn to add nub"
    assert a + 2 == b, "Learn to add nub"

@pytest.mark.tier1
def test_sixthTest():
    print("Sixth Test")

