def palindrome_partitioner(s: str) -> int:
	n = len(s)
	if n <= 1:
		return 0

	res = list(range(n + 1))

	for c in range(n):
		l, r = c, c
		while l >= 0 and r < n and s[l] == s[r]:
			res[r + 1] = min(res[r + 1], res[l] + 1)
			l -= 1
			r += 1
	
		l, r, = c, c + 1
		while l >= 0 and r < n and s[l] == s[r]:
			res[r + 1] = min(res[r + 1], res[l] + 1)
			l -= 1
			r += 1

	return res[n] - 1

if __name__ == "__main__":
	print(palindrome_partitioner("aab"))
	print(palindrome_partitioner("aba"))
	print(palindrome_partitioner("abc"))

#confirmar q funcione con strings largos