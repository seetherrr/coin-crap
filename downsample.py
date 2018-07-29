# Notes on implementation:
#
# how to downsample:
#
# first group rows into chunks of `n` rows
# n is number of input rows per output row
# list(zip(*[iter(s)]*n))
#
# you probably also want to cut any rows off the end of your input list
# which can't be used to make up a group of `n` input rows
#
# each output value in each output row will be the result of some aggregate
# function taken across all `n` values in the current chunk. e.g. output
# timestamp will be the minimum value found among the `n` input rows. e.g.
# 2 output open will be the first value found among the `n` input rows.
# etc.
#
# look for functions like min(), max(), avg(), and expressions like xs[0],
# xs[-1] etc. nvm avg doesn't exist

