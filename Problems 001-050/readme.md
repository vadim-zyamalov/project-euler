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

# Задача 31

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
s(c) & = \max \{c \mid t \geqslant c \}
\end{aligned}$$

Таким образом можно "обратить" вычисления и идти "снизу вверх".
Этот способ вычислительно проще, так как не требуется производить дорогую операци вызова функции.

1. создадим массив с индексами от 0 до целевой суммы включительно.
   В ячейку 0 запишем 1, в остальные ячейки --- 0.
2. Для каждой монеты, начиная с наименьшей, к каждой ячейке, **начиная** с ячейки, соответствующей номиналу монеты, прибавляем ячейку с индексом за вычетом нминала монеты.
   Можно увидеть, что это равносильно применению записанной выше рекурсивной функции:

   * значение в ячейке перед суммированием равно $w(t, s(c))$;
   * значение в прибавляемой ячейке равно $w(t-c, c)$.