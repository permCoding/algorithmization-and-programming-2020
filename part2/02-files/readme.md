## Файлы  

---

[HTML-colors](https://basicweb.ru/html/html_colors.php)  

---  

Рассмотренный далее код расположен по этому адресу:  
https://repl.it/@pCoding/ReadWrite  

---

Далее рассмотрены примеры обработки текстового файла  

Пусть есть текстовый файл input.txt:  

```
1 2 3
4 5 6
7 8 9
```

Прочитаем содержимое текстового файла и выведем на экран:  

```
# p1
f1 = open('input.txt', 'r') # открываем файл для чтения
text = f1.read() # читаем все символы
print(text) # вывести все символы на экран
f1.close() # закрываем файл
```


Можно поступить иначе, считать файл в строковую переменную и разбить её на список строк по сепаратору «перенос строки»:

```
# p2
f1 = open('input.txt', 'r') # открываем файл для чтения
text = f1.read() # читаем все символы
lines = text.split('\n') # разбиваем на массив строк
f1.close() # закрываем файл
```

и вывести все элементы списка на экран с помощью цикла по коллекции:

```
# p3
for line in lines:
    print(line) # выводим на экран все строки
```

или вывести строки на экран с помощью цикла по индексам с проверкой условия:

```
# p4
n = len(lines) # узнаём количество строк
for i in range(n):
    if i>0: # выводим часть списка
        print(lines[i])
```

или вывести строки в обратном порядке в другой текстовый файл:

```
# p5
f2 = open('output.txt', 'w')
line = ''
for i in range(n-1,-1,-1): # строки в обратном порядке
    line = lines[i] + '\n' 
f2.write(line) # выводим строку в файл
f2.close()
```

или подсчитать сумму чисел в определённом столбце:

```
# p6
acc = 0
for line in lines:
    lst = line.split(' ')
    acc += int(lst[0]) # сумма чисел в левом столбце
print("acc =", acc)
```

или создать из списка строк двумерный список:

```
# p7
# создать двумерный массив
tab = [] # создали пустой список
for line in lines:
    tmp = line.split(' ') # делаем из строки список
    tab.append(tmp) # добавляем его в tab
```

и найти в нём сумму чисел в левом столбце:

```
# p8
acc = 0
for row in range(len(tab)):
    acc += int(tab[row][0]) # строка row и столбец 0
print("acc =", acc)
```

или просто вывести все элементы двумерного списка на экран:

```
# p9
for t in tab:
    print(*t)
```

или поменять знаки для всех чисел, лежащих на главной диагонали:

```
# p10
for row in range(len(tab)):
    t = tab[row]
    for col in range(len(t)):
        if row==col:
            tab[row][col] = -int(tab[row][col])
for t in tab:
    print(*t)
```

---  

```

```

---  



