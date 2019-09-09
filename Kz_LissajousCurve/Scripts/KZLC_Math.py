import math

# 2pi
PI2 = math.pi * 2.0


# Function like the Numpy.linspace()
def linspace(min, max, count):
    values = list()

    if count == 0:
        return values

    values.append(float(min))
    if count > 1:
        step = float((max - min) / (count - 1))

    for i in range(count - 2):
        values.append(float(min + step * (i + 1)))

    if count > 1:
        values.append(float(max))

    return values
