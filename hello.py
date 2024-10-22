print("Hello World")
# payment
# Authentication
# Chat
class Payment:
    def __init__(self, receipient, amount):
        self.receipient = receipient
        self.amount = amount
        print("Payment is made to", receipient, "of amount", amount)
    
    def check_balance(self,initial):
        return initial - self.amount

    @classmethod
    def update_initial_balance(cls, new_balance):
        cls.initial_balance = new_balance
    
    @staticmethod
    def check_valid_transaction(hour):
        if hour >= 8 and hour <= 17:
            return True
        return False
transaction1 = Payment("A", 25) # payment1 is an object -> it is an instance of the payment class
# Payment.update_initial_balance(800)
# print(transaction1.initial_balance)
# print(Payment.initial_balance)
print(transaction1.check_valid_transaction(13))