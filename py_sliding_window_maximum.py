def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

	if not nums or k <= 0:
		return []

	q: list[int] = []
	head: int = 0
	res: list[int] = []

	for i in range(len(nums)):
		if head < len(q) and q[head] <= i - k:
			head += 1
		while len(q) > head and nums[q[-1]] <= nums[i]:
			q.pop()
		q.append(i)
		if i >= k - 1:
			res.append(nums[q[head]])
	return res

if __name__ == "__main__":
	print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
	print(sliding_window_maximum([1, 2, 3], 3))
	print(sliding_window_maximum([1, 2, 3], 4))
	print(sliding_window_maximum([1, 2, 3], 0))
	print(sliding_window_maximum([], 2))
