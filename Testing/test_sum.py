def test_sum():
    assert sum([1,2,3])==6

def test_sum_tup():
    assert sum((1,2,10))==13


if __name__=="__main__":
    test_sum()
    test_sum_tup()
    print("Everything passed")
