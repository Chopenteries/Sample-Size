# s = sigma, e = euler's number
import math


def run():
    print("Welcome to sample size calculator")
    choice = input("Which method?(new or old?): \n")
    if choice == "new" or choice == "n":
        samples = input("Input your samples: \n").split()
        new_method(samples)
    elif choice == "old" or choice == "o":
        raw_confident = input("Put your confident (99.99%,95%,90% etc.) : \n")
        confident = ((100 - int(raw_confident)) / 100)
        final = cal(confident)
        print(f"your sample test should be : {round(final)} ({final}) test(s).")


def cal(c):
    e = 2.718
    sigma = 6
    first = sigma * c
    second = first ** c
    third = second * 100
    forth = third / e
    return forth


def new_method(x):
    for i in range(0, len(x)):
        x[i] = int(x[i])
    x1 = max(x)
    x2 = min(x)
    x3 = (x1 + x2)/2
    sigma_food = [x1, x2, x3]
    # Eo = e
    e = ((x1 - x2) / 2) / 50
    # N obs = n_obs
    n_obs = ((3 * find_sigma(sigma_food)) / e) ** 2
    # nφ = empirical_sample
    empirical_sample = math.log(n_obs) * math.pi
    # n* = n_mark
    n_mark = 30.07
    empirical_sample_minus_n_mark = empirical_sample - n_mark
    # Π = pi
    pi = 1 - ((empirical_sample - n_mark) / n_mark)
    pi_percent = pi * 100
    print(f"nφ      = {empirical_sample}\n"
          f"n*      = {n_mark}\n"
          f"nφ - n* = {empirical_sample_minus_n_mark}\n"
          f"Π       = {pi}\n"
          f"Π%      = {pi_percent}")


def find_sigma(x):
    y = len(x)
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = int(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / y
    answer = math.sqrt(v)
    return answer
