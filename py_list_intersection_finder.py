def list_intersection_finder(lists: list[list[int]]) -> list[int]:

	if not lists:
		return []

	for sub in lists:
		if len(sub) == 0:
			return []

	res = set(lists[0])

	for sub in lists[1:]:
		res &= set(sub)

	return sorted(res)

if __name__ == "__main__":
	print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
	print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
	print(list_intersection_finder([[1, 2, 3], []]))
	print(list_intersection_finder([]))
