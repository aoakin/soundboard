from tkinter import *
import tkinter
import winsound

root = tkinter.Tk()

root.title("Soundboard")
root.geometry("400x120")
root.iconbitmap(r'c:\Users\Ayo\Desktop\programming\python\soundboard\icon.ico')
root.resizable(width=False, height=False)

def bass1():
	b1 = winsound.PlaySound("kick1.wav", winsound.SND_FILENAME)
def hihat1():
	h1 = winsound.PlaySound("hihat1.wav", winsound.SND_FILENAME)
def snare1():
	s1 = winsound.PlaySound("snare1.wav", winsound.SND_FILENAME)
def beat1():
	sb1 = winsound.PlaySound("kreamy.wav", winsound.SND_FILENAME)
def beat2():
	sb2 = winsound.PlaySound("sample_beat.wav", winsound.SND_FILENAME)

button_bass = Button(root, relief = "groove", text = "KICK", command = bass1)
button_bass.place(x = 5,y = 30)

button_hihat = Button(root, relief = "groove", text = "HI HAT", command = hihat1)
button_hihat.place(x = 5, y = 60)

button_snare = Button(root, relief = "groove", text = "SNARE", command = snare1)
button_snare.place(x = 5, y = 90)

button_beat1 = Button(root, relief = "groove", text = "SAMPLE BEAT 1", command = beat1)
button_beat1.place(x = 300, y = 30)

button_beat2 = Button(root, relief = "groove", text = "SAMPLE BEAT 2", command = beat2)
button_beat2.place(x = 300, y = 60)

root.mainloop()