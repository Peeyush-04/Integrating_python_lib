def generate_ndarray(shape, start=0, stop=1):
    """
    Generates an n-dimensional array with the specified shape and values ranging from start to stop-1.

    Parameters:
        shape (tuple): The shape of the array.
        start (int): The start value for the elements of the array (default is 0).
        stop (int): The stop value for the elements of the array (default is 1).

    Returns:
        list: The n-dimensional array.
    """
    try:
        if len(shape) == 0:
            return None
        elif len(shape) == 1:
            return [start + i * (stop - start) / (shape[0] - 1) for i in range(shape[0])]
        else:
            return [generate_ndarray(shape[1:], start, stop) for _ in range(shape[0])]
    except Exception as e:
        print(f"Error generating ndarray: {e}")
        return None

