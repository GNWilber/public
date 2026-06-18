Oto rozwiązania poszczególnych zadań z arkusza egzaminacyjnego:

---

### **Zadanie 1**
**Treść:**
*Ile jest numerów rejestracji długości 6, w których mogą pojawić się litery $A, B, C$ i cyfry $1, 2, 3, 4, 5, 6, 7$ i w których (niekoniecznie różne) litery i (niekoniecznie różne) cyfry stoją na przemian?*

**Rozwiązanie:**
Mamy zestaw liter $L = \{A, B, C\}$ o liczności $|L| = 3$ oraz zestaw cyfr $D = \{1, 2, 3, 4, 5, 6, 7\}$ o liczności $|D| = 7$.
Rejestracja ma długość 6. Ponieważ litery i cyfry stoją na przemian, istnieją dwa możliwe, rozłączne wzorce układu znaków:
1. **Litera, Cyfra, Litera, Cyfra, Litera, Cyfra (L D L D L D)**
   Liczba takich numerów wynosi:
   $$|L| \times |D| \times |L| \times |D| \times |L| \times |D| = 3^3 \times 7^3 = 27 \times 343 = 9261$$

2. **Cyfra, Litera, Cyfra, Litera, Cyfra, Litera (D L D L D L)**
   Liczba takich numerów wynosi:
   $$|D| \times |L| \times |D| \times |L| \times |D| \times |L| = 7^3 \times 3^3 = 343 \times 27 = 9261$$

Suma obu możliwości daje całkowitą liczbę numerów rejestracyjnych:
$$9261 + 9261 = \mathbf{18522}$$

---

### **Zadanie 2**
**Treść:**
*Na ile sposobów można rozmieścić 4 nierozróżnialne białe kule i 2 nierozróżnialne czarne kule w 4 szufladach?*

**Rozwiązanie:**
Rozmieszczenie kul białych i czarnych przebiega niezależnie. Ponieważ kule w obrębie danego koloru są nierozróżnialne, a szuflady są rozróżnialne, stosujemy kombinacje z powtórzeniami (model "gwiazdek i kresek"), gdzie liczba sposobów rozmieszczenia $k$ obiektów w $n$ szufladach wynosi $\binom{k+n-1}{k}$:

1. Rozmieszczenie 4 białych kul ($k_w = 4$) w 4 szufladach ($n = 4$):
   $$W = \binom{4+4-1}{4} = \binom{7}{4} = 35$$

2. Rozmieszczenie 2 czarnych kul ($k_b = 2$) w 4 szufladach ($n = 4$):
   $$B = \binom{2+4-1}{2} = \binom{5}{2} = 10$$

Całkowita liczba sposobów wynosi:
$$W \times B = 35 \times 10 = \mathbf{350}$$

---

### **Zadanie 3**
**Treść:**
*Ile jest pięciocyfrowych liczb o cyfrach ze zbioru $\{3, 4, 5, 6, 7, 8\}$, w których dokładnie dwie cyfry się powtarzają?*

**Rozwiązanie:**
Sformułowanie „dokładnie dwie cyfry się powtarzają” można zinterpretować na dwa sposoby:

* **Interpretacja A (jedna cyfra występuje dokładnie dwukrotnie, a pozostałe trzy są różne):**
  W liczbie występuje dokładnie jedna para takich samych cyfr (np. $\{a, a, b, c, d\}$).
  1. Wybór cyfry, która ma się powtórzyć (dwukrotnej): $\binom{6}{1} = 6$ sposobów.
  2. Wybór 3 pozostałych (różnych) cyfr ze zbioru: $\binom{5}{3} = 10$ sposobów.
  3. Liczba permutacji z powtórzeniami takich 5 cyfr: $\frac{5!}{2!} = 60$.
  
  Liczba takich liczb wynosi:
  $$6 \times 10 \times 60 = \mathbf{3600}$$

* **Interpretacja B (dokładnie dwie różne wartości cyfr powtarzają się w zapisie liczby):**
  W liczbie występują dokładnie dwie cyfry mające krotność $\ge 2$. Dla długości 5 możliwe są dwa układy:
  1. Układ typu $\{a, a, b, b, c\}$ (dwie pary i jedna pojedyncza cyfra):
     * Wybór 2 cyfr dwukrotnych: $\binom{6}{2} = 15$
     * Wybór 1 cyfry pojedynczej: $\binom{4}{1} = 4$
     * Liczba permutacji: $\frac{5!}{2!2!} = 30$
     * Razem: $15 \times 4 \times 30 = 1800$
  2. Układ typu $\{a, a, a, b, b\}$ (jedna potrójna i jedna podwójna):
     * Wybór cyfry potrójnej: $\binom{6}{1} = 6$
     * Wybór cyfry podwójnej: $\binom{5}{1} = 5$
     * Liczba permutacji: $\frac{5!}{3!2!} = 10$
     * Razem: $6 \times 5 \times 10 = 300$
     
  Suma dla tej interpretacji wynosi:
  $$1800 + 300 = \mathbf{2100}$$

