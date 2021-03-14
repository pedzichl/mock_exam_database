Egzamin
Python i bazy danych – egzamin próbny.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki
Odpowiedzi na pytania programistyczne umieszczaj w odpowiednich plikach answer1.py – answer5.py

Powodzenia!
Zadanie 1 (3pkt)

Napisz skrypt (program) w Pythonie tworzący bazę danych.

    Powinien utworzyć bazę danych o nazwie exam2
    Powinien być odporny na błędy połączenia.
    Powinien poinformować użytkownika, jeśli taka baza danych już istnieje.

Rozwiązanie umieść w pliku answer1.py.
Zadanie 2 (5 pkt)

W bazie danych chcemy mieć następujące tabele:

* Users: id :

    autonumerowany (klucz główny),

    name : varchar(60),

    email : varchar(60),

    password : varchar(60)

* Messages:

    id : autonumerowany (klucz główny),

    user_id: int,

    message : text

* Items: id :

    autonumerowany (klucz główny),

    name : varchar(40),

    description : text,

    price : decimal(7,2)

* Orders: id :

    autonumerowany (klucz główny),

    description : text

Zajrzyj do pliku answer2.py, znajdziesz tam zdefiniowane zmienne: query_1, query_2 ... query_9. W zmiennych umieść następujące zapytania SQL:

    query_1: Tworzące tabelę Users (email ma być unikatowy).
    query_2: Tworzące tabelę Messages (pamiętaj o relacji jeden do wielu z tabelą Users).
    query_3: Tworzące tabelę Items.
    query_4: Tworzące tabelę Orders.
    query_5: Stworzenie relacji wiele do wielu między tabelami Items a Orders (tabela ma się nazywać ItemsOrders, a pola relacji item_id i order_id).
    query_6: Wybranie wszystkich przedmiotów (Item) o cenie większej niż 13.
    query_7: Włożenie do tabeli Orders nowego zamówienia o opisie "przykładowy opis".
    query_8: Usuniecie użytkownika o id 7.
    query_9: Wybranie wszystkich użytkowników z tabeli Users, którzy mają przypisaną jakąś wiadomość w tabeli Messages.
    query_10: Dodanie do tabeli Messages pola date_of_created, przechowującego datę utworzenia wiadomości. Powinno być uzupełniane automatycznie podczas dodawania wiersza do bazy. Może przyjmować wartość null (dla wiadomości wpisanych do bazy, przed jego dodaniem.)

Za każde zapytanie przysługuje pół punktu.

Uwaga 1: Podczas pisania zapytań nie używaj nazwy bazy danych w zapytaniu. Uwaga 2: Pilnuj dokładności nazw tabel i pól oraz typów danych!
Zadanie 3 (3pkt)

Napisz generator dividers, który przyjmie jeden argument number. Generator powinien generować kolejne dzielniki liczby przekazanej jako argument.
Przykład użycia:

for i in dividers(6):

    print(i)

Wynik:

1

2

3

6

Rozwiązanie umieść w pliku answer3.py.
Zadanie 4 (4pkt)

Używając frameworka Flask, napisz stronę udostępnioną pod adresem /add_product, która spełni następujące założenia:

    Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
        name: nazwę produktu,
        description: opis produktu,
        price: cenę produktu.

    Pamiętaj: nazwij pola dokładnie tak, jak w poleceniu (ustaw odpowiednio atrybut name tagu <input>)

    Po wejściu metodą POST:
        zweryfikuje poprawność danych,
        zapisze te dane do bazy danych do tabeli Items (tabela taka sama jak w zadaniu 1) i wyświetli komunikat Product added!,
        jeśli którakolwiek wartość będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat: Invalid data!.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu. Rozwiązanie umieść w pliku answer4.py.
Zadanie 5 (5pkt)

Napisz w Pythonie klasę VIPUser. Klasa ma spełniać następujące właściwości:

    Dziedziczyć po klasie User (zajrzyj do modułu exam_lib) oraz mieć dodatkowy atrybut: _vip_card_number. Atrybut ten nie powinien być dostępny na zewnątrz klasy (pamiętaj o odpowiedniej konwencji nazw).

    Mieć metodę __init__, która przyjmuje następujące dane:
        imię,
        nazwisko,
        mail,
        numer karty VIP. Imię, nazwisko i mail mają być przekazywane do odpowiedniej metody klasy nadrzędnej. Metoda ta ma sprawdzać, czy podany numer jest prawidłowy.
        Jeżeli jest – to go nastawiać.
        Jeżeli nie – to numer ma być nastawiony na None.

    Mieć metodę statyczną _check_card(new_number) – numer jest prawidłowy, jeżeli:
        jest większy niż 999,
        podzielny przez 2. Metoda ma zwracać wartość logiczną. Metoda nie powinna być dostępna z zewnątrz klasy.

    Mieć metodę statyczną use_vip_card() – ciało metody może zostać puste (lub zwrócić wartość None).

    Mieć setter i getter (@property) dla atrybutu _vip_card_number.
        Setter ma nastawiać zmienną _vip_card_number (jeżeli podany nowy numer spełnia założenia).
        Getter (property) ma po prostu zwrócić wartość atrybutu.

Rozwiązanie zadania umieść w pliku answer5.py.
