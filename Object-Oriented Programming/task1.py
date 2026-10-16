import numpy as np

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

def attach_names(data, names):
    attached_output = []

    for data_vals, name in zip(data, names):
        attached_output.append({'name': name,
                                'data_vals': data_vals})

    return attached_output

print(attach_names(data, ['Alice', 'Bob']))