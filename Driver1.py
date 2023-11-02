import pandas as pd

# the linear relationship between two variables
# related to the slope of a straight line on a a Cartesian coordinate plane
# cartesian plane represents points in a 2D space
# y = mx + b
# result of this algorithm finds m = slope
# (the change in the y-coordinate/change in the x-coordinate)
def slope(x, y1, y2, y3):
    print(f'{x}-{y1}/{y2}-{y3} = {x-y1}/{y2-y3}');
    numerator = x - y1

    # if the numerator equals zero
    # then there is no change in the y-coordinate meaning that there is no vertical movement
    # and there is just a horizontal line
    # when the numerator is zero that means 
    if numerator == 0:
        return 1

    denominator = y2 - y3

    # if the denominator equals zero
    # then there is no change in the x-coordinate meaning that there is no horizontal movement
    # and there is just a vertical line
    # when the denominator is zero that means 
    if denominator == 0:
        return 1
    print(numerator/denominator);
    return numerator / denominator


def additionRecursive(df, length, lowerBound, upperBound, missingValue):
    firstTerm = multiplyRecursive(df, length, 0, lowerBound - 1, lowerBound, missingValue)

    secondTerm = multiplyRecursive(df, length, lowerBound + 1, length - 1, lowerBound, missingValue)

    output = firstTerm * secondTerm

    return output

# a recursive function that iterates through the set bounds
def multiplyRecursive(df, length, lowerBound, upperBound, index, missingValue):
    if lowerBound == upperBound:
        return slope(df.iloc[missingValue, 0], df.iloc[lowerBound, 0], df.iloc[index, 0], df.iloc[lowerBound, 0])

    return slope(df.iloc[missingValue, 0], df.iloc[lowerBound, 0], df.iloc[index, 0], df.iloc[lowerBound, 0]) * multiplyRecursive(df, length, lowerBound + 1, upperBound, index, missingValue)

# read csv file into a pandas dataframe object
# get the amount of rows in the dataframe object
data = pd.read_csv('input.csv');
length = len(data)
print(f'Dataset Object: (N = {length})\n');
print(data);


# find the missing value
# if the data at (i, 1) is not a number 
# then set the findValue to that of index of the missing value
findValue = None
for i in range(0, len(data) - 1):
    if pd.isna(data.iloc[i, 1]):
        findValue = i
        break
print(f'\nFind: f({findValue+1}) = ?');
print("-----------------------");

# loop through each index of the dataframe
# if current index value is equal to that of the missing value index
# then skip that index and continue with the loop
# if its the first index in the array
# then the summation is equal to that of the summation plus first algorithm
# if its the last index in the array
# then the summation is equal to that of the summation plus second algorithm
# if its the middle index in the array 
# then the summation is equal to that of the summation plus third algorithm
summation = 0
for i in range(0, len(data)):
    print()
    if i == findValue:
        print(f'f({findValue+1}) = Skipping this iteration because it includes the missing value');
        print("-----------------------");
        continue;
    elif i == 0:
        temp = multiplyRecursive(data, length, 1, length - 1, 0, findValue);
    elif i == length - 1:
        temp = multiplyRecursive(data, length, 0, length - 2, length - 1, findValue);
    else:
        temp = additionRecursive(data, length, i, length - 2, findValue);
    
    print(f'Combined slopes: {temp}');
    temp *= data.iloc[i, 1]
    print(f'f({i+1}):{temp}');
    summation += temp;
    print("-----------------------");

print(f'f({findValue+1}) = {summation}');
