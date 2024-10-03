from sequences import get_next_value


# Using a lib to make auto incrementing values as not possible
# for django to have multiple auto incr - id field
def image_order_next_val():
    return get_next_value("image_order")
