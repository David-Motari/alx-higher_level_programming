#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
        function that divides element by element 2 lists.
    """
    
    i = 0
    n_arry = []
    while i < list_length:
        n = 0
        try:
            n = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            i += 1
            n_arry.append(n)

    return n_arry
