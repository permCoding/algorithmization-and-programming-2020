## Структуры данных  

### Кортеж - tuple  

Кортежи: являются неизменяемой последовательностью элементов.  
То есть кортеж, как список, только элементы нельзя менять.  
Чтобы присвоить переменной значение типа данных Tuple, необходимо заключить последовательность элементов в круглые скобки.

Кортеж - tuple
Кортежи: являются неизменяемой последовательностью элементов.
То есть кортеж, как список, только элементы нельзя менять. Чтобы присвоить переменной значение типа данных Tuple, необходимо заключить последовательность элементов в круглые скобки.

```
tpl = (1, 2, '0', 3.1415, "слово", False)

print(type(tpl))
print(tpl)
print(tpl[0])
for item in tpl:
    print(item)
```

```
persons = [
    (1, "Иванов Иван", 18),
    (2, "Грета Тунберг", 12),
    (3, "Ада Лавлейс", 45)
]

for item in persons:
    print(item)
```

```
persons = [
    (1, "Иванов Иван", 18),
    (2, "Грета Тунберг", 12),
    (3, "Ада Лавлейс", 45)
]

person = (0, "Тот самый", 33)
men = (4, "Некто Нектович", 20)

persons.insert(0, person)
persons.append(men)
persons.extend([person, men])

for item in persons:
    print(item)
```

---

### Множество - set  

Множество - это такая коллекция, к которой нет повторяющихся элементов. При попытке добавить во множество элемент, который там уже есть повторный элемент не добавится. Во множестве у элементов нет порядковых номеров - к ним нельзя обратиться по индексу, можно только проверить наличие элемента во множестве. При попытке создать множество с повторяющимися элементами - дубликаты будут удалены.

```
st = {'A', 'B', 'C', 'D'}
print(type(st), '\t', st, '\n')

st = set()

st.add(1)
st.add(2)
st.add(1)
st.add(0)

print(st)
print(list(st))

lstA = [1, 2, 3, 4, 5]
lstB = [3, 4, 5, 6, 7]
lstAB = lstA + lstB
print(lstAB)
st = set(lstAB)
print(st)

print(8 in st)
print(7 in st)
```

```
Операции над множествами:

len(s) - число элементов в множестве.
x in s - принадлежит ли x множеству s.
set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
set == other - все элементы set принадлежат other и все элементы other принадлежат set.
set.issubset(other) или set <= other - все элементы set принадлежат other.
set.issuperset(other) или set >= other - аналогично.
set.union(other, ...) или set | other | ... - объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... - пересечение.
set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.copy() - копия множества.
set.update(other, ...); set |= other | ... - объединение.
set.intersection_update(other, ...); set &= other & ... - пересечение.
set.difference_update(other, ...); set -= other | ... - вычитание.
set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.add(elem) - добавляет элемент в множество.
set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) - удаляет элемент, если он находится в множестве.
set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
set.clear() - очистка множества.
```

### Словарь  

Словарь - это такая коллекция, в которой хранятся пары в формате «ключ-значение». Значения ключей в словаре уникальны.

```
persons = {
    1: ("Иванов Иван", 18),
    2: ("Грета Тунберг", 12),
    3: ("Ада Лавлейс", 45)
}

print(type(persons))
print(persons)

persons[0] = ("Тот самый", 33)
print(persons)

persons.update({4: ("Некто Нектович", 20)})
print(persons)

for key in persons.keys():
    print(f"{key}\t{persons[key]}")

print(persons[0])
print(persons.get(0))
print(persons.get(9))
```





---  

```

```

---  



