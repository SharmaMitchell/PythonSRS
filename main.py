import tkinter as tk
from random import randint
window = tk.Tk()
window.title("SRS v1")
window.geometry("800x425")


with open("JapaneseWords.tsv") as f:
	deck = f.readlines()

def reset():
	startStop.config(text="Start Review",command=review)

def review():
	decksize.configure(text="{} Words to Review".format(len(deck)))
	nextButton.pack_forget()
	backWord.pack_forget()

	if(len(deck) == 0):
		done = tk.Label(text="Done reviewing! Good job!",font=("Arial",16))
		done.pack()
		frontWord.pack_forget()
		startStop.pack_forget()
		exit = tk.Button(text="Exit",command=window.destroy)
		exit.pack()
		return

	startStop.config(text="Stop Review", command=reset)
	random_index = randint(0,len(deck)-1)
	wordJP, wordEN = deck[random_index].split("\t")
	frontWord.config(text=wordJP)
	print(wordJP)

	def showAns():
		backWord.config(text=wordEN)
		backWord.pack()
		showAnswer.pack_forget()
		nextButton.pack()

		deck.pop(random_index)

	showAnswer = tk.Button(text="Show Answer",command=showAns)
	showAnswer.pack()



hello = tk.Label(text="Welcome to the SRS!")
hello.pack()

decksize = tk.Label(text="{} Words to Review".format(len(deck),font=("Arial",12)))
decksize.pack()

startStop = tk.Button(text="Start Review",command=review)
startStop.pack()

frontWord = tk.Label(text="",font=("Arial",18))
frontWord.pack()

backWord = tk.Label(text="",font=("Arial",14))
backWord.pack()

nextButton = tk.Button(text="Next Word",command=review)


tk.mainloop()