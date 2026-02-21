#!/usr/bin/python3
kdef safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while True:
        try:
            if i >= x:
                break
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
        i += 1
    print()
    return count
