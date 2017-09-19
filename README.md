# randnum

1.gen_random_range() function is used to generate random numbers by time drift method.
2.generate() is used to create random numbers given number of times.Here in this gen_random_range()
is called to generate random numbers given number of times.
3.User input for high,low ,times is taken which defines respectively the highest number,lowest number
to create a range of random numbers for given number of times (i.e times)
4.div_num is the basis of the partition. Numbers biased towards highest number and lowest numbers
are partitioned based on this number.
5.To print the higher numbers than div_num,we called generate() by passing key arguments as:
low1 = div_num + 1 (This is done to ensure that in any case ,number generated should be higher
than div_num)
high = high + 1 (because when list is created using gen_random_range,we want to include the
highest number entered nu user also)
times = time1(= rounds(73*times)/100))i.e we want to generate higher number than the div_num only
for 73% times of total times we want number to be printed.

6. //ly, for printing the lower number than div_num,we passed following arguments to generate():
time2 = times - time1 i.e total times opted by user - num of times higher num is printed
high1 = div_num - 1 (printed only numbers shorter than div_num for 23% times)
7.Results of both step 6 and 7 are appended in every[]
8.Result printed