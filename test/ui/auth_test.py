import allure
import pytest
import time
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage

# @pytest.mark.skip
def test_auth(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")
    user_name = test_data.get("user_name")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step(f"Проверить что URL + {current_url} + заканчивается на user61946865/boards"):
        assert current_url.endswith("user61946865/boards")
    with allure.step("Проверить данные пользователя"):
        with allure.step(f"Имя пользователя должно быть {user_name}"):
            assert info[0] == user_name
        with allure.step(f"Почта пользователя должна быть {email}"):
            assert info[1] == email
