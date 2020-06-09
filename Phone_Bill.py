"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax
"""
class Phonebill:
    TOTAL_CALL = 0                         # Total Call Read from User
    TOTAL_MSG = 0                          # Total Message Read from User
    CAll_ALLOW_MONTH = 50                  # Allow call usage 50 minute per month
    MSG_ALLOW_MONTH = 50                   # Allow Message usage 50 messages per month
    ADD_CHARGE_CALL_PER_MINUTE = 0.25      # Additional minute of air time costs $0.25
    ADD_CHARGE_MSG_PER_EACH = 0.15       # Additional minute of message costs $0.15
    ADD_911_CHARGE = 0.44           # Additional charge to support 911 is $ 0.44
    SALES_TAX = 5                   # The entire bill is subject to 5 % sales tax
    ADD_CALL = 0                    # Additional call time more than 50 min in a month
    ADD_MSG = 0                     # Additional msg more than 50 msg in a month
    ADD_CALL_CHARGE = 0             # Additional Call Charge if more than 50 minute
    ADD_MSG_CHARGE = 0              # Additional Msg Charge if more than 50 message
    TOTAL_BILL_5_EXCLUDE = 0        # Total Bill NOT including 5 % Sales Tax
    TOTAL_BILL_5_INCLUDE = 0        # Total Bill including 5 % sales Tax
    MONTHLY_PLAN_BILL = 15          # Monthly Plan costs $15
    
    # Get Total number of minutes and text messages used in a month
    def get_usage(self):
        cond = True
        try:
            self.TOTAL_CALL = float(input("Enter the total number of minutes : "))
            self.TOTAL_MSG = float(input("Enter the total number of messages : "))
        except ValueError:
            print("Invalid Input!!")
            cond = False
        return cond
    
    # Check Additional Usage
    def check_additional(self):
        if self.TOTAL_CALL > self.CAll_ALLOW_MONTH:
            self.ADD_CALL = round(self.TOTAL_CALL - self.CAll_ALLOW_MONTH,2)
        if self.TOTAL_MSG > self.MSG_ALLOW_MONTH:
            self.ADD_MSG = round(self.TOTAL_MSG - self.MSG_ALLOW_MONTH,2)
        
    # Calculate The Additional Bill
    def calculate_additional(self):
        self.ADD_CALL_CHARGE = round(self.ADD_CALL * self.ADD_CHARGE_CALL_PER_MINUTE,2)
        self.ADD_MSG_CHARGE = round(self.ADD_MSG * self.ADD_CHARGE_MSG_PER_EACH,2)

    # Calculate including 5 % sales tax
    def calculate_tax(self):
        self.TOTAL_BILL_5_EXCLUDE = round(self.MONTHLY_PLAN_BILL + self.ADD_CALL_CHARGE + self.ADD_MSG_CHARGE + self.ADD_911_CHARGE,2)
        self.TOTAL_BILL_5_INCLUDE = round(self.TOTAL_BILL_5_EXCLUDE + ((self.TOTAL_BILL_5_EXCLUDE * self.SALES_TAX) / 100),2)

    # Pinter the Bill
    def print_bill(self):
        print("#########################")
        print(f"Your Monthly Plan Bill  -  ${self.MONTHLY_PLAN_BILL}")
        if self.TOTAL_CALL > self.CAll_ALLOW_MONTH:
            print(f"Additional Call {self.ADD_CALL} - ${self.ADD_CALL_CHARGE}")
        if self.TOTAL_MSG > self.MSG_ALLOW_MONTH:
            print(f"Additional Call {self.ADD_MSG} - ${self.ADD_MSG_CHARGE}")
        print(f"Total Bill - ${self.TOTAL_BILL_5_EXCLUDE}")
        print(f"Total Bill inc 5 % Tax - ${self.TOTAL_BILL_5_INCLUDE}")   
        print("########################") 
    
my_phone_bill = Phonebill()
cond = my_phone_bill.get_usage()
if cond == True:
    my_phone_bill.check_additional()
    if my_phone_bill.TOTAL_CALL > my_phone_bill.CAll_ALLOW_MONTH or my_phone_bill.TOTAL_MSG > my_phone_bill.MSG_ALLOW_MONTH:
        my_phone_bill.calculate_additional()
    my_phone_bill.calculate_tax()
    my_phone_bill.print_bill()
