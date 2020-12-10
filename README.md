<b>ENGLISH</b>

(Russian is below)

<b>A short story of this project</b>

I started to learn Pyton on my own almost in the same time with German.
My friend and I decided to work together, call each other on video, check each other out and come up with small tasks. To better remember numbers, we gave each other simple examples of addition and subtraction with numbers up to 100. We asked and answered in German, but found that while one answered, the other might forget what he/she asked. Or one might have made a mistake either in the calculations or in the translation, and the other might not have noticed that or made a mistake too. I came up with a solution — I wrote a script that generated a list of examples with answers — so we began to stumble much less, and this practice itself turned out to be very useful and effective. I can recommend it to anyone who is learning new languages.

<b>What I added later:</b>
* generation of multiplication and division examples
* a function that converts positive natural numbers to string values with the same number written in German words
* using this function — output examples both in numerical form and in German words
* one more script that generates dates — to study them in the same form. This script has a function in ordinal numbers, but only up to 31
* more intelligent results: the likelihood of repeated numbers and dates kept to a minimum. The output of mathematical operations and centuries is also balanced
* a script that generates a list of numerals in a given range - in number format and in German
* function to save the received data to a text file

At this stage the project began to look like able to be useful for other people. Therefore I uploaded it to the public repository on GitHub. I will be glad if it's really useful for someone.

<b>in the plans:</b>
* GUI
* telegram bot

<b>Files in the project:</b>
* core.py — here are functions that are used by several modules for data processing at once
* cli.py - functions used by the command-line interface
* german_numbers.py — simple interface for converting numbers to strings with these numbers in German
* german_examples.py — examples of simple mathematical operations, presented in the form of numbers and in German.
* german_dates.py — list of random dates in several formats: DD.MM.YYYY. US, Russian, German and completely in German words
* german_numerals_list.py - a list of numerals in a given range - in number format and in German

<b>if you don't know how to run python scripts:</b>
1. Download the contents of the repository: "Clone or download" → "Download ZIP»
2. Install the Python interpreter version 3.x if it is not installed on your system.
3. Run the command prompt in the folder where the scripts are located
4. Run them with commands like "python3 german_examples.py" or "python3 german_dates.py»

Depending on the settings in your operating system, the interpreter may be called differently — for example, "python" or "py".


<b> RUSSIAN / РУССКИЙ </b>

<b>Небольшая история этого проекта</b>

Я начал самостоятельно изучать Python почти одновременно с немецким.
Мы с подругой решили скооперироваться, созваниваться по видео, проверять друг друга и придумывать небольшие задания. Чтобы лучше запомнить числительные,давали друг другу простые примеры на сложение и вычитание с числами до 100. И спрашивали, и отвечали на немецком, но И спрашивали, и отвечали на немецком, но столкнулись с тем, что пока один отвечал, второй мог забыть, что спрашивал. Или же один мог ошибиться либо в подсчётах, либо в переводе, а второй мог не заметить или ошибиться сам. Я придумал решение — написал скрипт, который генерировал список примеров с ответами — так мы стали спотыкаться гораздо меньше, да и сама эта практика оказалась весьма полезной и эффективной. Могу порекомендовать всем, кто учит новые языки.

<b>Что я добавил позднее:</b>
*	генерация примеров на умножение и деление
*	функция, которая переводит натуральные положительные числа в строковые значения с тем же числом написанным немецкими словами
*	с использованием этой функции — вывод примеров как в числовом виде, так и немецкими словами
*	еще один скрипт, генерирующий даты — для их изучения в той же форме. Так появился перевод и в порядковые числительные, но только до 31
*	более умная выдача: вероятность повторов чисел и дат сведена к минимуму. Также сбалансирована и выдача математических операций, а в скрипте с датами — выдача по векам.
*	Скрипт генерирующий список числительных в заданном диапазоне - в формате чисел и на немецком
*	Функция для сохранения полученных данных в текстовый файл

На этом этапе проект стал создавать впечатление, будто он уже может оказаться полезным и для других людей. Потому загрузил его в публичный репозиторий на GitHub. Буду рад, если он действительно кому-то пригодится.

<b>В планах:</b>
*	графический интерфейс
*	telegram-бот

<b>Файлы в проекте:</b>
*	core.py — здесь находятся функции, которые используются сразу несколькими модулями для обработки данных
*	cli.py - функции, используемые интерфейсом командной строки
*	german_numbers.py — простой интерфейс для конвертации чисел в строки с этими числами на немецком языке
*	german_examples.py — вывод списка случайных примеров с простыми математическими операциями — числами и на немецком.
*	german_dates.py — список случайных дат в нескольких форматах: ДД.ММ.ГГГ. американский, российский, немеций и полностью немецкими словами
*   german_numerals_list.py - список числительных в формате чисел и на немецком

<b>Если вы не знаете, как запускать python-скрипты:</b>
1.	Скачайте содержимое репозитория: «Clone or download» → «Download ZIP»
2.	Установите интерпретатор Python версии 3.x, если в вашей системе он не установлен. 
3.	Запустите командную строку в папке, где находятся скрипты
4.	Запускайте их командами вроде «python3 german_examples.py» или «python3 german_dates.py»

Интерпретатор, в зависимости от настроек в вашей операционной системе, может вызываться иначе — например «python» или «py».

