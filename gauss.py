import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Augmented matrix
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    
    # Forward elimination
    for i in range(n):
        # Find the pivot
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        # Swap rows
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        
        # Eliminate column entries below the pivot
        for j in range(i + 1, n):
            ratio = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= ratio * augmented_matrix[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.sum(augmented_matrix[i, i + 1:n] * x[i + 1:])) / augmented_matrix[i, i]
    
    return x
