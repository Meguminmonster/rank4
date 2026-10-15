def array_rotation_detector(arr1: list, arr2: list) -> bool:

	if len(arr1) != len(arr2):
		return False

	long = len(arr1)

	if long == 0:
		return True

	mix = arr1 + arr1

	for i in range(long):
		if mix[i:i + long] == arr2:
			return True

	return False

if __name__ == "__main__":
	print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
	print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
