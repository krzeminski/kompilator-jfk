# kompilator-jfk
Celem projektu jest samodzielne zaprojektowanie bardzo prostego języka programowania i implementacja jego kompilatora. Projekt obejmuje wszystkie etapy przetwarzania kodu źrodłowego, aż do utworzenia kodu maszynowego. Należy wykorzystywać narzędzia wspomagające pracę twórcy kompilatora.

Przód kompilatora, czyli analiza leksykalno-składniowa powinna zostać wykonana przy pomocy generatora analizatorów ANTLR lub innych podobnych narzędzi. Z wynikowego drzewa AST należy wygenerować reprezentacje pośrednią (IR) w formie zgodnej ze specyfikacją LLVM. Optymalizacja reprezetacji pośredniej, a także generowanie kodu maszynowego wykonają narzędzie dostępne w LLVM. Wiedza niezbędna do realizacji projektu będzie szczegółowo i stopniowo omawiana na wykładzie.

Projekt podzielony jest na trzy etapach przy wykorzystaniu technologii ANTLR i LLVM. Jednak po wcześniejszym uzgodnieniu dopuszczalne jest realizowanie go zarówno w innym trybie jak i technologiach.

 

Etap 1: Proste operacje na zmiennych (15 pkt)
Wymagania minimalne (10 pkt):

obsługa dwóch typów zmiennych: całkowite, rzeczywiste,
podstawowa obsługa standardowego wejścia-wyjścia (np. polecenia read i print),
obsługa podstawowych operacji artmetycznych,
wskazywanie błędów podczas analizy leksykalno-składniowej﻿
Rozszerzenia:

obsługa zmiennych tablicowych (3 pkt)
obsługa macierzy liczb (5 pkt)
obsługa wartości logicznych (2pkt za AND, OR, XOR, NEG, 5p. jeżeli zaimplementowane zostanie short-circuit boolean evaluation)
obsługa liczb o różnej precyzji (np. Float32, Float64) (5 pkt)
obsługa typu ciąg znaków (string) (3 pkt)﻿
Etap 2: Sterowanie przepływem programu  (15 pkt)

Na końcową obronę projektu należy przynieść wydrukowany krótki podręcznik zaprojektowanego języka. Podręcznik powinien od strony użytkownika opisywać składnię języka, jego możliwości oraz ograniczenia.

Wymagania minimalne (10 pkt):

instrukcja warunkowe, pętla,
możliwość tworzenia funkcji,
obsługa zasięgu zmiennych (lokalne i globalne)
Proponowane rozszerzenia:

obsługa struktur (5 pkt)﻿
obsługa klas (5 pkt)
dynamiczne typowanie (wartości w pudełkach) (5 pkt)
funkcje-generatory (jak funkcje wykorzystujące yield w Python) (5 pkt)