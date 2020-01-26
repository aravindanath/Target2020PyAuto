"""
https://docs.python.org/3/library/exceptions.html
"""


def exception():

    try:
        a= 10
        b =0
        c= a/b
        print(c)
    # except ZeroDivisionError:
    #     print("Zero division")
    except :
        print("Zero cant divide")
        # raise  ("This has an exception")
        raise exception("This has an exception")
    else:
        print("Else block is getting executing because no exception")
    finally:
        print("Finally will execute always..")



exception()