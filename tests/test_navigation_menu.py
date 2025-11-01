import pytest


def test_check_side_menu_contents_and_functionality(inventory_page, pages):
    inventory_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    inventory_page.open_side_menu()

    assert inventory_page.menu_all_items_button.is_visible()
    assert inventory_page.menu_about_button.is_visible()
    assert inventory_page.menu_logout_button.is_visible()
    assert inventory_page.menu_reset_app_button.is_visible()
    inventory_page.close_side_menu()


@pytest.mark.parametrize(
    "menu_option", [
        "All Items",
        "About",
        "Logout"
    ]
)
def test_side_menu_navigation(inventory_page, pages, menu_option):
    inventory_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    inventory_page.open_side_menu()

    if menu_option == "All Items":
        inventory_page.menu_all_items_button.click()
        inventory_page.current_page_should_be(expected_url=pages["INVENTORY_PAGE"])

    elif menu_option == "About":
        inventory_page.menu_about_button.click()
        inventory_page.current_page_should_be(expected_url=pages["ABOUT_PAGE"])

    elif menu_option == "Logout":
        inventory_page.menu_logout_button.click()
        inventory_page.current_page_should_be(expected_url=pages["LOGIN_PAGE"])
