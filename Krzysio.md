Cześć! Super, że się za to zabierasz. Masz rację – te kolokwia opierają się na powtarzalnych schematach. Jeśli zrozumiesz algorytm dla każdego z 5 zadań, bez problemu zdasz, niezależnie od tego, jakie liczby prowadzący wstawi. 

Przygotowałem dla Ciebie **kompleksowy przewodnik od absolutnych podstaw**. Będziemy omawiać zadania typami (od 1 do 5). Dla każdego typu najpierw wyjaśnię "na chłopski rozum" o co chodzi i podam przepis (kroki), a potem rozwiążę po 2-3 różne wersje tego zadania z Twoich zdjęć, żebyś zobaczył, jak to działa w praktyce. Na samym końcu znajdziesz kod LaTeX z gotową ściągawką.

Zaczynamy!

---

### ZADANIE 1: Prawdopodobieństwo warunkowe (rzuty kilkoma kostkami)

**O co w tym chodzi?**
Prawdopodobieństwo klasyczne to stosunek tego "co chcemy" (wyniki sprzyjające) do "wszystkiego co możliwe" (wszystkie wyniki). Prawdopodobieństwo **warunkowe** to sytuacja, w której "ktoś z góry daje Ci podpowiedź". Nasza pula "wszystkiego co możliwe" się kurczy do tych wyników, które spełniają warunek.

**Kroki postępowania:**
1. **Oznacz zdarzenia:** $A$ to zdarzenie, którego szukamy (np. suma oczek = 6). $B$ to nasz **warunek** (podpowiedź, np. wiemy, że maksimum to 3).
2. **Znajdź moc warunku $|B|$:** Wypisz lub policz, na ile sposobów może zajść sama podpowiedź (warunek). Z reguły łatwiej wypisać wyniki na palcach, jeśli nie ma ich dużo.
3. **Znajdź moc części wspólnej $|A \cap B|$:** Wypisz te zdarzenia, które spełniają OBA kryteria naraz (np. suma to 6 ORAZ maksimum to 3).
4. **Podziel:** Ostateczny wynik to $P(A|B) = \frac{|A \cap B|}{|B|}$. Pamiętaj, nie musisz tu wcale liczyć ułamków z wielkich prawdopodobieństw, wystarczy podzielić liczbę zdarzeń pasujących przez liczbę zdarzeń warunku!

#### Wersja A: Rzut 3 kostkami czworościennymi (3k4). Szukamy sumy 6, warunek: maksimum z wyników to 3.
**Krok 1:** $A$ - suma to 6, $B$ - największa wyrzucona liczba to 3. Kostki k4 mają ścianki $\{1, 2, 3, 4\}$.
**Krok 2: Szukamy $|B|$.** Maksymalny wynik to 3. To znaczy, że rzucamy tylko liczbami $\{1, 2, 3\}$, ale **przynajmniej raz musi wypaść trójka** (inaczej maksimum byłoby mniejsze). Wszystkich możliwych rzutów liczbami 1, 2, 3 na trzech kostkach jest $3 \cdot 3 \cdot 3 = 27$. Odejmujemy od tego rzuty, gdzie nie ma żadnej trójki (czyli rzuty tylko 1 i 2, a jest ich $2 \cdot 2 \cdot 2 = 8$). Zatem wyników, gdzie maksimum to dokładnie 3, jest $|B| = 27 - 8 = 19$.
**Krok 3: Szukamy $|A \cap B|$.** Szukamy takich rzutów, których suma to 6 ORAZ największa liczba to 3. Skoro największa to 3, to nasza suma wygląda tak: $3 + \text{kostka\_2} + \text{kostka\_3} = 6$. Z tego wynika, że dwie pozostałe kostki muszą dać w sumie 3. Jak można uzyskać sumę 3 z dwóch kostek? Tylko rzucając $1$ i $2$ (albo $2$ i $1$). 
Więc pasujące zestawy to zbiór liczb $\{1, 2, 3\}$. Na ile sposobów mogą ułożyć się na trzech kostkach? (To permutacje: 1-2-3, 1-3-2, 2-1-3, 2-3-1, 3-1-2, 3-2-1). Jest ich dokładnie 6. Zatem $|A \cap B| = 6$.
**Krok 4: Wynik.** $P(A|B) = \frac{6}{19}$.

