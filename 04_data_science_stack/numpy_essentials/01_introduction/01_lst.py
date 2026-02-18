temperatures = [32.5,34,53,34,53,54.8]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)

print(round(average,2))

#now if we increase the number of temperatures to a million , loop will get so slow it will take forever to 
# calculate the average. 
# this is where our hero comes up ok.
# that is numpy.
