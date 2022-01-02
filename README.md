# PythonSRS
A weekend project of mine, inspired by SRS programs I personally use such as Anki and Quizlet.
The main functionality of the program is a digital implementation of flashcards.


The "cards" are stored one-per-line in a tsv (tab-separated values) file, in the format: "word-score  JP-word EN-word"

The above mentioned "word score" is used to prioritize less-familiar words during review. Scores are updated (written to the tsv file) when the user clicks "stop review", or "Exit" at the end of the review session.

I used python, and python's tkinter module, to build this project. Python's seamless file integration and tkinter's simplicity helped me cut down on busywork & start on implementation ASAP.

There are still a number of features I'd like to implement (see wiki), but the core functionality is complete, and the program is currently usable as a simple SRS.