#### Wersja B: Rzut 3 kostkami sześciennymi (3k6). Szukamy sumy 7, warunek: na przynajmniej jednej kostce wypadło 2.
**Krok 1:** $A$ - suma 7, $B$ - wypadła co najmniej jedna dwójka.
**Krok 2: Szukamy $|B|$.** Łatwiej policzyć zdarzenie przeciwne: "nie wypadła żadna dwójka". Zwykły rzut to $6^3 = 216$ opcji. Brak dwójek (rzucamy resztą z 5 liczb) to $5^3 = 125$ opcji. Więc rzutów z co najmniej jedną dwójką jest $|B| = 216 - 125 = 91$.
**Krok 3: Szukamy $|A \cap B|$.** Szukamy: suma wynosi 7 ORAZ mamy chociaż jedną dwójkę. Mamy 3 kostki: $2 + \text{k2} + \text{k3} = 7$, więc pozostałe dwie muszą dać sumę 5.
Z czego zrobimy 5 na dwóch kostkach?
Z $1+4$ (oraz $4+1$) $\rightarrow$ mamy trójki liczb: (2, 1, 4), (2, 4, 1), (1, 2, 4), (4, 2, 1), (1, 4, 2), (4, 1, 2) $\rightarrow$ 6 możliwości.
Z $2+3$ (oraz $3+2$) $\rightarrow$ mamy trójki liczb z dwiema dwójkami!: (2, 2, 3), (2, 3, 2), (3, 2, 2) $\rightarrow$ 3 możliwości.
Więcej opcji na sumę 5 na dwóch kostkach nie ma. Razem $|A \cap B| = 6 + 3 = 9$.
**Krok 4: Wynik.** $P(A|B) = \frac{9}{91}$.

---

### ZADANIE 2: Drzewka, Wzór Bayesa (losowanie kostki i rzut)

**O co w tym chodzi?**
Znasz skutek, szukasz przyczyny. Kolega rzucił kostką i mówi Ci "Wypadło 2!". Chcesz odgadnąć, **którą z dwóch kostek** rzucił. To klasyczne zadanie na tzw. Twierdzenie Bayesa. Najłatwiej rozwiązać to rysując "drzewko" albo stosując wzór na proporcje: liczymy prawdopodobieństwo "naszej" gałęzi (tej o którą pyta zadanie) i dzielimy przez sumę wszystkich gałęzi, na których wystąpił ten sam wynik (tu: wyrzucenie "2").

**Kroki postępowania:**
1. **Oznacz zdarzenia (hipotezy):** Np. $H_1$ to wylosowanie pierwszej kostki, $H_2$ to drugiej. Określ ich szanse (często po 50%, ale czasem inne).
2. **Oznacz skutek $S$:** Np. wyrzucenie liczby 2.
3. **Oblicz szanse na skutek z każdej kostki:** $P(S|H_1)$ (szansa na wynik jeśli rzucono pierwszą) i $P(S|H_2)$.
4. **Złóż to do wzoru (Prawdopodobieństwo całkowite - mianownik):** Suma gałęzi dających nasz wynik to $P(S) = P(H_1) \cdot P(S|H_1) + P(H_2) \cdot P(S|H_2)$.
5. **Wzór Bayesa:** Podziel interesującą Cię gałąź przez sumę. $P(H_1|S) = \frac{\text{Interesująca gałąź}}{\text{Suma gałęzi (Mianownik z punktu 4)}}$.

