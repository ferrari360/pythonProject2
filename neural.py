# weight =0.1
# def neural_network(input, weight):
#     prediction = input * weight
#     return prediction
#
# number_of_toes = [8.5,9.5,10,9]
# input = number_of_toes[0]
# pred = neural_network(input,weight)
# print(pred)

# import numpy as np
# def neural(a,b):
#     pref = a.dot(b)
#     return pref
# a = np.array([1,2,3])
# b = np.array([3,4,5])
# print(neural(a,b))
#



# def w_sum(a,b):
#     assert(len(a) == len(b))
#     output = 0
#     for i in range(len(a)):
#         output += (a[i] * b[i])
#     return output
#
# weights = [0.1, 0.2, 0]
# def neural_network(input, weights):
#     pred = w_sum(input,weights)
#     return pred
#
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
#
# input = [toes[0],wlrec[0],nfans[0]]
# pred = neural_network(input,weights)
# print(pred)

# def elementwise_multiplication(vec_a, vec_b,vec_c):
#     assert (len(vec_a) == len(vec_b))
#     for i in range(len(vec_a)):
#          vec_c[i]=vec_a[i]*vec_b[i]
#     return vec_c
# vec_a = [1,3,4]
# vec_b = [3,4,6]
# vec_c = [0,0,0]
#
# print(elementwise_multiplication(vec_a, vec_b, vec_c))
#
#
# def vector_sum(vec_a):
#     sum = 0
#     for i in range(len(vec_a)):
#         sum+=vec_a[i]
#     return sum
# print(vector_average(vec_c))


# import numpy as np
# weights = np.array([0.1, 0.2, 0])
# def neural_network(input, weights):
#     pred = input.dot(weights)
#     return pred
#
# toes = np.array([8.5, 9.5, 9.9, 9.0])
# wlrec = np.array([0.65, 0.8, 0.8, 0.9])
# nfans = np.array([1.2, 1.3, 0.5, 1.0])
#
# input = np.array([toes[0],wlrec[0],nfans[0]])
# pred = neural_network(input,weights)
# print(pred)



# def w_sum(a,b):
#     assert(len(a) == len(b))
#     output = 0
#     for i in range(len(a)):
#         output += (a[i] *b[i])
#     return output
#
# def vect_mat_mul(vect,matrix):
#     assert(len(vect) == len(matrix))
#     output = [0,0,0]
#     for i in range(len(vect)):
#         output[i]=w_sum(vect,matrix[i])
#     return output
#
# weights = [[1,2,3],[4,5,6],[1,1,1]]
# a = [5,8,9]
# b = [4,7,1]
# c = [1,3,4]
# input = [a[0],b[0],c[0]]
#
# def neural_network(input, weights):
#     pred = vect_mat_mul(input,weights)
#     return pred
#
# print(neural_network(input, weights))

# import numpy as np
# ih_wgt = np.array([[0.1, 0.2, -0.1],[-0.1,0.1, 0.9],[0.1, 0.4, 0.1]]).T
# hp_wgt = np.array([[0.3, 1.1, -0.3],[0.1, 0.2, 0.0],[0.0, 1.3, 0.1]]).T
# weights = [ih_wgt, hp_wgt]
# print(weights)
#
# def neural_network(input, weights):
#     hid = input.dot(weights[0])
#     pred = hid.dot(weights[1])
#     return pred
#
# toes = np.array([8.5, 9.5, 9.9, 9.0])
# wlrec = np.array([0.65,0.8, 0.8, 0.9])
# nfans = np.array([1.2, 1.3, 0.5, 1.0])
# input = np.array([toes[0],wlrec[0],nfans[0]])
# pred = neural_network(input,weights)
# print(pred)

# import numpy as np
# a = np.array([1,4,7])
# b = np.array([4,5,2])
# c = np.array([[3,0,9],[7,6,5]])
# d = np.zeros((2,4))
# e = np.random.rand(2,5)
# print(a*0.1)
# print(c*0.2)
# print('a*b',a*b)
# print('a*b*0,2',a*b*0.2)
# print('a*c',a*c)
#
# import numpy as np
# a = np.zeros((4,1)).T
# print('a',a)
# b = np.zeros((4,3))
# print('b',b)
#
#
# c = a.dot(b)
# print(c.shape)
#
# import numpy as np
# a = np.array([1,2,3,4,5]).T
# b = np.array([1,4,5,6,7]).T
# c = a.dot(b)
# print(c)

# knob_weight = 0.5
# input = 0.5
# goal_pred = 0.8
#
# pred = input*knob_weight
# error = (pred-goal_pred)**2
# print(error)

weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.1

for iteration in range(1101):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2

    print("Error: " + str(error) + " Prediction: " + str(prediction))

    up_prediction = input*(weight + step_amount)
    up_error = (goal_prediction - up_prediction) ** 2

    down_prediction = input*(weight - step_amount)
    down_error = (goal_prediction - down_prediction) ** 2


    if down_error < up_error:
        weight -= step_amount
    if down_error > up_error:
        weight += step_amount