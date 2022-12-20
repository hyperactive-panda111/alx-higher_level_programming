afe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return (result)
