
rotations = int(input())
letter = 'z'
for i in range(rotations):
	if (ord(letter) >= 122):
		letter = 'a'
	letter = chr(ord(letter) + 1)
print(letter)