#### Wersja A: k4 (szansa 2/3) lub k6 (szansa 1/3). Wypadło 2. Szansa, że to k4?
**Krok 1:** Wybór kostki: $P(k4) = \frac{2}{3}$, $P(k6) = \frac{1}{3}$.
**Krok 2 & 3:** Skutek to wypadnięcie "2". 
Jeśli mamy k4 (ścianki 1,2,3,4), szansa na 2 wynosi: $P(2|k4) = \frac{1}{4}$.
Jeśli mamy k6 (ścianki 1..6), szansa na 2 wynosi: $P(2|k6) = \frac{1}{6}$.
**Krok 4 (Mianownik):** Prawdopodobieństwo, że W OGÓLE wypadnie 2.
$P(2) = (\text{szansa na k4} \cdot \text{szansa na 2 z k4}) + (\text{szansa na k6} \cdot \text{szansa na 2 z k6})$
$P(2) = \left(\frac{2}{3} \cdot \frac{1}{4}\right) + \left(\frac{1}{3} \cdot \frac{1}{6}\right) = \frac{2}{12} + \frac{1}{18} = \frac{1}{6} + \frac{1}{18} = \frac{3}{18} + \frac{1}{18} = \frac{4}{18} = \frac{2}{9}$.
**Krok 5 (Wynik):** Pytają o k4. Bierzemy kawałek równania dotyczący k4 (z mianownika) i dzielimy przez cały mianownik.
$P(k4|2) = \frac{\frac{2}{3} \cdot \frac{1}{4}}{\frac{2}{9}} = \frac{\frac{2}{12}}{\frac{2}{9}} = \frac{1}{6} \cdot \frac{9}{2} = \frac{9}{12} = \frac{3}{4}$. Odpowiedź: 3/4.

#### Wersja B: k6 (szansa 1/2) lub k8 (szansa 1/2). Wypadła liczba > 4. Szansa, że to k6?
**Krok 1:** Wybór: $P(k6) = \frac{1}{2}$, $P(k8) = \frac{1}{2}$.
**Krok 2 & 3:** Skutek to wynik $> 4$.
Dla k6 (wyniki 5, 6): $P(>4 | k6) = \frac{2}{6} = \frac{1}{3}$.
Dla k8 (wyniki 5, 6, 7, 8): $P(>4 | k8) = \frac{4}{8} = \frac{1}{2}$.
**Krok 4 (Mianownik):** 
$P(>4) = \left(\frac{1}{2} \cdot \frac{1}{3}\right) + \left(\frac{1}{2} \cdot \frac{1}{2}\right) = \frac{1}{6} + \frac{1}{4} = \frac{2}{12} + \frac{3}{12} = \frac{5}{12}$.
**Krok 5 (Wynik):** Pytają o k6.
$P(k6 | >4) = \frac{\frac{1}{2} \cdot \frac{1}{3}}{\frac{5}{12}} = \frac{\frac{1}{6}}{\frac{5}{12}} = \frac{1}{6} \cdot \frac{12}{5} = \frac{2}{5}$. Odpowiedź: 2/5.

---

### ZADANIE 3: Niezależność zdarzeń

**O co w tym chodzi?**
Dwa zdarzenia są niezależne, jeśli wiedza o tym, że zaszło jedno, nie zmienia szansy na to, że zajdzie drugie. Matematycznie sprawdza się to bardzo prostym testem (równaniem). Musisz sprawdzić, czy lewa strona równa się prawej.
Wzór-test: **Czy $P(A) \cdot P(B) = P(A \cap B)$?** Jeśli tak, są niezależne. Jeśli nie, są zależne.

**Kroki postępowania:**
1. Zdefiniuj ile jest wszystkich możliwości $|\Omega|$ (np. rzut kostką 12-ścienną to 12 opcji).
2. Wypisz wyniki dla zdarzenia $A$, policz je ($|A|$) i oblicz $P(A) = \frac{|A|}{|\Omega|}$.
3. Wypisz wyniki dla zdarzenia $B$, policz je ($|B|$) i oblicz $P(B) = \frac{|B|}{|\Omega|}$.
4. Znajdź część wspólną $A \cap B$ (wyniki, które są OBU listach), policz je i oblicz $P(A \cap B)$.
5. Wstaw do wzoru $P(A) \cdot P(B)$ i sprawdź czy wyjdzie to samo co $P(A \cap B)$.

