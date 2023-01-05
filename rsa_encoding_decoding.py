import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e, tot):
    g, x, y = egcd(e, tot)
    return x % tot

def rsa(p, q):
    e=0
    n=p*q
    nprime = (p-1)*(q-1)
    while verifPremier(e)==False:
        tmp = random.randint(100, 1000)
        if verifPremier(tmp) and e<nprime:
            e=tmp
    d = modinv(e, nprime)
    return ((n, e), (n, d))

def verifPremier(n):
	if n==0:
		return False
	for i in range (2, n):
		if n%i == 0:
			return False
	return True

def creationCle():
	p=0
	q=0
	while verifPremier(p)==False:
		tmp = random.randint(100, 1000)
		if verifPremier(tmp):
			p=tmp
	while verifPremier(q)==False or q==p:
		tmp = random.randint(100, 1000)
		if verifPremier(tmp):
			q=tmp
	(clePublique, clePrivee) = rsa(p, q)
	return[clePublique, clePrivee]

def encoderMessage(message, clePublique):
	tmp=[]
	for i in message:
		tmp.append(ord(i)**clePublique[1]%clePublique[0])
	return tmp

def decoderMessage(message, clePrivee):
	tmp=[]
	retour=""
	for i in message:
		tmp.append(i**clePrivee[1]%clePrivee[0])
	for i in tmp:
		retour+=chr(i)
	return retour

(clePublique, clePrivee) = creationCle()

message=input("Entrez le message de départ: ")
print("le message de départ est: ",message)
messageCode = encoderMessage(message,clePublique)
print("le message codé ressemble à ça: ",messageCode)
messageDecode = decoderMessage(messageCode, clePrivee)
print("le message décodé est le suivant:",messageDecode)