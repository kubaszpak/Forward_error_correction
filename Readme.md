# Forward error correction

<br>

### Piotr Łach 

### Jakub Szpak 

<br>
<br>

### Model symulacyjny zbudowano z pomocą języka Python. Zaimplementowano następujące klasy: 
- koder
- kanał
- dekoder

Koder ma za zadanie zakodowanie wiadomości wejściowej przez potrojenie każdego bitu. W związku z tym wysyłana wiadomość ma trzykrotnie większy rozmiar niż wiadomość wejściowa.

Kanał zakłóca przesyłaną wiadomość z prawdopodobieństwem wejściowym p. Zakłócenie polega na odwróceniu wartości bitu. 

Dekoder dekoduje odebraną wiadomość poprzez sprawdzenie każdej trójki bitów i wpisanie do zdekodowanej wiadomości wartości bitu występującego więcej razy. 





### Eksperyment nr 1:
 - Wygenerowano ciąg bitów wielkości 2^18 = 262144
 - Zakodowano go przez potrojenie każdego bitu
 - Ciąg umieszczono w symulatorze kanału transmisyjnego, który w zależności od prawdopodobieństwa p zamieniał bity w ciągu na przeciwne. Dobrano prawdopodobieństwa z przedziału [0;30]%
 - Otrzymano następujące wartości przekłamań:
  
  <br>

<div style="text-align:center"><img src="charts/3code/chart_1.png" /></div>


<br>
<br>

### Eksperyment nr 2:
 - Wygenerowano ciąg bitów wielkości 2^m, m in range [10,24]
 - Zakodowano go przez potrojenie każdego bitu
 - Ciąg umieszczono w symulatorze kanału transmisyjnego, który ze stałym prawdopodobieństwem 0,15 zamieniał bity w ciągu na przeciwne 
 - Otrzymano następujące wartości przekłamań

<br>


<div style="text-align:center"><img src="charts/3code/chart_2.png" /></div>

<br>
<br>



## Optymalizacja systemu 
System zoptymalizowano poprzez zastosowanie kodów BCH, zamiast stałego potrajania bitów. Zmodyfikowano koder i dekoder. W celu spełnienia założeń wykorzystaliśmy klasę BCHCode z biblioteki komm.




## Eksperymenty z kodami BCH

### Eksperyment pierwszy



W pierwszym z eksperymentów przygotowaliśmy słownik parametrów BCH dla m od 3 do 8. Każda jedna wartość na osi x to średnia z pomiarów dla każdej kombinacji parametrów. 

m - określa długość słowa kodowego n = 2^m - 1 <br>
t - zdolność korekcyjna <br>
k - długość pojedynczego pakietu

<br>

<div style="text-align:center"><img src="charts/bch/p0to20.png" /></div>

<br>

Przeprowadzając pomiar w ten sposób otrzymaliśmy mniejsze wartości błędów niż dla prostego kodu potrajającego.  

<br>

### Indywidualna analiza parametrów


Wykonano 10 eksperymentów wykorzystując różne parametry kodów na wiadomości o rozmiarze 2048b. Dla każdego z eksperymentów generowano nową populację dziesięciokrotnie. Wyniki są uśrednione. 

<br>

<div style="text-align:center"><img src="charts/bch/3_1_4.png" /></div>
<div style="text-align:center"><img src="charts/bch/4_2_27.png" /></div>
<div style="text-align:center"><img src="charts/bch/5_2_21.png" /></div>
<div style="text-align:center"><img src="charts/bch/5_5_11.png" /></div>
<div style="text-align:center"><img src="charts/bch/6_1_57.png" /></div>
<div style="text-align:center"><img src="charts/bch/6_15_7.png" /></div>
<div style="text-align:center"><img src="charts/bch/7_4_99.png" /></div>
<div style="text-align:center"><img src="charts/bch/7_21_29.png" /></div>
<div style="text-align:center"><img src="charts/bch/8_1_247.png" /></div>
<div style="text-align:center"><img src="charts/bch/8_63_9.png" /></div>







