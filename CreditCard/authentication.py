import random

#this class is for authentication
class Authentication:
    def __init__(self):
        self.sum = 0

        #this function is to verify the cade  using luhn methody
    def verify_card(self, card_num):
        total_even_i = 0
        total_odd_i = 0
        str_list = str(card_num)
        for i in range((len(str_list) - 1), -1, -1):
            if i % 2 == 0:
                num_even_i = int(str_list[i])
                num_even_i = num_even_i * 2
                if num_even_i > 9:
                    num_even_i = (num_even_i - 9)
                total_even_i += num_even_i
            else:
                total_odd_i += int(str_list[i])

        self.sum = total_even_i + total_odd_i
        if self.sum % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

        #function to checksum luhn method also known as modulus 10 or mod 10 algorithm
    def get_checksum(self, first_portion):
        first_portion = str(first_portion)
        valid_card_lenght = 16
        for x in range((valid_card_lenght-1) - len(first_portion)):
            other_portion = str(random.randint(0, 9))
            first_portion += other_portion

        self.verify_card(int(first_portion))
        if self.sum % 10 == 0:
            checksum = 0
        else:
            checksum = 10 - (self.sum % 10)
            full_card = first_portion + str(checksum)
        print("The generated Card: ", full_card)
        print("The card is :",self.verify_card(full_card))
        return checksum
