from astin_excercise1 import unique_members

# A non-empty array A consisting of N integers is given. # A permutation is a sequence containing each element from 1 to N once, and only once.
# For example, array A such that:
# A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2
# is a permutation, but array A such that: # A[0] = 4 A[1] = 1 A[2] = 3 # is not a permutation, because value 2 is missing.
# The goal is to check whether array A is a permutation.
# Write a function: # def solution(A) # that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
# For example, given array A such that:
# A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2 # the function should return 1.
# Given array A such that:
# A[0] = 4 A[1] = 1 A[2] = 3 # the function should return 0.
# Write an efficient algorithm for the following assumptions:
#  N is an integer within the range [1..100,000];
#  each element of array A is an integer within the range [1..1,000,000,000].

permut = [4, 1, 3, 2, 5, 6, 7, 8, 9, 10]
no_permut = [4, 1, 3]


def permutation(array):
    max_value = max(array)
    min_value = min(array)
    diff = max_value - min_value
    if len(array) == unique_members(array):
        if diff == (len(array)-min_value):
            return 1
        else:
            return 0



print('Permutation is: ', permutation(no_permut))