import pandas as pd

def algorithm(x, y1, y2, y3):
    numerator = x - y1

    if numerator == 0:
        return 1

    denominator = y2 - y3

    if denominator == 0:
        return 1

    return numerator / denominator

def additionRecursive(df, length, lowerBound, upperBound):
    firstTerm = multiplyRecursive(df, length, 0, lowerBound - 1, lowerBound)

    secondTerm = multiplyRecursive(df, length, lowerBound + 1, length - 1, lowerBound)

    output = firstTerm * secondTerm

    return output

def multiplyRecursive(df, length, lowerBound, upperBound, index):
    if lowerBound == upperBound:
        return algorithm(df.iloc[2, 0], df.iloc[lowerBound, 0], df.iloc[index, 0], df.iloc[lowerBound, 0])

    return algorithm(df.iloc[2, 0], df.iloc[lowerBound, 0], df.iloc[index, 0], df.iloc[lowerBound, 0]) * multiplyRecursive(df, length, lowerBound + 1, upperBound, index)

# Read your data into a DataFrame without column names
data = pd.read_csv('input.csv');
df = pd.DataFrame(data)

length = len(df)
findValue = None
summation = 0

for i in range(0, len(df) - 1):
    if pd.isna(df.iloc[i, 1]):
        findValue = i
        break

for i in range(0, len(df)):
    if i == findValue:
        continue
    elif i == 0:
        summation += df.iloc[i, 1] * multiplyRecursive(df, length, 1, length - 1, 0)
    elif i == length - 1:
        summation += df.iloc[i, 1] * multiplyRecursive(df, length, 0, length - 2, length - 1)
    else:
        summation += df.iloc[i, 1] * additionRecursive(df, length, i, length - 2)

print(summation)