#### Wersja A: Rzut kostką 12-ścienną (1k12). $A$ - liczba podzielna przez 2, $B$ - podzielna przez 4.
**Krok 1:** Zbiór wyników to $\{1, 2, ..., 12\}$. $|\Omega| = 12$.
**Krok 2 ($A$):** Liczby podzielne przez 2: $A = \{2, 4, 6, 8, 10, 12\}$. Jest ich 6. Więc $P(A) = \frac{6}{12} = \frac{1}{2}$.
**Krok 3 ($B$):** Liczby podzielne przez 4: $B = \{4, 8, 12\}$. Jest ich 3. Więc $P(B) = \frac{3}{12} = \frac{1}{4}$.
**Krok 4 (Część wspólna):** Liczby z $A$, które są też w $B$ to $\{4, 8, 12\}$ (czyli liczby podzielne i przez 2 i przez 4 to po prostu te podzielne przez 4). Jest ich 3. Zatem $P(A \cap B) = \frac{3}{12} = \frac{1}{4}$.
**Krok 5 (Test):** Sprawdzamy czy $P(A) \cdot P(B) = P(A \cap B)$.
Lewa strona: $\frac{1}{2} \cdot \frac{1}{4} = \frac{1}{8}$.
Prawa strona: $\frac{1}{4}$.
$\frac{1}{8} \neq \frac{1}{4}$.
**Odpowiedź:** Nie, nie są niezależne (są zależne).

#### Wersja B: Rzut kostką 20-ścienną (1k20). $A$ - podzielne przez 4, $B$ - podzielne przez 3.
**Krok 1:** $|\Omega| = 20$.
**Krok 2 ($A$):** Podzielne przez 4 z zakresu 1-20: $\{4, 8, 12, 16, 20\}$. Jest ich 5. $P(A) = \frac{5}{20} = \frac{1}{4}$.
**Krok 3 ($B$):** Podzielne przez 3 z zakresu 1-20: $\{3, 6, 9, 12, 15, 18\}$. Jest ich 6. $P(B) = \frac{6}{20} = \frac{3}{10}$.
**Krok 4 (Część wspólna):** Podzielne przez 4 i przez 3 (czyli przez 12): to tylko liczba $\{12\}$. Jest 1 taka liczba. $P(A \cap B) = \frac{1}{20}$.
**Krok 5 (Test):** Lewa: $\frac{1}{4} \cdot \frac{3}{10} = \frac{3}{40}$. Prawa: $\frac{1}{20} = \frac{2}{40}$.
$\frac{3}{40} \neq \frac{2}{40}$.
**Odpowiedź:** Nie są niezależne.

---

### ZADANIE 4: Prawdopodobieństwo geometryczne

**O co w tym chodzi?**
Wyobraź sobie, że rzucasz rzutką w planszę z zamkniętymi oczami i zawsze trafiasz wewnątrz. Plansza to obszar $\Omega$. Pytają Cię, jaka jest szansa na trafienie w konkretny, zamazany na kolorowo kawałek tej planszy (obszar $A$). Szansa to nic innego jak matematyczny stosunek pól figur: $\frac{\text{Pole Zamazane}}{\text{Pole Całej Planszy}}$.

**Kroki postępowania:**
1. Narysuj układ współrzędnych i zaznacz figurę podaną w zadaniu (prostokąt, trójkąt).
2. Oblicz jej pole ($|\Omega|$) ze zwykłych wzorów z podstawówki ($a \cdot b$, $\frac{a \cdot h}{2}$).
3. Zaznacz na rysunku warunek (nierówność). Narysuj linię (np. parabolę $y=x^2$) i zakreśl to, co jest nad/pod nią zgodnie ze znakiem nierówności, ale TYLKO wewnątrz naszej figury.
4. Oblicz pole zakreślonej części ($|A|$). Czasem to zwykły trójkąt, a czasem trzeba policzyć prostą całkę oznaczoną.
5. Wynik to $|A| / |\Omega|$.

