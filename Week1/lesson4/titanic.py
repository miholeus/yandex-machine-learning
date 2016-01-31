# coding: utf-8

"""
1. Загрузите выборку из файла titanic.csv с помощью пакета Pandas.
2. Оставьте в выборке четыре признака: класс пассажира (Pclass), цену билета
(Fare), возраст пассажира (Age) и его пол (Sex).
3. Обратите внимание, что признак Sex имеет строковые значения.
4. Выделите целевую переменную — она записана в столбце Survived.
5. В данных есть пропущенные значения — например, для некоторых пассажиров
неизвестен их возраст. Такие записи при чтении их в pandas принимают значение
nan. Найдите все объекты, у которых есть пропущенные признаки, и удалите их
из выборки.
6. Обучите решающее дерево с параметром random_state=241 и остальными
параметрами по умолчанию.
Вычислите важности признаков и найдите два признака с наибольшей важностью.
Их названия будут ответами для данной задачи (в качестве ответа укажите
названия признаков через запятую или пробел, порядок не важен).
"""

import pandas
import operator
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
