
def determinant(matrix):
    """
    Finds the determinant of a square matrix using recursive expansion by minors.

    Parameters:
        matrix (list of lists): The input square matrix.

    Returns:
        float: The determinant of the matrix.
    """
    # Base case: for a 1x1 matrix, the determinant is the single element
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case: for a 2x2 matrix, the determinant is calculated directly
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        det = 0
        for j in range(len(matrix)):  # Choose a column to calculate minors
            # Calculate the minor by excluding the first row and the current column
            minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
            # Recursively calculate the determinant of the minor and sum up with sign changes
            det += (-1) ** j * matrix[0][j] * determinant(minor)
        return det