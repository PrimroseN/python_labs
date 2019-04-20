from authentication import Authentication

#creating  a class called BanCard
class BankCard:
    #Below are bankcard function with conditions
    #"__init__" is a reseved method in python classes()
    #self represents the instance of the class
    def __init__(self, card_num):
        self.card_num = card_num
        self.vendor = self.get_vendor(self.card_num)

        #validating the card
    def get_vendor(self, card_num):
        validity = Authentication().verify_card(card_num)
        if validity == 'Valid':
            first_digit = str(card_num)[0]
            industry = ''

            #conditions

            if first_digit == '3':
                industry = 'Travel & Entertainment'
                issuer = 'American Express'
            elif first_digit == '4' or first_digit == '5' or first_digit == '6':
                industry = 'Banking'
                if first_digit == '4':
                    issuer = 'Visa'
                elif first_digit == '5':
                    issuer = 'MasterCard'
                else:
                    issuer = 'Discover'
            return '\tIndustry: {0} \n\tIssuer: {1}'.format(industry, issuer)
        else:
            self.vendor = "Invalid card has no Vendor"
            return self.vendor

        #getting card details
    def get_card_details(self):
        return "\nCARD DETAILS\nCard No.: {0} \nVendor Info: \n{1}".format(self.card_num, self.vendor)

