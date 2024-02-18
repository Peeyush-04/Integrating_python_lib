
import time

# Record the start time
start_time = time.time()

# program code goes here

import firstlib
import seclib
import thirdlib
ndarray=thirdlib.generate_ndarray((5,5),1,40)
ndarray=firstlib.reverse(ndarray)
# print(ndarray)
print(seclib.determinant(ndarray))
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print("Time taken:", elapsed_time, "seconds")
