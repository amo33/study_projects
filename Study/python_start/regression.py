from ast import increment_lineno
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = 2 * np.random.rand(100,1)
y = 6 + 4*x + np.random.randn(100, 1) # make a noise to be as an input 

plt.scatter(x, y)
#plt.show()

def get_cost(y, y_pred):
    N = len(y)
    cost = np.sum(np.square(y-y_pred))/N
    return cost 

def get_weight_updates(w1, w0, X, y, lr = 0.01):
    N = len(y)
    w1_update = np.zeros_like(w1)
    w0_update = np.zeros_like(w0)

    y_pred = np.dot(X, w1.T) + w0
    diff = y - y_pred
    w0_factors = np.ones((N,1))
    # update is done : size of result is (1,N)*(N,1) - You see if we don't use transpose the original shape is 'row' focused [~~~~ ]วüลย  
    w1_update = -(2/N)*lr*(np.dot(X.T, diff))
    w0_update = -(2/N)*lr*(np.dot(w0_factors.T, diff))

    return w1_update, w0_update

def gradient_descent_Steps(X, y, iter = 10000):
    
    w0 = np.zeros((1,1))
    w1 = np.zeros((1,1))

    for ind in range(iter):
        w1_update , w0_update = get_weight_updates(w1, w0, X, y, lr = 0.01)
        w1 -= w1_update
        w0 -= w0_update

    return w1, w0 
iters = 10000
w1, w0 = gradient_descent_Steps(x, y, iters)
print("w1: {0: .3f} w0: {1: .3f}".format(w1[0][0], w0[0][0]))
y_pred = w1[0,0]*x + w0
print("Gradient Descent Total Cost:{0:.4f} ".format(get_cost(y, y_pred)))

def stocastic_gradient_descent_step(x, y, batch_size = 10, iters = 1000):
    w0 = np.zeros((1,1))
    w1 = np.zeros((1,1))
    prev_cost = 10000
    iter_index = 0

    for ind in range(iters):
        np.random.seed(ind)
        stocastic_random_index = np.random.permutation(x.shape[0])
        # get the amount of mini batch 
        sample_x = x[stocastic_random_index[0:batch_size]]
        sample_y = y[stocastic_random_index[0:batch_size]]

        w1_update , w0_update = get_weight_updates(w1, w0, sample_x, sample_y, lr = 0.01)
        w1 -= w1_update
        w0 -= w0_update
    return w1, w0

w1, w0 = stocastic_gradient_descent_step(x,y , iters)
print("w1: ", round(w1[0][0], 3), "w0: ", round(w0[0][0], 3))
y_pred = w1[0][0] * x + w0
print("Stocastic Gradient Descent Total cost: {0:. 4f}". format(get_cost(y,y_pred)))
# Since we are studying one element related(only x), we use the w1 and w0 whose size are (1,1)