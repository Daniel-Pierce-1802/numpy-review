# Author: Daniel J. Pierce
# Date: 2026-08-16


def main():
    # Define interval and tolerance

    a = 1
    b = 2
    tolerance = 1e-6

    # Define function

    def f(x):
        return x**3 - x - 2

    root = bisection(f, a, b, tolerance)
    print(root)


def bisection(function, left, right, tolerance):
    left_eval = function(left)
    right_eval = function(right)
    midpoint = (left + right) / 2

    if check_signs(left_eval, right_eval) == False:
        return f"Function does not change signs over the given interval"

    else:
        while (right - left) > tolerance:
            left_side = check_signs(function(left), function(midpoint))
            if left_side == True:
                right = midpoint
            else:
                left = midpoint

            midpoint = (left + right) / 2

        return midpoint


def check_signs(left_eval, right_eval):
    if left_eval < 0 and right_eval < 0:
        return False

    elif left_eval > 0 and right_eval > 0:
        return False

    else:
        return True


if __name__ == "__main__":
    main()
