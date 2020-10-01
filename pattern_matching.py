pattern = 'GGGT'
genome = 'AATCGGGTTCAATCGGGGT'

def pattern_match(pattern,genome):
	start_points = []
	for i in range(len(genome) - len(pattern) + 1):
		if genome[i:i+len(pattern)] == pattern:
			start_points.append(i)
	return start_points

ans = pattern_match(pattern,genome)

print(" ".join(str(x) for x in ans))
