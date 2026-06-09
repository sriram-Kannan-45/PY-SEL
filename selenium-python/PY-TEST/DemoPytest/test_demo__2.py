import pytest

@pytest.mark.add
def test_sample_5():

    assert 1+1 != 3


@pytest.mark.add
def test_sample_6():

    assert 2+1 != 4


@pytest.mark.skip(reason= "mo reason")
def test_assert_7():

    assert 1+1 == 2

@pytest.mark.smoke
def test_compare_3():

    x = 1
    y = 3

    assert x != y

@pytest.mark.xfail

def test_compare_4():

    x = 40

    y=40

    assert x!=y

