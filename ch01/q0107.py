
# 1.7
# Rotate Matrix
#
# Given an image represented by an NxN matrix, where each pixel in the
# image is 4 bytes, write a method to rotate the image by 90
# degrees. Can you do this in place?
#


def sol1 (m) :
    return list (zip (* (m [::-1])))


def sol2 (m) :
    return (list (zip (* m))) [::-1]

