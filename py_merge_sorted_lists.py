def merge_two(l1: list[int], l2: list[int]) -> list[int]:

	res = []
	i = 0
	b = 0

	while i < len(l1) and b < len(l2):
		if l1[i] <= l2[b]:
			res.append(l1[i])
			i += 1
		else:
			res.append(l2[b])
			b += 1

	while i < len(l1):
		res.append(l1[i])
		i += 1
	while b < len(l2):
		res.append(l2[b])
		b += 1
	
	return res

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

	if not lists:
		return []

	res = lists

	while len(res) > 1:
		ronda = []
		for i in range(0, len(res), 2):
			if i + 1 < len(res):
				a = merge_two(res[i], res[i + 1])
				ronda.append(a)
			else:
				ronda.append(res[i])
		res = ronda

	return res[0]

if __name__ == "__main__":
	print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
	print(merge_sorted_lists([[]])) 
	print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
