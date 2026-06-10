import pytest

@pytest.mark.dependency(name="valid")
def test_valproduct(test_setup_and_teardown):

    driver = test_setup_and_teardown

    val_item = read_config.get_config("search term", "val_item")

    driver.find_element(By.NAME, "search").send_keys(val_item, Keys.ENTER)

    assert driver.find_element(
        By.XPATH,
        '//a[text()="HP LP3065"]'
    ).is_displayed()


@pytest.mark.dependency(depends=["valid"], name="invalid")
def test_invalproduct(test_setup_and_teardown):

    driver = test_setup_and_teardown

    inval_item = read_config.get_config("search term", "inVal_item")

    driver.find_element(By.NAME, "search").send_keys(inval_item, Keys.ENTER)

    actual = "There is no product that matches the search criteria."

    expected = driver.find_element(
        By.XPATH,
        '//p[contains(text(),"There is no product")]'
    ).text

    assert actual == expected


@pytest.mark.dependency(depends=["invalid"])
def test_noproduct(test_setup_and_teardown):

    driver = test_setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("", Keys.ENTER)

    actual = "There is no product that matches the search criteria."

    expected = driver.find_element(
        By.XPATH,
        '//p[contains(text(),"There is no product")]'
    ).text

    assert actual == expected