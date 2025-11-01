import pytest


def test_items_can_be_removed_from_shopping_cart(cart_page, pages):
    cart_page.navigate_to_page(url=pages["CART_PAGE"], title="Your Cart")

    initial_item_count = cart_page.get_cart_item_count()
    for n in range(initial_item_count):
        cart_page.remove_first_item_from_cart()
        assert cart_page.get_cart_item_count() == initial_item_count - (n + 1)


@pytest.mark.parametrize("next_step", ["return", "proceed"])
def test_cart_can_be_exited_and_proceeded_from(cart_page, pages, next_step):
    cart_page.navigate_to_page(url=pages["CART_PAGE"], title="Your Cart")

    if next_step == "return":
        cart_page.return_to_shop_page()
        cart_page.current_page_should_be(expected_url=pages["INVENTORY_PAGE"])

    elif next_step == "proceed":
        cart_page.proceed_to_checkout_page()
        cart_page.current_page_should_be(expected_url=pages["CHECKOUT_PAGE1"])
