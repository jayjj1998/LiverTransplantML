def Normalize(dataFrame):
    result = dataFrame.copy()
    max_value = result.max()
    min_value = result.min()
    result = (result - min_value) / (max_value - min_value)
    return result

