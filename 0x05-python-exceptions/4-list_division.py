#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = len(my_list_1)
    y = len(my_list_2)

    try:
        z = [my_list_1[a]/my_list_2[b] for a in range(x) for b in range(y) if a == b]
        list_length = len(z)

    except ZeroDivisionError:
        print("division by 0")
    except (TypeError):
        print("wrong type")
    except (IndexError):
        print("out of range")

    finally:
        return z
