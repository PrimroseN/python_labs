from bankcard import *
from authentication import *

def main():

    cnum = input("Please enter the card number")
    print("The card number entered is : ",cnum)
    #card_num = card_num_list[3]
    card_num=int(cnum)
    auth = Authentication()
    card = BankCard(card_num)


    # 1)Verify the bank card
    verify = auth.verify_card(card_num)
    print("The card is :",verify)


    #2) Vendor: Displaying Vendor information
    details = card.get_card_details()
    print(details)


    # 3) Calculate checksum
    fportion = input("Please enter the first ")
    checksum=str(fportion)
    checksum = auth.get_checksum(fportion)
    print(" The checksum is : ", checksum)
    print()



    # 4) Generate random valid card
    vendor = "MasterCard"
    if vendor == 'Visa':
        first_digit = '4'
    elif vendor == 'MasterCard':
        first_digit = '5'
    checksum = auth.get_checksum(first_digit)
    print("The checksum: ", checksum)


if __name__ == '__main__':
    main()
