#RSA Level 3 5


from Crypto.PublicKey import RSA

my_key = RSA.import_key(open("mykey2").read())



print("n = ",str(my_key.n))
print("e = ",str(my_key.e))
print("d = ",str(my_key.d))
#print(str(my_key.p))
#print(str(my_key.q))
