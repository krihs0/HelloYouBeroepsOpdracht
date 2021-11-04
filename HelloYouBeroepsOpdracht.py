import os
import time

def cls():
    os.system("cls")

def einde():
    print("Het lijkt erop dat je het niet hebt overleefd")
    print("")
    replay()

def a1():
    cls()
    print("De oorlog in Irak breekt uit en het is niet meer veilig om naar school te gaan.")
    time.sleep(1)
    print("A: Blijf naar school gaan")
    print("B: Je stop met naar school gaan")
    answera1 = input("Type A/B: ")
    if answera1 == "a" or answera1 == "A":
        cls()
        a11()
    elif answera1 == "b" or answera1 == "B":
        cls()
        a12()

def a11():
    print("Terwijl je op school zit gaat de politie je school controleren.")
    time.sleep(1)
    print("A: Blijf in de klas zitten")
    print("B: Ga weg door een achteruitgang")
    answera11 = input("Type A/B: ")
    if answera11 == "a" or answera11 == "A":
        cls()
        print("Omdat je in de klas blijft zitten vindt de politie je en zet je in een jezidi kamp waar je uiteindelijk verhongert.")
        time.sleep(3)
        einde()
    elif answera11 == "b" or answera11 == "B":
        cls()
        print("Je bent netaan onstsnapt en bent nu veilig thuis.")
        time.sleep(3)
        a2()
        
def a12():
    print("Je blijft veilig thuis want je denkt niet dat de school veilig is.")
    time.sleep(1)
    a2()
    

def a2():
    print("Je ouders hebben gezorgt dat je thuis geschoold word.")
    time.sleep(4)
    cls()
    a3()

def a3():
    print("Het wordt veel te gevaarlijk in Irak.")
    print("A: Vlucht")
    print("B: Duik onder")
    answera3 = input("Type A/B: ")
    if answera3 == "a" or answera3 == "A":
        cls()
        print("Waar wil je naartoe vluchten?")
        print("A: Syrie")
        print("B: Turkije")
        answera31 = input("Type A/B: ")
        if answera31 == "a" or answera31 == "A":
            print("Je vlucht naar syrie, maar Syrie wilt je niet dus stuurt je door naar Turkije")
            time.sleep(4)
            cls()
            a6()
        elif answera31 == "b" or answera31 == "B":
            print("Je vlucht naar turkije")
            time.sleep(2)
            cls()
            a6()
    elif answera3 == "b" or answera3 == "B":
        cls()
        print("Waar wil je onderduiken?")
        print("A: Het verzet")
        print("B: Je eigen huis")
        answera32 = input("Type A/B: ")
        if answera32 == "a" or answera32 == "A":
            cls()
            print("Het verzet vraagt of je kan helpen met wat spullen dragen")
            print("A: Help niet")
            print("B: Help")
            answera321 = input("Type A/B: ")
            if answera321 == "a" or answera321 == "A":
                cls()
                print("Je dacht dat binnen blijven veiliger was maar de politie valt het zerzet binnen en iedereen beland in een jezidikamp")
                print("A: Probeer gelijk te ontsnappen")
                print("B: Probeer een bewaker te bevrienden")
                answer4 = input("Type A/B: ")
                if answer4 == "a" or answer4 == "A":
                    cls()
                    print("Het ontsnappen gaat niet zoals plan en het loopt niet goed af")
                    time.sleep(3)
                    einde()
                if answer4 == "b" or answer4 == "B":
                    cls()
                    print("Je hebt een bewaker bevriend en de bewaker helpt je te ontsnappen")
                    time.sleep(3)
                    a51()

            if answera321 == "b" or answera321 == "B":
                cls()
                print("Je bent mee naar buiten te gaan om te helpen, als je terugkomt is alles een rotzooi en is er niemand meer")
                time.sleep(3)
                a51()
        elif answera32 == "B" or answera32 == "B":
            cls()
            print("Het leek een goed idee maar de politie vindt jullie en jullie verhingeren in een jezidikamp")
            einde()

def a51():
    print("Er is geen andere optie dan te vluchten, het verzet heeft geregeld dat alle overgebleven mensen naar nederland kunnen")
    time.sleep(5)
    a7()

def a6():
    print("In Turkije wordt gezegd dat het in nederland goed is")
    print("A: Blijf in Tukrije")
    print("B: Ga naar Nederland")
    answera6 = input("Type A/B: ")
    if answera6 == "a" or answera6 == "A":
        cls()
        print("Je bent in turkije gebleven. Je woont daar nu 3 jaar maar de werk en leef-omstandigheden zijn te slecht dus jullie besluiten toch naar nederland te gaan")
        time.sleep(5)
        a7()
    if answera6 == "b" or answera6 == "B":
        cls()
        a7()

def a7():
    cls()
    print("In nederland is het veilig, jullie, krijgen onderdak je ouders krijgen een goede baan en je kan naar een normale school ")
    print("")
    replay()

def replay():
    print("Wil je dit programma nog een keer doen?")
    answerreplay = input("Type Y/N: ")
    if answerreplay == "y" or answerreplay == "Y":
        a1()
    if answerreplay == "n" or answerreplay == "N":
        print("Goodbye!")
        time.sleep(2)
        exit()

while True:
    a1()
    