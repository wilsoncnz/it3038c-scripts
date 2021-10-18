# it3038c-scripts: Lab 7
### NumPy for Lab 7
In this lab, we will be utilizing the python plugin NumPy. NumPy is a plugin that is used for applying mathematical operations to numerical values in a nice code form. 

In this example, we will use NumPy to generate a random sample of data and manipulate it to allow for something like blind testing - this would be good for a numerical study or something similar, maybe practicing data interpretation.

### How to Install NumPy
NumPy is a plugin for Python, to install, I used Pip.
To install using Pip, type:

<code> pip install numpy </code> 

<code> import numpy </code>

## Looking at Lab 7 code - Python
https://github.com/wilsoncnz/it3038c-scripts/blob/main/labs/Lab7.py

In this Lab I chose to generate random numerical values to show how NumPy can manipulate arrays, the values in the array, indexes, index values, etc.
This would be useful with manipulating data, gathering data, organizing data, and research settings. You can click on the link above to access the code and copy and paste it into whatever application you would like that supports Python. 

<code> numpy.random.seed(1234) </code>

this creates a constant set of random numerical values.

<code> array = numpy.array([[4,4,4], [5,4,3], [9,7,2], [3,7,5]]) 
print('new array= ',array) </code>

Creates an array for random numbers.

<code> number_of_values = numpy.random.randint(2,10,4)
print('Number of Values= ', number_of_values) </code>

This outputs 4 random integer values between 2 and 10

<code> p=[] 
for i in range(4):
    p.append(numpy.random.normal(loc=array[i,:], scale=1, size=(number_of_values[i],3))) 
</code>

Creates an empty array so we can add values later, using the next p.append function. Also creates normal distribution of values located around each array.

<code> p=numpy.concatenate(p) 
print('p values in one array: ', p) </code>

Concatenate merges the 4 p arrays into single aray.

<code> p_points=p.shape[0]
print('Number of points in p= ', p_points) </code>

Returns the number of points in the p array.

<code> idx=numpy.arange(p_points) 
print('Indexing p values= ', idx) </code>

Indexes the number of p values starting at 0.

<code> rnd_idx=numpy.random.permutation(idx) 
print('Scrambled index= ', rnd_idx) </code>

Randomly scrambles index!

<code> p=p[rnd_idx] 
print('p values mixed up', p) </code>

Mixes and outputs p values up based on scrambled index.

This code could be useful for generating data points around localized zones and mixing index values for corresponding points. 








  

