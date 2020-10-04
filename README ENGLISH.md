<b>A short story of this project</b>

I started to learn Pyton on my own almost in the same time with German.
My friend and I decided to work together, call each other on video, check each other out and come up with small tasks. To better remember numbers, we gave each other simple examples of addition and subtraction with numbers up to 100. We asked and answered in German, but found that while one answered, the other might forget what he/she asked. Or one might have made a mistake either in the calculations or in the translation, and the other might not have noticed that or made a mistake too. I came up with a solution — I wrote a script that generated a list of examples with answers — so we began to stumble much less, and this practice itself turned out to be very useful and effective. I can recommend it to anyone who is learning new languages.

<b>What I added later:</b>
* generation of multiplication and division examples
* a function that converts positive natural numbers to string values with the same number written in German words
* using this function — output examples both in numerical form and in German words
* one more script that generates dates — to study them in the same form. This script has a function in ordinal numbers, but only up to 31
* more intelligent results: the likelihood of repeated numbers and dates kept to a minimum. The output of mathematical operations and centuries is also balanced

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

<b>if you don't know how to run python scripts:</b>
1. Download the contents of the repository: "Clone or download" → "Download ZIP»
2. Install the Python interpreter version 3.x if it is not installed on your system.
3. Run the command prompt in the folder where the scripts are located
4. Run them with commands like "python3 german_examples.py" or "python3 german_dates.py»

Depending on the settings in your operating system, the interpreter may be called differently — for example, "python" or "py".
