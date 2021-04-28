import random


def q_sort(a):
    if len(a) > 1:
        x = a[
            random.randint(0, len(a) - 1)]  # чоң жана кичине бөлүктөргө бөлүү үчүн салыштыруучу кокус маанини тандайбыз
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = q_sort(low) + eq + q_sort(hi)

    return a


a = [9, 5, -3, 4, 7, 8, -8]
a = q_sort(a)

print(a)

