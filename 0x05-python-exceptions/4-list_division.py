#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    y = []
    for a in range(0, list_length):
        try:
            z = my_list_1[a]/my_list_2[a]

        except ZeroDivisionError:
            print("division by 0")
            z = 0
        except (TypeError):
            print("wrong type")
            z = 0
        except (IndexError):
            print("out of range")
            z = 0

        finally:
            y.append(z)
    return y