#### Wersja A: Punkt z prostokąta $(0,0), (0,2), (1,0), (1,2)$. Warunek: $y > x^2$.
**Krok 1 & 2:** Nasza plansza to prostokąt, który na osi X ma długość 1 (od 0 do 1), a na osi Y wysokość 2 (od 0 do 2). Jego Pole $|\Omega| = 1 \cdot 2 = 2$.
**Krok 3:** Rysujemy linię $y = x^2$ (to parabola startująca z $(0,0)$, przechodząca przez $(1,1)$). Nierówność to $y > x^2$, czyli interesuje nas obszar NAD parabolą, ale zamykający się w naszym prostokącie.
**Krok 4:** Jak policzyć pole nad parabolą w naszym prostokącie? Cały prostokąt jest od $x=0$ do $x=1$ i pod dachem do $y=2$. Pole NAD krzywą w tym prostokącie najłatwiej policzyć odejmując pole POD krzywą od całego obszaru (od prostokąta, ale uwaga - parabola ma wartość od 0 do 1 dla x w zakresie 0..1, a nasz prostokąt sięga do y=2. Najbezpieczniej posłużyć się całką całego tego obszaru. Obszar ten z góry ogranicza $y=2$, a z dołu parabola $y=x^2$, od lewej do prawej $x \in [0, 1]$.
Pole $A = \int_{0}^{1} (\text{górna linia} - \text{dolna linia}) \,dx = \int_{0}^{1} (2 - x^2) \,dx$.
Liczymy prostą całkę: z $2$ to $2x$, z $x^2$ to $\frac{x^3}{3}$.
Wstawiamy granice 0 i 1: $\left(2(1) - \frac{1^3}{3}\right) - (0 - 0) = 2 - \frac{1}{3} = \frac{5}{3}$. To jest pole $|A|$.
**Krok 5:** $P(A) = \frac{\text{Pole } A}{\text{Pole } \Omega} = \frac{\frac{5}{3}}{2} = \frac{5}{6}$. Odpowiedź: 5/6.

#### Wersja B: Punkt z trójkąta $(0,0), (2,0), (0,1)$. Warunek $y < x/2$.
**Krok 1 & 2:** Trójkąt o podstawie na osi X długości 2 (od 0 do 2) i wysokości na osi Y równej 1. Pole trójkąta $|\Omega| = \frac{1}{2} \cdot a \cdot h = \frac{1}{2} \cdot 2 \cdot 1 = 1$.
*(Uwaga, przeciwprostokątną trójkąta opisuje funkcja liniowa od punktu $(0,1)$ do $(2,0)$. Jej wzór to $y = -\frac{1}{2}x + 1$)*.
**Krok 3:** Warunek to $y < \frac{x}{2}$. Granicą jest prosta $y = \frac{1}{2}x$. Chcemy obszar POD tą prostą. Musimy sprawdzić, gdzie te dwie proste się przecinają: $-\frac{1}{2}x + 1 = \frac{1}{2}x \implies 1 = x$. Skoro przetną się w $x=1$, to dla obszaru pod prostą $y = \frac{1}{2}x$ wewnątrz trójkąta stworzą się dwie strefy. Ale chwila, narysuj to. Trójkąt i przecinająca go z $(0,0)$ linia lekko wznosząca się w górę. Szukamy obszaru POD nią.
To trójkąt, który ma wierzchołki $(0,0)$, $(2,0)$ i punkt przecięcia $(1, 1/2)$.
Zatem to po prostu mniejszy trójkąt o podstawie na osi X od 0 do 2 (czyli długość 2) i wysokości y=1/2.
**Krok 4:** Pole tego małego trójkąta to $|A| = \frac{1}{2} \cdot a \cdot h_{nowe} = \frac{1}{2} \cdot 2 \cdot \frac{1}{2} = \frac{1}{2}$.
*(Obejdzie się bez całek, czysta geometria!)*
**Krok 5:** $P(A) = \frac{|A|}{|\Omega|} = \frac{1/2}{1} = \frac{1}{2}$.

---

### ZADANIE 5: Wartość oczekiwana zmiennej ciągłej

**O co w tym chodzi?**
Masz daną funkcję zwaną "gęstością" (opisuje ona, wokół jakich liczb najczęściej kręcą się losowe wyniki - im wyżej, tym większa szansa). "Wartość oczekiwana" (oznaczana jako $EX$ lub $E(X)$) to nic innego jak **średnia**. W świecie ciągłym sumowanie zastępujemy całką.
Wzór, który po prostu musisz zakuć na blachę:
$$E(X) = \int_{-\infty}^{\infty} x \cdot f(x) dx$$
Czyli bierzesz z zadania funkcję, **mnożysz ją przez małe "x"** i wyliczasz całkę w granicach podanych w zadaniu klamrą (tam gdzie nie ma zera). Jeśli są dwa przedziały w klamrze, liczysz dwie całki i je dodajesz.

#### Wersja A: Funkcja $h(x) = \frac{1}{2}$ dla $x \in [0,1]$ ORAZ $h(x) = \frac{1}{4}$ dla $x \in (1,3]$.
**Kroki:** Mnożymy każdy kawałek przez $x$ i całkujemy:
$EX = \int_{0}^{1} x \cdot \left(\frac{1}{2}\right) dx + \int_{1}^{3} x \cdot \left(\frac{1}{4}\right) dx$
Wyliczamy pierwszą całkę: $\int \frac{1}{2}x \,dx = \frac{1}{2} \cdot \frac{x^2}{2} = \frac{x^2}{4}$. W przedziale [0,1] to: $\frac{1^2}{4} - \frac{0^2}{4} = \frac{1}{4}$.
Wyliczamy drugą całkę: $\int \frac{1}{4}x \,dx = \frac{1}{4} \cdot \frac{x^2}{2} = \frac{x^2}{8}$. W przedziale [1,3] to: $\frac{3^2}{8} - \frac{1^2}{8} = \frac{9}{8} - \frac{1}{8} = \frac{8}{8} = 1$.
**Wynik:** Dodajemy obie: $EX = \frac{1}{4} + 1 = 1\frac{1}{4}$ (lub 1.25).

#### Wersja B: Funkcja $h(x) = \frac{2-x}{2}$ dla $x \in [0,2]$.
**Kroki:** Uprośćmy wzór na ułamki: $\frac{2}{2} - \frac{x}{2} = 1 - \frac{1}{2}x$. To jest nasza funkcja.
Teraz mnożymy ją przez $x$ z urzędu ze wzoru na Wartość Oczekiwaną:
$x \cdot (1 - \frac{1}{2}x) = x - \frac{1}{2}x^2$.
Liczymy całkę z tego w przedziale od 0 do 2.
$EX = \int_{0}^{2} (x - \frac{1}{2}x^2) dx$
Całka z $x$ to $\frac{x^2}{2}$. Całka z $\frac{1}{2}x^2$ to $\frac{1}{2} \cdot \frac{x^3}{3} = \frac{x^3}{6}$.
Mamy $\left[ \frac{x^2}{2} - \frac{x^3}{6} \right]$ od 0 do 2.
Podstawiamy 2: $\frac{2^2}{2} - \frac{2^3}{6} = \frac{4}{2} - \frac{8}{6} = 2 - \frac{4}{3} = \frac{6}{3} - \frac{4}{3} = \frac{2}{3}$.
Dla zera wszystko się zeruje (minus 0).
**Wynik:** $EX = \frac{2}{3}$.

---

