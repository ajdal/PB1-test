from csv import DictReader
from model import Student

def nalozi_studente(pot):
    studenti = []
    with open(pot, encoding="utf-8") as file:
        bralec = DictReader(file)

        for vrstica in bralec:
            student = Student(
                vrstica["Ime"],
                vrstica["Program"],
                int(vrstica["Letnik"]),
            )
            studenti.append(student)

    return studenti