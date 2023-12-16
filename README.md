# Dokumentacja z Projektu z Fizyki 
## **1. Temat:**
#### _Ruch na równi pochyłej w górę (ruch jednostajnie opóźnony)_
## **2. Wzory wykorzystane w projekcie:**
### **a) Wzory bez uwzględnienia tarcia:**
#### Siła grawitacji na równi pochyłej - F<sub>graw</sub> = m * g * sin(α)
![siła grawitacji na równi pochyłej bez tarcia](/images/siła_g_bez.png)
###### F<sub>graw</sub> to siła wzdłuż równi, 
###### m to masa ciała,
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
#### Przyspieszenie wzdłuż równi pochyłej - a = g * sin(α)
###### a to przyspieszenie wzdłuż równi, 
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
#### Ruch jednostajnie opóźniony po równi pochyłej - s = v<sub>0</sub> * t + 1/2 * a * t<sup>2</sup>
###### s to przebyta droga,
###### v<sub>0</sub> to prędkość początkowa,
###### t to czas, 
###### a to przyspieszenie wzdłuż równi.
#### Maksymalna wysokość dla ruchu na równi pochyłej - h = ( v<sub>0</sub><sup>2</sup> * sin(α)<sup>2</sup>) / ( 2 * g )
###### h to maksymalna wysokość, 
###### v<sub>0</sub> to prędkość początkowa, 
###### α to kąt nachylenia równi, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>).
#### Prędkość końcowa w ruchu jednostajnie opóźnionym pod górę - v<sub>k</sub> = v<sub>0</sub> - g * t
###### v<sub>k</sub> to prędkość końcowa, 
###### v<sub>0</sub> to prędkość początkowa, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup> ),
###### t to czas. 
### **b) Wzory z uwzględnieniem tarcia:**
#### Siła wzdłuż równi z uwzględnieniem tarcia - F<sub>graw</sub> = m * g * sin(α) - μ * m * g * cos(α)
###### F<sub>graw</sub> to siła wzdłuż równi, 
###### m to masa ciała, 
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
###### μ to współczynnik tarcia.
#### Przyspieszenie wzdłuż równi z uwzględnieniem tarcia - a = g ( sin(α) - μ * cos(α) ) 
###### a to przyspieszenie wzdłuż równi, 
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
###### μ to współczynnik tarcia.
#### Ruch jednostajnie opóźniony uwzględniając tarcie w górę równi - s = ( v<sub>0</sub> * t - 1/2 * a * t<sup>2</sup> ) / 1 - ( μ * g * t<sup>2</sup> ) / ( 2 * v<sub>0</sub> )
###### s to odległość przebyta,
###### v<sub>0</sub> to prędkość początkowa,
###### t to czas, 
###### a to przyspieszenie wzdłuż równi
###### μ to współczynnik tarcia.
#### Maksymalna wysokość  ruchu na równi pochyłej z uwzględnieniem siły tacia - h = ( v<sub>0</sub><sup>2</sup> * sin(α)<sup>2</sup> ) / 2 * g * ( 1 - μ * cos(α) )
###### h to maksymalna wysokość, 
###### v<sub>0</sub> to prędkość początkowa, 
###### α to kąt nachylenia równi, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>), 
###### μ to współczynnik tarcia. 
#### Prędkość końcowa w ruchu jednostajnie opóźnionym pod górę - v<sub>k</sub> = ( v<sub>0</sub> - μ * g * t ) / 1 + ( μ * g * t ) / 2 * v<sub>0</sub>
###### v<sub>k</sub> to prędkość końcowa, 
###### v<sub>0</sub> to prędkość początkowa, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup> ),
###### t to czas
###### μ to współczynnik tarcia.
## **3. Co należy wprowadzić?**
#### Masę
#### Kąt
#### Drogę (wysokość)
## **4. Co wylicza?**
#### Siłę grawitacji na równi pochyłej
#### Maksymalna wysokość
#### Czas, w jakim pojazd wjedzie na górę 
#### Prędkość końcową 
#### Przyspieszenie (opóźnienie)
## **5. Co należy uwzględnić?**
#### Współczynnik tarcia
#### Maksymalna prędkość samochodu/pojazdu jadącego
#### Kąt mniejszy niż 90 stopni 
#### Najwyższy punkt na świecie
## **6. Założenia:**
#### Program napiszemy w Pythonie
#### Zamiana jednostek na m/s na km/h, jeśli jedzie rower
#### Aplikacja okienkowa
#### Animacja wjazdu pod górę równi pochyłej 
#### Wykres w pythonie (na podstawie danych zapisywanych w pliku Excel) _na wykresie należy zawrzeć drogę w czasie/prędkość w czasie/energię potencjalną w czasie/ energię kinetyczną w czasie_
