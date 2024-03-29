# Задачи 1-50

## Задача 29

Самое простое решение --- брутфорс, тем более, что размер задачи невелик.

Решение посложнее за авторством [WP](https://projecteuler.net/action=redirect;post_id=92910) основано на явном поиске числа дубликатов.
Идея в том, что для каждой степени $p$ мы смотрим на число пересечений со степенями $k = 1, \dots, p-1$.
Они расположены в точках $div(lcm(k, p), p)$.
Для их правильного учета сохраняем точки либо в массиве (дорого по памяти), либо в битовой маске.

Затем находим число **истинных** степеней, то есть чисел, которые представимы в виде какой-либо степени, но не большей.
Итоговое число дубликатов является поэлелементным произведением двух полученных списков.

Есть еще более хитрое [решение](https://projecteuler.net/action=redirect;post_id=93014).
Понять его достаточно сложно, так как два момента от меня ускользают.
Оно основано на поиске именно числа различных чисел.

Для начала определяется максимально возможная степень, для которой потенциально возможны пересечения.
Это $\log_2 N$.
Для каждой степени от 2 до этого предела проводится следующая процедура:

1. берется какая-либо степень $p$.
2. для всех степеней от $p$ до предельной из списка $[p, maxP]$ убираются все кратные.
   То есть, например, для $p = 2$ и $maxP = 10$ из списка $[2, 10]$ исключаются $4, 6, 8, 10$ как кратные 2, $6, 9$ как кратные 3, и так далее.
3. для каждой оставшейся степени считается число кратных степеней в пределах $[(p-1)N+1, pN]$ (почему так, не понимаю) за вычетом пересечений со степенями от $p$ до этой степени в совокупности методом включения-исключения.
Пределы $[(p-1)N+1, pN]$, как мне кажется, это границы области, в которую может попасть степень идеальной, пардон, степени (после приведения к базовому основанию), но не может попасть степень идеальной степени, меньшей на единицу.
Под идеальной степенью будем понимать число, представимое в виде степени некоторого базового основания, но не представимое в виде степени более высокого порядка.

Далее к числу уникальных показателей для какой-либо степени (то есть число степеней, в которые можно возвести идеальную степень), прибавляем все предыдущие количества, для учета меньших степеней того-же базового основания.

После этого перебираем все числа от 2 до $\sqrt{N}$; далее смысла рассматривать нет, так как только эти числа, взятые в качестве базового основания, могут порождать дубликаты.
Для каждого находим максимальную степень, при возведении в которую число не превысит $N$, и считаем число степеней, при возведении в которую оно превысит $\sqrt{N}$.
Для первого числа находим соответствующее число уникальных показателей (из найденного выше списка) и прибавляем его к аккумулятору ответа.

После этого прибавляем к аккумулятору $(N - \sqrt{N})(N - 1)$, чтобы учесть все степени чисел после $\sqrt{N}$.
Так как мы явно дважды посчитали сверх степени чисел до корня (смотри второе найденное число степеней), то мы должны домножить его на $N-1$ и вычесть из ответа.

Алгоритм муторный, но быстрый. Если заменить массивы на битовые операции, то можно сэкономить на памяти.

## Задача 31

Я решил методом динамического программирования при помощи рекурсии с мемоизацией.
На каждом шаге я **уменьшаю** целевое число на одну монету, не меньшую, чем на предыдущем шаге.
Алгоритм плохо работает на больших целевых суммах, так как требует рекурсивных вызовов.

В сопроводительных документах (к этой задаче они есть) приведен анализ задачи с выводом рекурсивной функции.
Там показано, что если принять за ответ результаты исполнения функции $w(t, c)$, где $t$ --- целевое число, а $c$ --- рассматриваемая на текущий момент монета, то можно вывести соотношение

$$\begin{aligned}
w(t, c) & = \begin{cases}
	1 & t = 0 \lor c = 1 \\
	w(t, s(c)) & c > 1 \land t < c \\
	w(t, s(c)) + w(t-c, c) & c > 1 \land t \geqslant c
\end{cases} \\
s(c) & = \max \left\\{c \mid t \geqslant c \right\\}
\end{aligned}$$

Таким образом можно "обратить" вычисления и идти "снизу вверх".
Этот способ вычислительно проще, так как не требуется производить дорогую операци вызова функции.

1. создадим массив с индексами от 0 до целевой суммы включительно.
   В ячейку 0 запишем 1, в остальные ячейки --- 0.
2. Для каждой монеты, начиная с наименьшей, к каждой ячейке, **начиная** с ячейки, соответствующей номиналу монеты, прибавляем ячейку с индексом за вычетом нминала монеты.
   Можно увидеть, что это равносильно применению записанной выше рекурсивной функции:

   * значение в ячейке перед суммированием равно $w(t, s(c))$;
   * значение в прибавляемой ячейке равно $w(t-c, c)$.

## Задача 33

Мое решение ужасно некрасиво, но работает.

На форуме подсмотрел идею более простого решения.
Из условия следует, что
$$\frac{10d + d}{10d + d} = \frac{d}{d}$$
где $d$ --- цифры.

Всего имеем 4 ситуации:

1. Пусть

   $$\frac{10x + y}{10z + y} = \frac{x}{z} < 1$$

   Тогда имеем

   $$(10x + y)z = (10z + y)x$$
   $$10xz + yz = 10xz + xy$$
   $$yz = xy$$

   Последнее равенство справедливо в двух случаях:

   * $y = 0$, но этот случай по условию является тривиальным, то есть неподходящим;
   * $y > 0,\ x = z$, что означает, что искомое рациональное число равно 1.

   То есть данный вариант не удовлетворяет условию задачи.

2. Пусть

   $$\frac{10y + x}{10y + z} = \frac{x}{z} < 1$$

   После аналогичных действий получим то же условие $yz = xy$.

   * вариант $y=0$ означает, что в числителе и знаменателе стоят однозначные числа, что противоречит условию задачи;
   * вариант $x = z$ также не подходит.

3. Пусть

   $$\frac{10x + y}{10y + z} = \frac{x}{z}$$

   Преобразованиями получим

   $$10xz + yz = 10yx + xz$$
   $$z = \frac{10xy}{9x+y}$$

   Таким образом, если искомое число соответствует этому случаю, то достаточно перебрать комбинации $0 \leqslant x,y \leqslant 9$ и найти те, для которых полученное значение $z$ будет больше $x$.

   Можно показать, что это выполняется при $x < y$, таким образом можно уменьшить число перебираемых вариантов, что не сильно критично для соременных компьютеров.

4. Пусть

   $$\frac{10y + x}{10z + y} = \frac{x}{z} < 1$$

   Тогда

   $$10yz + xz = 10xz + xy$$
   $$z = \frac{xy}{10y - 9x}$$

   Аналогично, можно показать, что в этом случае $x > y$.

Если мой код выполняется за 0.02 секунды, то более быстрый вариант гораздо быстрее, быстрее 1 десятитысячной.

## Задача 43

Мой итоговый код выполняется за секунду.

Подсмотренный код, который реализует мою первоначальную идею конструирования искомых чисел, отрабатывает за 15 сотых секунды.

## Задача 44

Оптимизация, которую я взял из обсуждения: вместо цикла

```python
for n in range(1, limit):
    for m in range(n + 1, limit):
        pass
```

я взял цикл

```python
for n in range(1, limit):
    for m in range(n):
        pass
```

Это позволяет не завершать цикл полностью, но останавливаться при обнаружении первой пары, удовлетворяющей условию.
Можно вообще избавиться от предела:

```python
n = 1
while True:
    for m in range(n):
        pass # Здесь что-то делается
    n += 1
```