from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    email = "juriizorn@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "355!Asd66")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    assert main_page.get_current_url().endswith("user61946865/boards")
    assert info[0] == "Юрий"
    assert info[1] == email
