import pytest


def test_item_prices_match_total(checkout_page, pages):
    checkout_page.navigate_to_page(
        url=pages["CHECKOUT_PAGE2"], title="Checkout: Overview"
    )

    subtotal = checkout_page.validate_item_prices_match_subtotal(
        sum_of_prices=checkout_page.sum_of_all_item_prices()
    )
    checkout_page.validate_subtotal_plus_tax_equal_total(subtotal=subtotal)


@pytest.mark.parametrize("next_step", ["cancel", "finalize"])
def test_order_can_be_finalized_or_canceled(checkout_page, pages, next_step):
    checkout_page.navigate_to_page(
        url=pages["CHECKOUT_PAGE2"], title="Checkout: Overview"
    )

    if next_step == "cancel":
        checkout_page.cancel_checkout()
        checkout_page.current_page_should_be(
            expected_url=pages["INVENTORY_PAGE"], title="Products"
        )

    elif next_step == "finalize":
        checkout_page.finalize_order()
        checkout_page.current_page_should_be(
            expected_url=pages["CHECKOUT_PAGE3"], title="Checkout: Complete!"
        )
