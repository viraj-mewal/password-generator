from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import pyperclip
import os

class window():
	def __init__(self):
		self.win = Tk()
		self.width = 500
		self.height = 200
		self.win.geometry(str(self.width) + "x" + str(self.height))
		self.win.title("Password Generator")
		self.win.iconbitmap(os.getcwd() + "\\password.ico")
		self.win.configure(bg="black")
		self.win.resizable(False, False)
		self.draw()
		self.win.mainloop()

	def check_password_strength_and_length(self):
		try:
			self.length = self.var.get()
		except:
			messagebox.showerror("Error", "Please enter length of the password in numbers only")
			return True
		self.mode = self.radio_value.get()
		self.password = self.main(self.length, self.mode)
		self.password_show.delete(0, "end")
		self.password_show.insert(0, self.password)

	def copy(self):
		pyperclip.copy(self.password)
		messagebox.showinfo("Info", "Password was copied")

	def save(self):
		try:
			self.filetext = self.password_show_value.get()
			self.file = filedialog.asksaveasfile(initialdir=os.getcwd(),
											defaultextension='.txt',
											filetype=[
											("text file",".txt"),
											("All files",".*")
											])
			self.file.write("Password :- " + self.filetext)
			self.file.close()
		except:
			messagebox.showinfo("Info", "No password to save")


	def draw(self):
		# heading

		self.heading = Label(self.win, text="Password Generator", font=("Comic Sans MS",20,"bold"), fg="white", bg="black")
		self.heading.place(x=self.width//2-120, y=5)

		# lenght input

		# -> Label

		self.length_label = Label(self.win, text="Length :-", bg="black", fg="white", font=("Comic Sans MS",20,"bold"))
		self.length_label.place(x=5, y=70)

		# password strength

		self.var = IntVar()
		self.length = Entry(self.win, textvariable=self.var, width=5, bg="black", fg="white", font=("Helvetica",20,"bold"))
		self.length.place(x=150, y=75)

		self.radio_value = StringVar()
		self.weak = Radiobutton(self.win, text="Weak", bg="black", fg="white", activebackground="light green", font=("Comic Sans MS",16,"bold"), variable=self.radio_value, value="weak", command=self.check_password_strength_and_length)
		self.weak.place(x=230, y=70)

		self.good = Radiobutton(self.win, text="Good", activebackground="light green", bg="black", fg="white", font=("Comic Sans MS",16,"bold"), variable=self.radio_value, value="good", command=self.check_password_strength_and_length)
		self.good.place(x=320, y=70)

		self.strong = Radiobutton(self.win, text="Strong", activebackground="light green", bg="black", fg="white", font=("Comic Sans MS",16,"bold"), variable=self.radio_value, value="strong", command=self.check_password_strength_and_length)
		self.strong.place(x=400, y=70)


		self.password_show_label = Label(self.win, text="Password :-", font=("Comic Sans MS",20,"bold"), bg="black", fg="white")
		self.password_show_label.place(x=10, y=self.height-60)

		self.password_show_value = StringVar()
		self.password_show = Entry(self.win, textvariable=self.password_show_value, font=("Helvetica",25,"bold"), width=7, bg="black", fg="white")
		self.password_show.place(x=self.width//2-70, y=self.height-55)

		self.copy_button = Button(self.win, text="Copy", font=("Baskerville",15,"bold"), fg="black", bg="yellow", activebackground="pink", command=self.copy)
		self.copy_button.place(x=self.width-170, y=self.height-55)

		self.save_button = Button(self.win, text="Save", font=("Baskerville",15,"bold"), fg="black", bg="aqua", activebackground="light green", command=self.save)
		self.save_button.place(x=self.width-90, y=self.height-55)



	def main(self, length, mode):
		self.length = length
		self.mode = mode
		self.lower = "abcdefghijklmnopqrstuvwxyz"
		self.capital_lower_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		self.capital_lower_digits_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
		self.password = ""

		if self.mode == "weak":
			for i in range(self.length):
				self.random_characters = random.choice(self.lower)
				self.password = self.password + str(self.random_characters)
		
		elif self.mode == "good":
			for i in range(self.length):
				self.random_characters = random.choice(self.capital_lower_digits)
				self.password = self.password + str(self.random_characters)

		elif self.mode == "strong":
			for i in range(self.length):
				self.random_characters = random.choice(self.capital_lower_digits_symbols)
				self.password = self.password + str(self.random_characters)

		return self.password

if __name__ == '__main__':
	win = window()