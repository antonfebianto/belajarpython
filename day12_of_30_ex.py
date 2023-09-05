import string

print("1->",string.ascii_letters)
print("2->",string.ascii_lowercase)
print("3->",string.ascii_uppercase)
print("4->",string.digits)
print("5->",string.hexdigits)
print("6->",string.octdigits)
print("7->",string.printable)
print("8->",string.punctuation)
print("9->",string.whitespace)
print("10->",string._sentinel_dict)

import statistics
data = [6,7,8,5,3,5,6,7,8,9]

print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
print(statistics.stdev(data))
print(statistics.fmean(data))

import random

print(random.choice(data))
print(random.random())

