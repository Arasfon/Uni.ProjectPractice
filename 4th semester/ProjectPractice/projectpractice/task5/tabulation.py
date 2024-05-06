from functions import calculate


def tabulate(x_min, x_max, x_step, y=1, a=1, b=1):
    count = int((x_max - x_min) // x_step) + 1

    x_values, f_values = [], []

    for i in range(count + 1):
        current_x = x_min + x_step * i
        x_values.append(current_x)

        current_f = calculate(current_x, y, a, b)
        f_values.append(current_f)

    return x_values, f_values
