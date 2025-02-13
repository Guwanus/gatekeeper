from datetime import datetime

uur = datetime.now().hour
kenteken = ["71-pd-dd", "29-jkf-5", "87-pb=hr", "65-hkr-8"]
invoerkenteken = input("Voer kenteken in:")

if invoerkenteken in kenteken:

    if uur >= 7 and uur <= 12:
        print("Goedemorgen! Welkom bij Fonteyn Vakantieparken")
    elif uur >= 12 and uur <= 18:
        print("Goedemiddag! Welkom bij Fonteyn Vakantieparken")
    elif uur >= 18 and uur <= 23:
        print("Goedenavond! Welkom bij Fonteyn Vakantieparken")
    else:
        print("Sorry, de parkeerplaats is ’s nachts gesloten")
    
else:
    print("U heeft helaas geen toegang tot het parkeerterrein")