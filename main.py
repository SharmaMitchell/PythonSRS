import tkinter as tk
from random import randint

window = tk.Tk()
window.title("SRS v1")
window.geometry("800x425")


with open("JapaneseWords.tsv") as f:
	deck = f.readlines() #store words (tab-separated) in an array of strings

reviewQueue = deck[:] # use [:] to copy all elements, rather than reference
#sort by score

def reset(): #clear all buttons from screen, when user clicks "stop review"
	startStop.config(text="Start Review",command=review)
	frontWord.pack_forget()
	backWord.pack_forget()
	correctButton.pack_forget()
	incorrectButton.pack_forget()
	showAnswer.pack_forget()

def close():
	f = open("JapaneseWords.tsv", "w")
	f.writelines(deck)
	f.close()
	window.destroy()

def review(): #review loop
	queueSize.configure(text="{} Words to Review".format(len(reviewQueue)))
	backWord.pack_forget()
	correctButton.pack_forget()
	incorrectButton.pack_forget()

	if(len(reviewQueue) == 0):
		done = tk.Label(text="Done reviewing! Good job!",font=("Arial",16))
		done.pack()
		frontWord.pack_forget()
		startStop.pack_forget()
		exit = tk.Button(text="Exit",command=close)
		exit.pack()
		return

	frontWord.pack()
	startStop.config(text="Stop Review", command=reset)
	random_index = randint(0,len(reviewQueue)-1)
	wordJP, wordEN, wordScore = reviewQueue[random_index].split("\t")
	frontWord.config(text=wordJP)
	#print(wordJP)

	def correct():
		word_index = deck.index(reviewQueue[random_index])
		deck[word_index] = "\t".join((wordJP, wordEN, str(int(wordScore)+1)))+"\n"
		#print(deck[word_index])
		reviewQueue.pop(random_index)
		review()
		return

	def incorrect():
		word_index = deck.index(reviewQueue[random_index])
		deck[word_index] = "\t".join((wordJP, wordEN, str(int(wordScore)-1)))+"\n"
		#print(deck[word_index])
		reviewQueue.pop(random_index)
		review()
		return

	correctButton.configure(command=correct)
	incorrectButton.configure(command=incorrect)

	def showAns():
		backWord.config(text=wordEN)
		backWord.pack()
		showAnswer.pack_forget()
		correctButton.pack()
		incorrectButton.pack()

	showAnswer.configure(command=showAns)
	showAnswer.pack()

hello = tk.Label(text="Welcome to the SRS!")
hello.pack()

queueSize = tk.Label(text="{} Words to Review".format(len(reviewQueue),font=("Arial",12)))
queueSize.pack()

startStop = tk.Button(text="Start Review",command=review)
startStop.pack()

frontWord = tk.Label(text="",font=("Arial",18))
#frontWord.pack()

backWord = tk.Label(text="",font=("Arial",14))
#backWord.pack()

showAnswer = tk.Button(text="Show Answer")

correctButton = tk.Button(text="Correct",command=review)
incorrectButton = tk.Button(text="Incorrect",command=review)


tk.mainloop()