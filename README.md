# Dokumentacja z Projektu z Fizyki 
## **1. Temat:**
#### _Ruch na równi pochyłej w górę (ruch jednostajnie opóźnony)_
## **2. Wzory wykorzystane w projekcie:**
### **a) Wzory bez uwzględnienia tarcia:**
#### Siła grawitacji na równi pochyłej 
![siła grawitacji na równi pochyłej bez tarcia](/images/siła_g_bez.png)
###### F<sub>graw</sub> to siła wzdłuż równi, 
###### m to masa ciała,
###### θ to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
#### Przyspieszenie wzdłuż równi pochyłej
![Przyspieszenie wzdłuż równi pochyłej](/images/a_bez.png)
###### a to przyspieszenie wzdłuż równi, 
###### θ to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
#### Ruch jednostajnie opóźniony po równi pochyłej 
![droga w ruchu jednostajnie opóźnionionym po równi pochyłej](/images/s_bez.png)
###### s to przebyta droga,
###### v<sub>0</sub> to prędkość początkowa,
###### t to czas, 
###### a to przyspieszenie wzdłuż równi.
#### Maksymalna wysokość dla ruchu na równi pochyłej 
![Maksymalna wysokość bez tarcia](/images/h_bez.pn)
###### h to maksymalna wysokość, 
###### v<sub>0</sub> to prędkość początkowa, 
###### α to kąt nachylenia równi, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>).
#### Prędkość końcowa w ruchu jednostajnie opóźnionym pod górę 
![Prędkość końcowa w ruchu jednostajnie opóźnionym pod górę bez tarcia](/images/vk_bez.png)
###### v<sub>k</sub> to prędkość końcowa, 
###### v<sub>0</sub> to prędkość początkowa, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup> ),
###### t to czas. 
### **b) Wzory z uwzględnieniem tarcia:**
#### Siła wzdłuż równi z uwzględnieniem tarcia 
![Siła z tarciem](/images/sila_g_tarcie.png)
###### F<sub>równi</sub> to siła wzdłuż równi, 
###### m to masa ciała, 
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
###### μ to współczynnik tarcia.
#### Przyspieszenie wzdłuż równi z uwzględnieniem tarcia 
![Przyspieszenie wzdłuż równi z tarciem](a_tarcie.png)
###### a to przyspieszenie wzdłuż równi, 
###### α to kąt nachylenia równi,
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>),
###### μ to współczynnik tarcia.
#### Ruch jednostajnie opóźniony uwzględniając tarcie w górę równi
![Droga w ruchu jednostajnie opóźnionym z taciem](/images/s_tarcie.png)
###### s to odległość przebyta,
###### v<sub>0</sub> to prędkość początkowa,
###### t to czas, 
###### a to przyspieszenie wzdłuż równi
###### μ to współczynnik tarcia.
#### Maksymalna wysokość  ruchu na równi pochyłej z uwzględnieniem siły tacia 
![Maksymalna wysokość z taciem](h_tarcie.png)
###### h to maksymalna wysokość, 
###### v<sub>0</sub> to prędkość początkowa, 
###### α to kąt nachylenia równi, 
###### g to przyspieszenie ziemskie (ok. 9,81 m/s<sup>2</sup>), 
###### μ to współczynnik tarcia. 
#### Prędkość końcowa w ruchu jednostajnie opóźnionym pod górę 
![Prędkość końcowa z tarciem](/images/v_tarcie.png)
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
<!-- Wszystkie wzory zapisane ręcznie: 
a) bez tarcia:
Siła grawitacji - F = m * g * sin(α)
Przyspieszenie - a = g * sin(α)
Droga -  s = v0 * t + 1/2 * a * pow(t,2)
Maksymalna wysokość h = ( pow(v,2) * sin(a)^2 ) / ( 2 * g )
Prędkość końcowa bez tarcia - vk = v0 - g * t
b) z tarciem: 
Siła grawitacji - F = m * g * sin(α) - μ * m * g * cos(α)
Przyspiesznie a = g ( sin(α) - μ * cos(α) ) 
Droga -  s = ( v0 * t - 1/2 * a * pow(t,2) ) / 1 - ( μ * g * pow(t,2) ) / ( 2 * v0 )
Maksymalna wysokość  h = ( v0^2 * sin(α)^2  ) / 2 * g * ( 1 - μ * cos(α) )
Prędkość końcowa z tarciem vk = ( v0 - μ * g * t ) / 1 + ( μ * g * t ) / 2 * v0
