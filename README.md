# informationAnalysis
 Разработайте программу, которая по заданному файлу Х рассчитывает:
— длину n файла Х в символах первичного алфавита А1;
— vi; — общее количество вхождений каждого из символов аi из A1 в Х
(целочисленную частоту аi);
и оценивает, считая файл Х порождённым источником без памяти:
— вероятность рi каждого из символов аi из А1;
— количество информации I(аi) в каждом символе аi из А1;
суммарное количество информации I(Х) в файле Х (не среднее на
символ, которое в n раз меньше, а именно суммарное!) в битах и байтах;
символом кодирования, как всегда, является байт (с учётом использования
архитектуры х86 это 8 бит, октет), первичным алфавитом А1 — множество
возможных значений байта (0...255).
Полученные величины необходимо вывести на экран или сохранить
в виде отчёта; причём таблица характеристик символов алфавита. а; Е Ат
должна выводиться дважды (либо в программе необходимо предусмотреть
пересортировку) — отсортированной по алфавиту (по значению а;) и отсор-
тированной по убыванию частоты их.
Проверьте разработанную программу на файлах различного формата,
(не только простом тексте; в том числе и на бинарных).
Задание №2. Разработайте программу, аналогичную №1, но
считающую символом кодирования печатный символ Unicode, а первичным
алфавитом А! — множество символов Unicode 
