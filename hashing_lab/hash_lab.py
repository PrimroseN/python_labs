#imported python hashing library
#a hash chain is a hash value that we hash again, and again to produce a chain.
#A = MD5(‘seed’)
#B = MD5(A)
#C = MD5(B)

import hashlib


#hashing a string hello world
some_string = "Hello World"
#md5 hashing converting the string to byte using the utf-8 encording
hash = hashlib.md5(str(some_string).encode('utf-8'))
#printing the md5 hash #
print("Hello world hash is :", hash.hexdigest())


# seed=('a2c83976c0adb482d280c6b10a042be3')
# using the example given, username 'ECSC' changed to lower case to be hashed to arrive at seed
seed='ECSC'.lower()
# seed.lower()

# the given challenge hash for 'ECSC'
challengehash='c89aa2ffb9edcc6604005196b5f0e0e4'

#The md5 hash to hash the given ECSC string
hash = hashlib.md5()

# for the md5 hashing algorithm to run on a string variable it needs to convert the string to byte using the utf-8 encording
# Now hash the seed using md5b
hash.update(seed.encode('utf-8'))

# declare a variable called seed & initialize it to false
seen = False
# md5 hash value made readable
myseedhash=(hash.hexdigest())

# print challenge hash found
print("My seed hash",myseedhash)

# print challenge hash found
while (seen== False):
    #if challenge hash is found, print found challenge hash
    if(myseedhash==challengehash):
        print("found challengehash")
        seen = True
        # break out of loop
        break

    else: #if hash challenge hash not keep hashing
        myseedhash = hashlib.md5(myseedhash.encode('utf-8')).hexdigest()
        # printing hashes as it loops through
        print("hashes :",myseedhash)
