import sklearn 
import joblib

model = joblib.load("Spam-detection.pkl")

# Just a Basic PyTest
Emails= ["""Dear Winner,

Congratulations!!! Your email address has been selected in our International Lottery Draw.

You have won $5,000,000 USD.

To claim your prize, please reply immediately with the following details:

Full Name
Address
Phone Number
Bank Account Information

You must respond within 24 hours or your winnings will be forfeited.

Kind regards,
Dr. Michael Johnson
Claims Officer
Global Lottery Commission""", """England v Macedonia - dont miss the goals/team news. Txt ur national team to 87077 eg ENGLAND to 87077 Try:WALES, SCOTLAND 4txt/ú1.20 POBOXox36504W45WQ 16+""",
"""Congrats! 1 year special cinema pass for 2 is yours. call 09061209465 now! C Suprman V, Matrix3, StarWars3, etc all 4 FREE! bx420-ip4-5we. 150pm. Dont miss out!""",
"Sorry my roommates took forever, it ok if I come by now?"]

def test():
    results = []
    for i in range(4):
        results.append(model.predict([Emails[i]])[0])
    assert [1,1,1, 0] == results