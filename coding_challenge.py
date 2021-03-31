import numpy as np
from heapq import heappop, heappush


def running_mean(x_i, old_mean, n):
    """
    Returns the running mean of all the accumulated inputs.
        Parameters:
                x_i: Current input
                old_mean: Mean calculated without x_i
                n: Total items input (N)
        Returns:
                Running Mean
    """
    return ((old_mean * (n - 1)) + x_i) / n


def running_std_dev(x_i_sum, x_i_sum_sq, x_i_mean, n):
    """
    Returns the running standard deviation of all the accumulated inputs.
        Parameters:
                x_i_sum: Sum of all inputs
                x_i_sum_sq: Sum of squares of all inputs
                x_i_mean: Mean calculated with current input
                n: Total items input (N)
        Returns:
                Running Standard Deviation
    """
    return np.sqrt((x_i_sum_sq / n) + (x_i_mean ** 2) - (2 * x_i_mean * x_i_sum / n))


def running_median(x_i, max_h, min_h):
    """
    Returns the running median of all the accumulated inputs.
        Parameters:
                x_i: Current input
                max_h: Max heap object
                min_h: Min heap object
        Returns:
                Running Median
    """
    if len(max_h) == len(min_h):
        return (max_h[0] + max(min_h)) / 2
    elif len(max_h) > len(min_h):
        return max_h[0]
    else:
        return min_h[0]


def main():
    print('Input a non-numeric value to exit.')

    # Initialize variables
    exit_flag = 0
    mean = 0
    inp_arr_len = 0
    running_sum = 0
    running_sum_sq = 0
    max_heap = []
    min_heap = []

    while not exit_flag:
        # Start inputting
        try:
            inp = float(input('Please input a number: '))
        except ValueError:
            print('Exiting: Non-numeric input encountered.')
            exit_flag = 1
            continue

        # Update input length, running sum, and running sum of squares
        inp_arr_len += 1
        running_sum += inp
        running_sum_sq += inp ** 2

        # Maintain and update a min heap and a max heap for median calculations
        if inp_arr_len == 1 or inp < max(min_heap):
            heappush(min_heap, inp)
        else:
            heappush(max_heap, inp)

        # Re-balance the heaps if difference in lengths > 1
        if len(min_heap) - len(max_heap) > 1:
            heappush(max_heap, max(min_heap))
            del min_heap[-1]
        elif len(max_heap) - len(min_heap) > 1:
            heappush(min_heap, max_heap[0])
            heappop(max_heap)
        else:
            pass

        # Return and print the running mean, standard deviation and median
        mean = running_mean(inp, mean, inp_arr_len)
        std = running_std_dev(running_sum, running_sum_sq, mean, inp_arr_len)
        median = running_median(inp, max_heap, min_heap)
        print(f'{mean}{", "}{std}{", "}{median}')


if __name__ == "__main__":
    main()
