import os

sim = {"num" : "1768000777", #mobile number
"CC" : "+880", #country code
"KI" : "", #ki 
"IMSI" : "08"+"", #must start with 08
"ICCID" : "",
"PIN1" : "1234",
"PUK1" : "12345678",
"PIN2" : "5678",
"PUK2" : "8754321"
}

for i in sim:
    print(i+" = "+sim[i])