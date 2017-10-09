woord = "zak"
ggl = []
gl = []
fouten = 0
print ("Welkom bij")

print("""
    ___         ___        ___     ___
   / __)       / __ \    (    )   /  __)    _
  (  (_-.     / (__) \    )  (__ ( (_-.     (
   \____/    (___)(___)  (______) \___/  \___)


""")


while True:

    vraag1 =  input("Kies een letter of kies een ? om het woord te raden:")
    lengte = len(vraag1)
    lengtewoord = len(woord)
    lengteggl = len(ggl)


    if lengte > 1:
        input("Fout, probeer het nog een keer:")
        fouten += 1
    else:

        if vraag1 in woord:
            ggl.append(vraag1)
            print("Goed geraden!")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))

        elif vraag1 == "?":
            raad = input("Raad het woord:")

        elif vraag1 not in woord:
            gl.append(vraag1)
            vraag2 = input("Fout, probeer het nog een keer:")
            print("Dit zij alle geraden letters: " + str(gl))
            print("Dit zijn je goed geraden letters: " + str(ggl))
            fouten += 1
            if vraag2 in woord:
                ggl.append(vraag2)
                print("Goed geraden!")
                print("Dit zij alle geraden letters: " + str(gl))
                print("Dit zijn je goed geraden letters: " + str(ggl))

            elif vraag2 not in woord:
                gl.append(vraag2)
                vraag2 = input("Fout, probeer het nog een keer:")
                print("Dit zij alle geraden letters: " + str(gl))
                print("Dit zijn je goed geraden letters: " + str(ggl))
                fouten += 1

            if fouten > 5:
                einde =input("Je hebt 5 fouten kies stop om te stoppen.")
                if einde = "stop":
                    break


            if lengteggl == lengtewoord:
                raad = input("Raad het woord met alle goed geraden letters:")
                if raad == woord:
                    print("Je hebt het woord goed geraden!")
                    break
                else:
                    input("Fout, probeer het nog een keer:")


















"""
if letters == woord:
    print("Ja je hebt ht woord geraden goedzo!" + woord)

"""
"""
woordenlijst= lijst met geheime woorden geheim woord wordt bepaald = bijvoorbeeld appel
functie=aantalFouten om fouten te tellen - aantalFouten = 0
functie tekenGalg(aantalFouten): met stappen gelijk aan fouten.
stap 1:teken stap1
------------------------
stap 2: teken stap2
------------------------
stap3: teken stap3
------------------------
stap4: teken stap4
------------------------
stap5: teken stap5
------------------------

functie ABC= houdt bij welke letters al ingevoerd zijn.

functie Letter= vraag om  1 letter in te typen.= print"Typ 1 letter in"

functie punten= houdt aantal punten per spel dat je speelt bij

functie highscore= telt aantal punten van het spel waar je de meeste punten hebt behaald op als "punten">"highscore" maak "punten"="highscore"
als Letter="?" dan mag speler hele woord intypen als speler niet goede woord intypt print"helaas dat is niet het goede woord!"
functie break= als typ in break= stop spel

while loop:
	print"Letter"+print"of een ?"
	als letter fout maak galgje stap 1(aantal fouten meegeven)+schrijf letter op en
		print"Helaas, fout!"

	als speler iets anders dan 1 letter intypt dan geef foutmelding+ print"kies 1 letter"

	als letter goed schrijf letter op bij de streepjes en print"Goed geraden!"


	als galg stap 5 is klaar print"helaas je hangt aan de galg"+ print"woord
	als "?" intyp print"raad woord" als woord goed geraden print"goed geraden" anders 	print"fout ga door"
	als woord geraden print"Ja goed geraden"+print"woord"
	als woord geraden print"Je hebt 50 punten"+ begint nieuw spel met nieuw woord.






"""
