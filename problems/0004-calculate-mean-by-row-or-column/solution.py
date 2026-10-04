import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	np_matrix = np.array(matrix)

	if mode == "row":
		means = np_matrix.mean(axis=1)
	else:
		means = np_matrix.mean(axis=0)

	return means.tolist()