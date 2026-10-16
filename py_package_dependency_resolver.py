def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

	if not packages:
		return []

	valid: set[str] = set(packages.keys())
	every: dict[str, int] = {}
	adj: dict[str, list[str]] = {pkg: [] for pkg in valid}

	for pkg, deps in packages.items():
		clean_deps = set(i for i in deps if i in valid)

		if pkg in clean_deps:
			return []

		every[pkg] = len(clean_deps)
		for i in clean_deps:
			adj[i].append(pkg)

	current = [pkg for pkg, deg in every.items() if deg == 0]
	res = []

	while current:
		current.sort()
		res.extend(current)

		cont = []
		for pkg in current:
			for dependent in adj[pkg]:
				every[dependent] -= 1
				if every[dependent] == 0:
					cont.append(dependent)

		current = cont

	if len(res) != len(packages):
		return []

	return res

if __name__ == "__main__":

	print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