---

### **Zadanie 4**
**Treść:**
*25-krawędziowy graf prosty posiada 3 wierzchołki stopnia 4, 4 stopnia 5 oraz wierzchołki stopnia 6. Podać ciąg stopni wierzchołków dopełnienia tego grafu.*

**Rozwiązanie:**
Niech $n$ oznacza łączną liczbę wierzchołków w grafie $G$. Z twierdzenia o uściskach dłoni wiemy, że suma stopni wierzchołków jest równa podwojonej liczbie krawędzi ($2 \times 25 = 50$):
$$3 \times 4 + 4 \times 5 + (n - 7) \times 6 = 50$$
$$12 + 20 + 6n - 42 = 50$$
$$6n - 10 = 50 \implies 6n = 60 \implies n = 10$$

Graf $G$ o 10 wierzchołkach ma:
- 3 wierzchołki o stopniu 4,
- 4 wierzchołki o stopniu 5,
- 3 wierzchołki o stopniu 6 ($10 - 7 = 3$).

Stopień wierzchołka $v$ w grafie dopełnienia $\bar{G}$ oblicza się jako $\operatorname{deg}_{\bar{G}}(v) = n - 1 - \operatorname{deg}_G(v) = 9 - \operatorname{deg}_G(v)$:
- Dla wierzchołków stopnia 4 w $G$: $9 - 4 = 5$ (3 wierzchołki),
- Dla wierzchołków stopnia 5 w $G$: $9 - 5 = 4$ (4 wierzchołki),
- Dla wierzchołków stopnia 6 w $G$: $9 - 6 = 3$ (3 wierzchołki).

Uporządkowany nierosnąco ciąg stopni wierzchołków dopełnienia wynosi:
$$\mathbf{(5, 5, 5, 4, 4, 4, 4, 3, 3, 3)}$$

---

### **Zadanie 5**
**Treść:**
*Graf $G$ jest rozłączną sumą grafów $K_{10}$ i $K_{8,8}$ (tj. posiada dwie składowe spójne izomorficzne z tymi grafami). Podać liczbę krawędzi dopełnienia grafu $G$.*

**Rozwiązanie:**
Graf $G$ składa się z dwóch składowych: $G_1 = K_{10}$ oraz $G_2 = K_{8,8}$.
1. Liczba wierzchołków grafu $G$:
   $$N = 10 + (8 + 8) = 26$$

2. Liczba krawędzi w grafie $G$ to suma krawędzi składowych:
   - W grafie pełnym $K_{10}$: $e_1 = \binom{10}{2} = 45$
   - W pełnym grafie dwudzielnym $K_{8,8}$: $e_2 = 8 \times 8 = 64$
   - Łącznie: $E_G = 45 + 64 = 109$

3. Liczba krawędzi w dopełnieniu grafu $\bar{G}$ o $N = 26$ wierzchołkach:
   $$E_{\bar{G}} = \binom{26}{2} - E_G = \frac{26 \times 25}{2} - 109 = 325 - 109 = \mathbf{216}$$

---

### **Zadanie 6**
**Treść:**
*Połączmy wybrane wierzchołki dwóch grafów pełnych $K_6$ i $K_7$ krawędzią. Ile drzew spinających ma otrzymany w ten sposób graf?*

**Rozwiązanie:**
Dodana krawędź $e$ łącząca podgrafy $K_6$ i $K_7$ stanowi most (cut-edge) w otrzymanym grafie $G$. Każde drzewo spinające grafu $G$ musi obowiązkowo zawierać tę krawędź, aby zachować spójność. 

Stąd liczba drzew spinających grafu $G$ jest iloczynem liczby drzew spinających każdej ze składowych. Korzystając z wzoru Cayleya ($n^{n-2}$):
- Liczba drzew spinających dla $K_6$: $T(K_6) = 6^{6-2} = 6^4 = 1296$
- Liczba drzew spinających dla $K_7$: $T(K_7) = 7^{7-2} = 7^5 = 16807$

Całkowita liczba drzew spinających wynosi:
$$T(G) = 1296 \times 16807 = \mathbf{21781872}$$