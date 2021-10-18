numpy.random.seed(1234) #creates a random seed for random numerical valyes

array = numpy.array([[4,4,4], [5,4,3], [9,7,2], [3,7,5]]) #creates an array of numbers
print('new array= ',array)

number_of_values = numpy.random.randint(2,10,4)
print('Number of Values= ', number_of_values)

idx=numpy.arange(70) #indexes values
print(idx)
rnd_idx=numpy.random.permutation(idx) #randomly scrambles index
print(rnd_idx)