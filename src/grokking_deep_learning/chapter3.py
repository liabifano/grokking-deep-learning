import numpy as np

def dot_product(a, b):
    assert len(a) == len(b), 'inputs must be the same size'

    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]

    return result


def elementwise_multi(a, b):
    assert len(a) == len(b), 'inputs must be the same size'

    result = []
    for i in range(len(a)):
        result.append(a[i]*b[i])

    return result


def elementwise_add(a, b):
    assert len(a) == len(b), 'inputs must be the same size'

    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result


def layer_many_to_1(input, weights):
    pred = dot_product(input, weights)

    return pred


def layer_1_to_many(input, weights):
    pred = [w*input for w in weights]

    return pred


def layer_many_to_many(input, weights):
    pred = []

    for i in range(len(input)):
        pred.append(dot_product(input, weights[i]))

    return pred


def nn(input, weights):
    hidden = layer_many_to_many(input, weights[0])
    pred = layer_many_to_many(hidden, weights[1])

    return pred

def nn_np(input, weights):
    hidden = input.dot(weights[0])
    pred = hidden.dot(weights[1])

    return pred




if __name__ == '__main__':
    toes = [8.5, 9.5, 9.9, 9.0]
    wlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.5, 1.0]
    input = [toes[0], wlrec[0], nfans[0]]

    w1 = [[0.1, 0.1, -0.3],
          [0.1, 0.2, 0.0],
          [0.0, 1.3, 0.1]]

    print(layer_many_to_many(input, w1))

    w2 = [[[0.1, 0.2, -0.1],
           [-0.1, 0.1, 0.9],
           [0.1, 0.4, 0.1]],
          [[0.3, 1.1, -0.3],
           [0.1, 0.2, 0.0],
           [0.0, 1.3, 0.1]]]

    print(nn(input, w2))

    w2_np = [np.array(w).T for w in w2]
    input_np = np.array(input)

    print(nn_np(input_np, w2_np))

