import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
import math


def load_function_values(filepath):
    with open(filepath) as file:
        function_values = file.read().split("\n")
        function_arr = np.array([combination.split(";") for combination in function_values]).astype(float)

        # return x and y values
        return function_arr[:, 0], function_arr[:, 1]


def plot_function(x_values, y_values):
    # plot points
    plt.plot(x_values, y_values)
    # plot connected function
    plt.plot(x_values, y_values, 'o', color='black')
    plt.show()


def find_y_for_x(x_values, y_values):
    # prints Y values till string is inserted
    while True:
        x_input, correctly_parsed = try_parse_int(input("Insert X value: "))
        if correctly_parsed:
            if x_input in x_values:
                x_index = list(x_values).index(float(x_input))
                print(y_values[x_index])
            else:
                # get the distances to all values
                distances = [distance - x_input for distance in x_values]
                # the distance of the next smaller one is subtracted from the given one (to get actual value, not the distance)
                next_smaller = x_input - abs(max([n for n in distances if n < 0]))
                # the distance of the next bigger one is added to the given one (to get actual value, not the distance)
                next_bigger = abs(min([n for n in distances if n > 0])) + x_input

                index_smaller = list(x_values).index(float(next_smaller))
                index_bigger = list(x_values).index(float(next_bigger))

                y_of_next_smaller = y_values[index_smaller]
                y_of_next_bigger = y_values[index_bigger]

                # gegenkathete
                a = y_of_next_bigger - y_of_next_smaller
                # ankathete
                b = next_bigger - next_smaller
                # atan is calculated in radians
                alpha = math.atan(a/b)
                # ankathete of smaller triangle
                c = x_input - next_smaller
                # gegenkathete of smaller triangle
                d = math.tan(alpha) * c
                # adding the smaller value to get the real value of wanted y
                calculated_y = y_of_next_smaller + d

                print(calculated_y)
        else:
            break


def try_parse_int(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def DFT(x):
    # creating an array for all entries, called k
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))

    # Calculate the exponential of all elements in the input array.
    # in discrete fourier transform, the sinusoids (analysing function) are defined like (e^-2j * pi * k * n(time) / N)) -> expl_img_2/3
    e = np.exp(-2j * np.pi * k * n / N)

    # fourier transform: multiplying the function with the analysing function (expl_img_2)
    # result is a complex number
    X = np.dot(e, x)

    # calculate the frequency
    N = len(X)
    n = np.arange(N)
    # / sampling rate
    T = N / 100
    freq = n / T

    # get the one side frequency (of Nyquist limit)
    # n_onside: number of samples on the one side
    n_oneside = N // 2
    f_oneside = freq[:n_oneside]

    # normalize the amplitude -> divide by the number of samples
    X_oneside = X[:n_oneside] / n_oneside

    for index, amplitude in enumerate(abs(X_oneside)):
        if round(amplitude) > 0:
            print(f"\nfrequency: {f_oneside[index]}Hz | amplitude: {amplitude}")
            print(f"= {round(amplitude,2)} * sin(2 * pi * {f_oneside[index]} * t)")


if __name__ == '__main__':
    parsed_x_values, parsed_y_values = load_function_values("./funciton_values.txt")

    thread = Thread(target=find_y_for_x, args=(parsed_x_values, parsed_y_values,))
    thread.start()

    plot_function(parsed_x_values, parsed_y_values)

    # Trigonometric
    parsed_x_values, parsed_y_values = load_function_values("./trigonometric_values.txt")
    plot_function(parsed_x_values, parsed_y_values)
    DFT(parsed_y_values)
