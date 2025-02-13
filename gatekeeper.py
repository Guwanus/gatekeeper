from datetime import datetime

def begroeting():
    uur = datetime.now().hour

    if 7 <= uur < 12:
        print("Goedemorgen! Welkom bij Fonteyn Vakantieparken")
    elif 12 <= uur < 18:
        print("Goedemiddag! Welkom bij Fonteyn Vakantieparken")
    elif 18 <= uur < 23:
        print("Goedenavond! Welkom bij Fonteyn Vakantieparken")
    else:
        print("Sorry, de parkeerplaats is ’s nachts gesloten")