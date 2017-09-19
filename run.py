import time


def gen_random_range(low, high):
    return int(low + int(round(time.time() * 1000)) % (high - low))

#gen_random_range function is used to create random numbers by time drift method.


def generate(low, high, times):
    for i in range(times):
        rand = gen_random_range(low, high)
        time.sleep(0.1)
        yield rand
# generate() is used to create random numbers given number of times


every = []

high = int(input("Select max. "))
high=high+1
low = int(input("Select min. "))

times = int(input("Select num of times "))

#high , low and times are the input values for deciding the range and number of times the number
# has to be generated



div_num = round(low + (high-low)/2)
print(div_num)

#div_num is the basis of partition.

#high
#here we have generated the partition and will print 73% times the higher numbers that div_num
#for that we have called the generate generator which yields the higher than the div_num values
low1 = div_num + 1
time1 = round((73 * times)/100)

for i in generate(low=low1,high=high,times=time1):
    every.append(i)

 #low
#here we have generated the partition and will print 27% times the smaller numbers that div_num
#for that we have called the generate generator which yields the smaller than the div_num values
time2 = times - time1
high1 = div_num - 1

for j in generate(low=low,high=high1,times=time2):
    every.append(j)

print(every)
#here in every[] we have appended the common result.:

