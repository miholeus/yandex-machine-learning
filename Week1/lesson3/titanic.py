# coding: utf-8

"""
1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа
приведите два числа через пробел.

2. Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не
нужен).

3. Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ
приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).

4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста
пассажиров. В качестве ответа приведите два числа через пробел.

5. Коррелируют ли число братьев/сестер с числом родителей/детей? Посчитайте
корреляцию Пирсона между признаками SibSp и Parch.

6. Какое самое популярное женское имя на корабле? Извлеките из полного имени
пассажира (колонка Name) его личное имя (First Name). Это задание — типичный
пример того, с чем сталкивается специалист по анализу данных. Данные очень
разнородные и шумные, но из них требуется извлечь необходимую информацию.
Попробуйте вручную разобрать несколько значений столбца Name и выработать
правило для извлечения имен, а также разделения их на женские и мужские.
"""

import pandas
import operator
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print("1. Male and Female")
print(data['Sex'].value_counts())
survived = data['Survived'].value_counts()
print("2. Survived")
print(float(survived[1])/sum(survived)*100)
print("3. First class passengers")
passengers = data['Pclass'].value_counts()
print(float(passengers[1])/sum(passengers)*100)
print("4. Age of passengers")
age = data['Age']
print("%s %s" % (age.mean(), age.median()))
print("5. Brothers/sisters and parents/children correlation")
print(data['SibSp'].corr(data['Parch'], method='pearson', min_periods=1))
print("6. Popular Female Name")
name = data['Name']
df = name.where(data['Sex'] == 'female')
names = [name for name in df if pandas.isnull(name) == False]
female_names = dict()
for name in names:
    name = name.split(",")[1] # name
    if "(" in name:
        first, last = (name.index("("), name.index(")"))
        f_name = name[first+1:last].split(" ")[0]
    else:
        f_name = name.replace("Miss.", "")
        f_name = f_name.strip().split(" ")[0]
    female_names[f_name] = female_names.get(f_name, 0) + 1
names_sorted = sorted(female_names.items(), key=operator.itemgetter(1))
print(names_sorted[-1][0])
