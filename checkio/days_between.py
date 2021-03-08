from datetime import date, timedelta

def days_diff(a, b):
    # your code here
    yeara, montha, daya = a
    yearb, monthb, dayb = b
    datea = date(yeara, montha, daya)
    dateb = date(yearb, monthb, dayb)
    return abs((datea-dateb).__getattribute__("days"))

# another way
def days_diff_2(a, b):
    # your code here
    datea = date(*a)
    dateb = date(*b)
    return abs((datea-dateb).__getattribute__("days"))

if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")

    #another way
    print("anotherway")
    print("Example:")
    print(days_diff_2((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff_2((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff_2((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff_2((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")