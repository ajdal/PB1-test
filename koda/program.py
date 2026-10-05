from branje_podatkov import nalozi_studente


def izpisi_studente(studenti):
    for student in studenti:
        print(student)


def najdi_studenta(studenti, ime):
    for student in studenti:
        if student.ime == ime:
            return student
    return None


def main():
    studenti = nalozi_studente("koda/studenti.csv")

    print("Pozdravljen svet!")
    print()

    izpisi_studente(studenti)


if __name__ == "__main__":
    main()