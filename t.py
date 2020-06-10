def printer(function):
    def new_function(*args):
        print(f"Started: {function.__name__}")
        output = function(*args)
        print("Finished")
        return output
    return new_function
# def circle_area(radius):
#     return 3.142 * radius ** 2
#area = printer(circle_area)(2)

@printer
def circle_area(radius):
    return 3.142 * radius ** 2
area = circle_area(2)
print(area)