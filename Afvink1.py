def main():
    try:
        bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        #bestand = "okeoke.txt"
        headers, seqs = lees_inhoud(bestand)
    
        zoekwoord = input("Geef een zoekwoord op: ")
    
        for index in range(len(headers)):                       #lees per header het bestand door
            if zoekwoord in headers[index]:                     #als het zoekwoord in de header zit, print de headers in de lijst
                print(headers[index])
                if zoekwoord not in headers[index]:
                    print("Zoekwoord staat niet in de headers") 
                if is_dna(seqs[index]):
                    print("sequence", index + 1, "is DNA")      #print dat het DNA is
                    knipt(seqs[index])                          #kijk of de enzymen knippen
                else:
                    print("het is geen dna")
    except KeyboardInterrupt:
        print("User interrupted")
def lees_inhoud(bestand):
    try:
        bestand = open(bestand)                             #open het bestand en maak 2 lege lijsten aan
    except IOError:
        print("Bestand niet gevonden")
    headers = []
    seqs = []
    sequentie = ''
    for line in bestand:                                    #voor elke lijn in het bestand, als de lijn begint met > , stop de header in de lijst headers.
        if line.startswith (">"):
            headers.append(line)
            if not sequentie == '':                         #als het niet begint met de header, stop de regels in de lijst sequenties.
                seqs.append(sequentie)
                sequentie = ''
        else:
            sequentie = sequentie + line.strip('\n')            
    seqs.append(sequentie)
        
    return headers, seqs                                    #return de gevonden lijsten

def is_dna(seq):
    for letter in seq:                                      #als in de sequentie A T G C er allemaal in zit, dan is het dna. anders niet
        if letter not in ['A','T','C','G']:
            return False
    return True
    

def knipt(seq):
    try:
        enzymen = open("enzymen.txt", 'r')                      #open het bestand van de restrictie enzymen
    except IOError:
        print("Bestand niet gevonden")
    for regel in enzymen:
        regel = regel.replace("^", "")
        regel = regel.replace("\n", "")
        enzyme, knip = regel.split()                        #haal de tekens er uit en splits de enzymnaam en de sequentie van elkaar
        if knip in seq:
            print(enzyme + " knipt in " + knip)             #print welk enzym knipt met welke sequentie

main()
