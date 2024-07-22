import numpy as np
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    return dot_product

def matrix_multi_vector(matrix, vector):
    result1 = np.dot(matrix, vector)
    return result1

def matrix_multi_matrix(matrix1, matrix2):
    result2 = np.dot(matrix1, matrix2)
    return result2

def inverse_matrix(matrix):
    result3 = np.linalg.inv(matrix)
    return result3

def compute_eigenvalues_eigenvectors(matrix):
    result4 = np.linalg.eig(matrix)
    return result4

def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    result5 = dot_product / (magnitude_v1 * magnitude_v2)
    return result5