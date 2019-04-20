#below

def rot13(s):
    result = ""

    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        # The ord() method returns an integer representing Unicode code point for the given Unicode character.
        r = ord(v)

        # Shift number back or forward
        if r >= ord('a') and r <= ord('z'):
            if r > ord('m'):
                r -= 13
            else:
                r += 13
        elif r >= ord('A') and r <= ord('Z'):
            if r > ord('M'):
                r -= 13
            else:
                r += 13

        # Append to result.
        result += chr(r)

    # Return transformation.
    return result
# Test method by requiring user input
s =input("Please enter a plain text")

#printing userr input
print("The plain text you entered is :",s)

#cyphertextwhatever the user enteres
print("\nThe cyphertext of",(s),"is : "+ rot13(rot13(rot13(s))))

print("\nThe plain text becomes",rot13(s))



#cyphertext to plain text of  what the user entered
print ("\nCyphertext",(rot13(s)),"to plain  text","is ",rot13(rot13(s)))
