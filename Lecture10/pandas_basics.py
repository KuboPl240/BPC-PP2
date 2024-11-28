# Import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 0. Using pandas, create a dataframe named Z containing a 10x10 matrix of random integers <= 100.
# Hint: use np.random.randint(100, size=(10, 10)) to generate the numbers.
# Do not make explicit labels to the columns, use defaults.
# <<< TODO: add 1 line of code here and update the print statement below. >>>
# Print the dataframe contents to the terminal.
Z = pd.DataFrame(np.random.randint(100, size=(10, 10)))
print('*** 0.')
print(Z)

# 1. From the matrix, use the pandas dataframe operations to find and print:
# Hint: iloc method is your friend
# A. The cell in the 2nd row and 5th column
# Hint: pay attention where the indexing starts
print('*** 1A.')
print( Z.iloc[1, 4])  

# B. The whole last column
# Hint: pay attention how the last index is defined, no need for counting the columns
print('*** 1B.')
print(Z.iloc[:, -1])

# C. The two last elements of the 2nd row (using one command)
print('*** 1C.')
print(Z.iloc[1, -2:])


# 2. Filter the matrix.
# A. Create a new dataframe Z80 as a copy of Z, ensuring the changes will not affect Z. 
# (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)
Z80 = Z.copy()
# B. Apply the filtering to Z80, keep only the values < 80, assign zero to the others.
# Use the 'Matlab-like' notation.
# <<< TODO: add 1 line of code here and uncomment the print statement below. >>>
# Print both Z and Z80 to ensure the original dataframe is unchanged.
print('*** 2.')
Z80[Z80 >= 80] = 0
print(Z80)
print(Z)

# 3. Create a new dataframe ZT as a transpose of the matrix Z. 
# (Find a correct method in the reference https://pandas.pydata.org/docs/reference/frame.html). 
print('*** 3.')
ZT = Z.T
print(ZT)
 
# 4. Perform element-wise subtraction between the matrix Z and its transpose ZT.
# Do not overthink it... the first idea that comes to your mind could be the best one.
Z_sub = Z - ZT
print('*** 4.')
print(Z_sub)

# 5. Calculate the sums of the columns of matrix Z.
# Look at the manual for the tasks 5., 6. 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html
# See how the 'axis' parameter work. 
# See the 'See also' section, it might help you later.
Z_sums = Z.sum(axis=0)
print('*** 5.')
print(Z_sums)

# 6. Calculate the sums of the rows of matrix Z. 
row_sums = Z.sum(axis=1)
print('*** 6.')
print(row_sums)

# 7. Find the maximum value of the whole matrix.
max_value = Z.max().max()
print('*** 7.')
print(max_value)

# 8. Plot the column sums (use the Z_sums variable) using the plt.plot(...) method
# Set the x label as 'Column', and y label as 'Sum' 
# For the use of the matplotlib.pyplot x/y label methods, see the manual:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# Hint: remember we have imported the matplotlib.pyplot as plt
# A. Instantiate the plot
plt.plot(Z_sums)
# B. set the x label
plt.xlabel('Column')
# C. set the y label
plt.ylabel('Sum')
# D. Check the x axis range, is it as you expected? If not, explore the xticks method
plt.xticks(range(len(Z_sums)))
# E. show the plot 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
plt.show()

# 8. F. - optional: Try to ask the AI to get the code for the plot, copy the code here, and spot the differences.

# 9. Plot data from file
# Reading: have a brief look at the supported formats at https://pandas.pydata.org/docs/reference/io.html.
# These can be loaded directly to the dataframe with one simple command, pandas does the job for you.
# Find out the extension of the 'freq' file provided with this lab, and find the corresponding file type 
# in the above mentioned IO reference.

# A. read the file directly into the dataframe called df
df = pd.read_csv('C:\\Users\\240967\\Documents\\PP2\\BPC-PP2\\Lecture10\\freq.csv')
# B. print the dataframe to the terminal (only few first lines wil appear) and look at the column names 
# (they are not default as in previous example). Open the source file to see, where the names and data come from.
# Remember the column names, you will need one of them for the filtering in the next step.
print(df)
# C. copy the value pairs where the response is less than -3dB to a new dataframe 'df3', 
# again, use the Matlab-like filtering
df3 = df[df['RelativeResponse'] < -3]
df3.loc[0, 'RelativeResponse'] = -10
# D. optional: change some values in the df3 and look if it has any impact on the original dataframe df. 
print(df)
# If yes, how would you avoid it?
df3 = df[df['RelativeResponse'] < -3].copy()
# E. plot the values, with 'Frequency' on its x axis, and 'RelativeResponse' on its y axis
# Do you like the appearance? You can change the scale of the x axis...
plt.plot(df3['Frequency'], df3['RelativeResponse'])
plt.xscale('log')
plt.xlabel('Frequency')
plt.ylabel('RelativeResponse')
# F. Show the plot
plt.show()

