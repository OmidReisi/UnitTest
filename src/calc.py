def add(x, y):
    """ADD Function

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    return x + y


def subtract(x, y):
    """Subtract Function

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    return x - y


def multiply(x, y):
    """Multiply Function

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    return x * y


def divide(x, y):
    """Divide Function

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't divide by zero")
        raise


# this is the wrong way of testing modules.
# divide(10, 0)
