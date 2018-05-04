def ticket1(age):
    if age < 15:
        print("children")
    elif age < 65:
        print("adults")
    else:
        print("seniors")

def test():
    ticket1(10)
    ticket1(20)
    ticket1(65)

test()
