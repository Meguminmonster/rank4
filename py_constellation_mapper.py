def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:

	space = [["." for _ in range(dim)]for _ in range(dim)]

	for r, c in stars:
		if 0 <= r < dim and 0 <= c < dim:
			space[r][c] = "*"

	return ["".join(i) for i in space]

if __name__ == "__main__":
	print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
	print(constellation_mapper([], 2))
