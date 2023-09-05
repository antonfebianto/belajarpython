import statistics
import collections
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statisik:
    def __init__ (rekam, data):
        rekam.count_a = len(data)
        rekam.sum_a = sum(data)
        rekam.min_a = min(data)
        rekam.max_a = max(data)
        rekam.range_a = max(data) - min(data)
        rekam.mean_a = statistics.mean(data)
        rekam.modus_a = statistics.mode(data)
        rekam.stdv = statistics.stdev(data)
        rekam.variance = statistics.variance(data)
        rekam.freq_dis = collections.Counter(data)
    def infone_mase(rekam):
        return f"Count :{rekam.count_a}\nSum : {rekam.sum_a} \nMin:{rekam.min_a}\nMax:{rekam.max_a} \nMean :{rekam.mean_a}\nModus :{rekam.modus_a}\nRange : {rekam.range_a}\nStd Devisiasi : {rekam.stdv}\nVariance : {rekam.variance}\nFreq Distribution : {rekam.freq_dis}"

p_coba = Statisik(ages)
print(p_coba.infone_mase())