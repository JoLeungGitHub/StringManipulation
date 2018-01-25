def duplicates(x):
	d = {};
	a = "";
	for char in x:
		if char in d:
			d[char] += 1
		else:
			d[char] = 1;

	for key in d:
		if d[key] > 1:
			a += key
	return ''.join(sorted(a))

def shuffle(a, b, c):
	for char in a:
		if char in c:
			c = c.replace(char, "")
		else:
			return False
	for char in b:
		if char in c:
			c = c.replace(char, "")
		else:
			return False
	if c == "":
		return True
	return False

def remove_vowels(a):
	i = 0
	while i < len(a):
		a[i] = ''.join(c for c in a[i] if c not in 'aeiouAEIOU')
		i += 1
	return a

def new_word(a, b):
	i = 0
	subs = []
	while i < len(a)-2:
		subs.append(a[i:i+3])
		i += 1
	for sec in subs:
		if sec in b:
			return a[:a.find(sec)] + b[b.find(sec):]
	return ""

def word_score(a):
	total = {}
	for word in a:
		score = 0
		passed = ""
		unique = True
		for char in word.lower():
			if char in passed and unique:
				unique = False
			score += ord(char) - 96
			passed += char
		if unique:
			score += 10
		if score in total:
			total[score].append(word)
		else:
			total[score] = [word]
	i = 0
	for key in sorted(total, reverse=True):
		for word in sorted(total[key], key=str.lower):
			a[i] = word
			i += 1
	return a
