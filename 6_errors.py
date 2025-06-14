def div42by (divide_by):
    try:
        return (42 / divide_by)
    except ZeroDivisionError: #we can omit error specification, will catch all errors
        print("this is an error")
    finally:
        print("yoohoo")
print(div42by(0))