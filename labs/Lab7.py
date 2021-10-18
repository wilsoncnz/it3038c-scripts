import numpy
numpy.random.seed(1234) #creates a random seed for random numerical valyes

array = numpy.array([[4,4,4], [5,4,3], [9,7,2], [3,7,5]]) #creates an array of numbers
print('new array= ',array)

number_of_values = numpy.random.randint(2,10,4)
print('Number of Values= ', number_of_values)

p=[] #creates empty array
for i in range(4):
    p.append(numpy.random.normal(loc=array[i,:], scale=1, size=(number_of_values[i],3))) 
    #add values onto empty 'p' array

p=numpy.concatenate(p) #overwrites 4 p arrays and merges them into a single array
p_points=p.shape[0] #returns number of points in p array
idx=numpy.arange(p_points) #indexes p values
print(idx)
rnd_idx=numpy.random.permutation(idx) #randomly scrambles index
print(rnd_idx)
p=p[rnd_idx] #mix p values up based on scrambled index