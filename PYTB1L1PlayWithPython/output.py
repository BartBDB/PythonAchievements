>>> 2+2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print("Mijn naam is Bart")
Mijn naam is Bart
>>> naam = "Bart"
>>> print(naam)
Bart
>>> print(naam.upper())
BART
>>> print(naam[0:2])
Ba
>>> print(naam[::-1])
traB
>>> leeftijd = 18
>>> print("Hallo " + naam + " ben je al " + str(leeftijd) + " jaar?")
Hallo Bart ben je al 18 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
19
>>> leeftijd-=1
>>> leeftijd
18
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>>     hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 1
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: unexpected indent
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print("Over " + str(hoelang_tot18jaar) + " jaar wordt je 18")
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print("Het is alweer " + str(hoelang_al18jaar) + " jaar geleden dat je 18 werd ;-)")
... else:
...     print("Je bent precies " + str(leeftijd) + " jaar")
...
Je bent precies 18 jaar
>>> from random import randint
>>> randint(0,1000)
600
>>> willekeurig getal = randint(0,1000)
  File "<stdin>", line 1
    willekeurig getal = randint(0,1000)
                ^
SyntaxError: invalid syntax
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
961
>>> print("Willekeurig getal tussen 0 en 1000: " + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 961
>>>
>>>
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 13:59:31.005405
>>> datum.strftime("%A %d %B %Y")
'Wednesday 09 September 2020'
>>>
>>> import locale
>>> locale.setlocale(locale.LC_TIME, "nl_NL")
'nl_NL'
>>> datum.strftime("%A %d %B %Y")
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, "it_IT")
'it_IT'
>>> datum.strftime("%A %d %B %Y")
'mercoledì 09 settembre 2020'
>>>