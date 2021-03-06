# Write a program to append the times tables to our sample.txt file.
# We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------

with open ("D:\Python\\10\FileIO\sample.txt", 'a') as jobber:
    print("\n\n", file=jobber)
    for i in range (1, 12):
        print("\t{} times 2 is {}".format(i, i*2), file=jobber)


# for i in range (1, 13):
#     print("\t{} times 2 is {}".format(i, i*2))