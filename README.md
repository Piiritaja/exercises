# Readability index

Ülesandeks on koostada programm, mis arvutab raamatu loetavuse indeksi.

Kõik raamatud on antud ülesandes .txt laiendiga.

Raamatu loetavuse hindamiseks kasutame Coleman–Liau indeksit. See indeks ütleb meile millise klassi õpilase jaoks raamat sobilik on.

Indeksit arvutatakse sellise valemiga:
I = 0.588L -0.296S -15.8,


kus L = keskmine tähtede arv 100 sõna kohta
    , S = keskmine lausete arv 100 sõna kohta

## Mall
[Mall](mall.py)

## Funktsioonid, mida realiseerida

### read_file(file_path)
Saab sisendiks faili(siin ülesandes on failiks raamatud .txt kujul), ning tagastab faili sisu stringina

### replace_word(file_path, word_to_replace, word_to_replace_with)
Saab sisendiks faili, mida muuta, sõna, mida asendada ning asendussõna.

Funktsioon asendab failis iga 'word_to_replace' sõne 'word_to_replace_with' sõnega.

Funktsioon peab looma vanast failist koopia, kujul '[faili nimi]_old.txt'.

### roll_back(file_path)
Saab sisendiks faili, mis eelmisele versioonile tagasi viia ('..._old.txt' faili sisule).

Kui '..._old.txt' faili ei eksisteeri, siis kustutatakse faili sisu. Tulemuseks tühi fail.

Peale vana sisu taastamist '..._old.txt' fail kustutatakse.

### count_occurrences(file_path, word)
Leiab mitu korda, ette antud failis otsitav sõna esineb.

### count words(file_path)
Leiab sõnade arvu failis.

### count_sentences(file_path)
Leiab lausete arvu failis.

Iga lause algab tühiku või uue reaga ja suure algustähega.

Koosta regex, mis loeks laused kokku. Abiks:

Lauses võivad olla mõttekohad: "..."

Lauses võivad olla numbrid: "2. september on tore päev!"

### get_paragraphs(file_path)
Saab sisendiks faili, ning leiab selle raamatu(sisendfaili) peatükid.

Kõik peatükkid on failis eraldi real ning on kujul:

'[Number]. [pealkiri]'

Tagastada list kõikidest pealkirjadest samal kujul. Näiteks:

>1. Algus

>See lugu algas ootamatult.

>Väga ootamatult.


>2. Lõpp

>Lugu lõppes ootamatult.


Väljundiks oleks: ['1. Algus','2. Lõpp']

kasuta regexit!

### readability(book_path,file_path)
Arvutab raamatu loetavuse, kasutades eelnevalt tutvustatud valemit.

Tagastab vastuse täisarvuna, mis on ümardatud alla.

### add_book(book_path,file_path)
Lisab raamatu(book_path) ette antud faili(file_path), milles on raamatute loetavuse indeksid.

Kui faili ei ole tuleb see fail luua.

Kui fail on olemas tuleb lisada faili lõppu uus rida ette antud raamatu kohta.

Kui fail on olemas aga sama nimega raamat on juba failis, tuleb uuendada selle raamatu loetavuse indeksit.

Failis on raamatud kujul '[raamatu pealkiri]: [arvutatud loetavuse indeks]. grade'

Kui loetavuse indeks tuleb miinusmärgiga, asendame indeksi nulliga.

Kui loetavuse indeks on rohkem kui 12 on raamat failis kujul: '[raamatu pealkiri]: not a children's book'

Raamatu nimi on faili nimi. Näiteks 'raamatud/Tõde ja Õigus.txt', pealkiri on 'Tõde ja Õigus'. 

Faili nimi võib sisaldada tühikuid.

### add_books(books_folder,file_path)
Lisab kõik raamatud ette antud kaustas, raamatute loetavuse indeksi faili.

Raamatu lisamise põhimõte sama, mis add_book funktsioonil.

Kaustas võib ka olla faile, mis ei ole raamatud.

Näiteks sellises kaustas:

>  'Tõde ja Õigus.txt'
>  
>  'Tõde ja Õigus.txt.old'
>  
>  'eksmat_avaldus.dox'
>  
>  'Püüton.txt'
  
On ainult 2 raamatut: 'Tõde ja Õigus.txt' ja 'Püüton.txt'
