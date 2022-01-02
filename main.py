import tkinter as tk

window = tk.Tk()
window.title("SRS v1")
window.geometry("800x425")

with open("JapaneseWords.tsv") as f:
	deck = f.readlines() #store words (tab-separated) in an array of strings
reviewQueue = deck[:] # use [:] to copy all elements, rather than reference
reviewQueue.sort() #sort by score, first number

def writeToFile(): #Write deck to file to save progress
	f = open("JapaneseWords.tsv", "w")
	f.writelines(deck)
	f.close()

def addToFile():
	startStop.pack_forget()
	addWord.pack_forget()
	enterWord = tk.Label(text="Enter Japanese word/phrase:")
	enterWord.pack()
	inputtxt = tk.Entry(window)
	inputtxt.pack()
	words = ["0"] # 0 = starting "familiarity score"
	
	def getWords():
		if(len(words)<3):
			words.append(inputtxt.get())
		if(len(words)==2):
			enterWord.configure(text="Enter English definition:")
		if(len(words)==3): #add to deck
			newWord = "\t".join(words)
			deck[-1] += "\n"
			deck.append(newWord)
			reviewQueue.insert(0,newWord) #add to front of review queue
			enterWord.pack_forget()
			inputtxt.pack_forget()
			enterButton.pack_forget()
			reset()

	enterButton = tk.Button(text="Enter", command=getWords)
	enterButton.pack()
	return

def reset(): #clear all buttons from screen, when user clicks "stop review"
	queueSize.configure(text="{} Words to Review".format(len(reviewQueue)))
	startStop.config(text="Start Review",command=review)
	startStop.pack()
	addWord.pack()
	frontWord.pack_forget()
	backWord.pack_forget()
	correctButton.pack_forget()
	incorrectButton.pack_forget()
	showAnswer.pack_forget()
	writeToFile() #also writing to file when user clicks "Stop Review", to save progress

def close():
	writeToFile()
	window.destroy()

def review(): #review loop
	queueSize.configure(text="{} Words to Review".format(len(reviewQueue)))
	backWord.pack_forget()
	correctButton.pack_forget()
	incorrectButton.pack_forget()
	addWord.pack_forget()

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
	queue_index = 0 #first word in queue
	wordScore, wordJP, wordEN = reviewQueue[queue_index].split("\t")
	frontWord.config(text=wordJP)

	def correct():
		word_index = deck.index(reviewQueue[queue_index])
		deck[word_index] = "\t".join((str(int(wordScore)+1), wordJP, wordEN))#+"\n"
		reviewQueue.pop(queue_index)
		review()
		return

	def incorrect():
		word_index = deck.index(reviewQueue[queue_index])
		deck[word_index] = "\t".join((str(int(wordScore)-1), wordJP, wordEN))#+"\n"
		reviewQueue.pop(queue_index)
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

hello = tk.Label(text="Welcome to the SRS!", font=("Arial",12))
hello.pack()

progressLabel = tk.Label(text="Progress saves after clicking 'Exit', 'Stop Review', or adding a card.")
progressLabel.pack()

queueSize = tk.Label(text="{} Words to Review".format(len(reviewQueue)),font=("Arial",12))
queueSize.pack()

startStop = tk.Button(text="Start Review",command=review)
startStop.pack()

addWord = tk.Button(text="Add Word",command=addToFile)
addWord.pack()

frontWord = tk.Label(text="",font=("Arial",18))

backWord = tk.Label(text="",font=("Arial",14))

showAnswer = tk.Button(text="Show Answer")

correctButton = tk.Button(text="Correct",command=review)
incorrectButton = tk.Button(text="Incorrect",command=review)

tk.mainloop()