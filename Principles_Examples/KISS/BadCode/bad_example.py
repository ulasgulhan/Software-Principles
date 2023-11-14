def complex_function(x, y, z):
    if x > y and z != 0:
        result = (x + y) / z
    else:
        result = x * y
    return result


output = complex_function(10, 5, 2)
print(output)