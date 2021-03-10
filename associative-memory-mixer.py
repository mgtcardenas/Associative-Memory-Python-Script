import numpy as np
import random as rnd

np.set_printoptions(precision=2)  # Let me see up to 2 decimals

#############
# CONSTANTS #
#############
M = 9  # The number of rows in the matrix
N = 16  # The number of cols in the matrix
SR = 0.7  # The Silence Rate, how probable it is that a note in the matrix (piano roll representation) will be a silence
LOWER_DIFF_LIMIT = (int)((M * N) * 0.05)  # %5 of the total size of the example arrays
UPPER_DIFF_LIMIT = (int)((M * N) * 0.70)  # %70 of the total size of the example arrays

#########################
# CONVENIENCE FUNCTIONS #
#########################
''' Convenience function for interpreting the results.
Translates the 1s and -1s to 1s and 0s. '''


def pretty_print_np_array(arr, m, n):
    i = 0
    for x in range(m):
        for y in range(n):
            if arr[i] == -1:
                print("0,", end="")
            else:
                print("1,", end="")
            i += 1
        print()


''' Function that measures how many elements two binary vectors do not have in common.
These vectors must be represented by 1s and -1s and be of the same size.
This function depends on numpy. '''


def calculate_binary_difference(u, v):
    return np.sum(np.absolute(u - v)) / 2


print(calculate_binary_difference(np.array([-1, -1, -1]), np.array([-1, -1, 1])))
print(np.absolute(np.array([-1, -1, -1])))

''' Function that returns a valid random input given the size of the samples.
It should also be given a silence rate (sr) value, i.e. the probability that a note will be a silence. '''


def get_random_input(n, sr):
    random_input = np.empty(n)
    for i in range(n):
        if rnd.random() > sr:  # it seems it is very important for this thing to be above 0.5
            random_input[i] = 1
        else:
            random_input[i] = -1
    return random_input


###################################################
# DEFINE THE SIGN FUNCTION AND HAVE IT VECTORIZED #
###################################################
def bipolar_step(n):
    return 1 if n >= 0 else -1


v_bipolar_step = np.vectorize(bipolar_step)  # vectorize a function -> apply it to each element of np_array

########################################################
# SPECIFY THE WEIGHT MATRIX W (AND THE BIAS VECTOR Ib) #
########################################################
z = np.loadtxt("training-patterns.txt", dtype='int', delimiter=',')

p = len(z)  # 2, The number of patterns
n = len(z[0])  # 144, The number of elements of each pattern (also equal to M x N)

ii = np.dot(np.identity(n), p / n)  # what to subtract in order to get 0s in the diagonal

w = np.outer(z[0], z[0].T)
for i in range(1, len(z)):
    w += np.outer(z[1], z[1].T)
w = np.dot(w, 1 / n)
w = w - ii
print(w)  # present the weight matrix

######################################
# PRESENT THE INITIAL INPUT VECTOR X #
######################################
i = 0
while True:
    print("RANDOM INPUT (INITIAL X)")
    x = get_random_input(M * N, SR)
    pretty_print_np_array(x, M, N)
    u = np.dot(x, w)  # multiplying (x, w) = (w, x) = (w.T, x) = (x.T, w)
    result = v_bipolar_step(u)
    diff1 = calculate_binary_difference(z[0], result)
    diff2 = calculate_binary_difference(z[1], result)
    # NOTE: Perhaps what I should do is have limits at the top and bottom
    # for example I want it to have at least 5 different notes, but I don't want it to have nearly 90% of its notes different
    # This parameters should be proportional to the sizes of the arrays (aka. len(z[0])).
    # Maybe diff1 > 5% and less than 80% I dunno
    i = i + 1
    if LOWER_DIFF_LIMIT < diff1 and diff1 < UPPER_DIFF_LIMIT and LOWER_DIFF_LIMIT < diff2 and diff2 < UPPER_DIFF_LIMIT:
        break

print("RESULT:")
pretty_print_np_array(result, M, N)

print("NUM ITERATIONS:", end="")
print(i)
