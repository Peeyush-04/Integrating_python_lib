
import time

# Record the start time
start_time = time.time()

#program code goes here
import integratedlib
ndarray=integratedlib.generate_ndarray((5,5),1,40)
ndarray=integratedlib.reverse(ndarray)
# print(ndarray)
print(integratedlib.determinant(ndarray))

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print("Time taken:", elapsed_time, "seconds")