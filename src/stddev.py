#spustenie napriklad stddev.py <in.txt

from mathlib import *
from fileinput import input


def mean_calc(nums):
    sum = 0
    for num in nums:
        sum = add(float(num),sum)

    mean = div(sum,len(nums))

    return mean


def variance(data):
    n = len(data)
    mean = mean_calc(data)
    deviations = [pow((sub(float(x),mean)),2) for x in data]
    deviations_sum=0
    for dev in deviations:
        deviations_sum = add(deviations_sum,dev)
    variance = deviations_sum / n
    return variance

def stdev(data):
  var = variance(data)
  std_dev = root(var, 2)
  return std_dev


num_array = input()
final_array = list()
for number in num_array:
    final_array.append(number)

final=final_array[0].split(" ")
print("Mean of numbers: "+str(mean_calc(final)))
print("Standard deviation is: "+str(stdev(final)))
