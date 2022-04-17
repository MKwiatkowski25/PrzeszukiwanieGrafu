import random

## Input

while True:
    try:
        liczba_tarasów = int(input("Podaj liczbę tarasów: "))
        liczba_ścieżek = int(input("Podaj liczbę ścieżek: "))
        numer_wybranego_tarasu = int(input("Podaj numer tarasu, do którego chce się dostać Bajtazar: "))
        liczba_bajtalarów = int(input("Podaj liczbę bajtalarów, którymi dysponuje: "))
    except:
        print("Podano niewłaściwe dane - powinny to być liczby całkowite" )
        continue
    if liczba_tarasów < 0 or liczba_tarasów> 100 or numer_wybranego_tarasu>liczba_tarasów or liczba_bajtalarów <= 0 or liczba_ścieżek<= 0 or liczba_ścieżek > 300 or liczba_ścieżek > liczba_tarasów*(liczba_tarasów - 1)/2:
        raise ValueError("Dane poza zakresem!")
    break



## Generowanie danych

ścieżki = [0] * int(liczba_tarasów*(liczba_tarasów-1)/2)
licznik = 0
for i in range(1,liczba_tarasów+1):
    for j in range(i+1,liczba_tarasów+1):
        ścieżki[licznik] = (i,j)
        licznik+=1


wybrane_ścieżki = random.sample(ścieżki, liczba_ścieżek)

## Dane (przykładowe listy krawędzi, które sobie zapisałem) :
#wybrane_ścieżki = [(2, 14), (2, 20), (6, 15), (2, 12), (7, 12), (2, 16), (7, 20), (7, 15), (10, 12), (12, 18), (7, 17), (18, 19), (8, 19), (8, 14), (9, 14), (1, 20), (5, 7), (6, 16), (4, 10), (8, 11), (1, 19), (14, 18), (13, 19), (4, 16), (6, 19), (5, 12), (13, 20), (19, 20), (1, 8), (5, 17), (4, 11), (1, 15), (3, 9), (6, 18), (5, 20)]
#wybrane_ścieżki = [(5, 6), (2, 3), (2, 4), (1, 6), (2, 6), (4, 7), (2, 7), (3, 7), (3, 6), (4, 5)]
#wybrane_ścieżki = [(6, 10), (3, 10), (3, 9), (2, 5), (7, 8), (5, 8), (1, 2), (6, 8), (1, 4), (1, 10), (6, 9), (2, 6)]
print(f"Losowo wybrane ścieżki między tarasami: \n{wybrane_ścieżki}")


def stwórz_macierz_incydencji(rozmiar, lista_krawędzi):   #
    M = [[2 ** 10] * rozmiar for i in range(rozmiar)]
    for j in lista_krawędzi:
        M[j[0]-1][j[1]-1] = j[1]
        M[j[1]-1][j[0]-1] = j[0]
    return M

l = stwórz_macierz_incydencji(liczba_tarasów,wybrane_ścieżki)


źródło = 1

D = [[0,0] for i in range(liczba_tarasów)]
for i in range(liczba_tarasów):
    D[źródło-1] = [0,źródło]
    D[i][0] = l[źródło - 1][i]
    if l[źródło-1][i] < 2**10:
        D[i][1] = źródło



NS = [0] * (liczba_tarasów-1)

for i in range(liczba_tarasów-1):
    NS[i] = i+2

## Algorytm Dijkstry
i = 1
while NS:
    mindist = 2**10
    for w in NS:
        if D[w-1][0] < mindist:
            v = w
            mindist = D[w-1][0]
    NS.remove(v)
    i+=1
    for w in NS:
        if D[w-1][0] > mindist + l[v-1][w-1]:
            D[w-1][0] = mindist + l[v-1][w-1]
            D[w-1][1] = v

for d in D:
    d[0]+=1

print(f"Lista reprezentująca koszt trasy ze źródła do konkretnego tarasu i numer poprzednika na ścieżce: \n{D}")

## Najkrótsza ścieżka do wybranego tarasu:

Trasa = [0]*liczba_tarasów
Trasa[0] = numer_wybranego_tarasu
punkt_trasy = D[numer_wybranego_tarasu-1][1]
Trasa[1] = punkt_trasy
licznik = 1

while punkt_trasy != 1:
    punkt_trasy = D[punkt_trasy-1][1]
    Trasa[licznik+1] = punkt_trasy
    licznik+=1

Trasa_od_startu = [0] * (licznik+1)
for i in range(licznik+1):
    Trasa_od_startu[i] = Trasa[licznik-i]

## Koszt, czy starczy bajtalarów

Koszt_trasy = D[numer_wybranego_tarasu-1][0]
czy_wystarczy_bajtalarów = "tak"
if liczba_bajtalarów < Koszt_trasy:
    czy_wystarczy_bajtalarów = "nie"

## Rezultaty:
print(f"Najtańsza droga do tarasu nr {numer_wybranego_tarasu} to: {Trasa_od_startu}. \nJej koszt to {Koszt_trasy} Bajtalarów \nCzy Bajtazarowi wystarczy bajtalarów na trasę: {czy_wystarczy_bajtalarów}")




