import pytest_check as ch

def test_check():

    print("Before first check")

    ch.equal(1, 1, "First failed")

    print("After first check")

    ch.equal(1, 1)

    print("After second check")

def test_check2():

    

    ch.equal(1, 1)

  