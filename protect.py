
def encrypt(string):
	out =[]
	[out.append(chr(ord(c)+12)) for c in string]
	return "".join(out)
def decrypt(string):
	out =[]
	[out.append(chr(ord(c)-12)) for c in string]
	return "".join(out)