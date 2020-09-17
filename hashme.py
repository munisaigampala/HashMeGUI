#! python2
__author__ = "Muni Sai G"
from Tkinter import *
import tkMessageBox
import hashlib

class windows():
	def __init__(self,master):
		self.varMD4=BooleanVar()
		self.varMD5=BooleanVar()
		self.varNTLM=BooleanVar()
		self.varSHA1=BooleanVar()
		self.opvarMD4=StringVar()
		self.opvarMD5=StringVar()
		self.opvarNTLM=StringVar()
		self.opvarSHA1=StringVar()
		# Frame Configuration Part
		master.resizable(width=False,height=False)
		master.title("HashMe")
		master.geometry("370x170")
		#master.iconbitmap(default='icon.ico')
		
		
		#Frame Content
		frame = Frame(master)
		frame.grid(row=0)
		
		self.labelUserInput = Label(master,text="   Your Text")
		self.labelUserInput.grid(row=0,column=0)
		self.labelEmpty = Label(master,text="   ")
		self.labelEmpty.grid(row=0,column=1)
		self.entryUserInput = Entry(master,width=43)
		self.entryUserInput.grid(row=0,column=2)
		
		
		self.labelMD4 = Checkbutton (master, text="MD 4",variable=self.varMD4,command=self.HashMe)
		self.labelMD4.select()
		self.labelMD4.grid(row=2,column=0,sticky=S)
		self.entryMD4 = Entry(master,width=44,textvariable=self.opvarMD4)
		self.entryMD4.config(state='readonly')
		self.entryMD4.grid(row=2,column=2)
		
		self.labelMD5 = Checkbutton (master, text="MD 5",variable=self.varMD5,command=self.HashMe)
		self.labelMD5.select()
		self.labelMD5.grid(row=3,column=0,sticky=S)
		self.entryMD5 = Entry(master,width=44,textvariable=self.opvarMD5)
		self.entryMD5.config(state='readonly')
		self.entryMD5.grid(row=3,column=2)
		
		self.labelNTLM = Checkbutton (master, text="NTLM",variable=self.varNTLM,command=self.HashMe)
		self.labelNTLM.select()
		self.labelNTLM.grid(row=4,column=0,sticky=S)
		self.entryNTLM = Entry(master,width=44,textvariable=self.opvarNTLM)
		self.entryNTLM.config(state='readonly')
		self.entryNTLM.grid(row=4,column=2)
		
		self.labelSHA1 = Checkbutton (master, text="SHA1",variable=self.varSHA1,command=self.HashMe)
		self.labelSHA1.select()
		self.labelSHA1.grid(row=5,column=0,sticky=S)
		self.entrySHA1 = Entry(master,width=44,textvariable=self.opvarSHA1)
		self.entrySHA1.config(state='readonly')
		self.entrySHA1.grid(row=5,column=2)
		
		buttonSubmit = Button(master,text='HashMe...',command=self.HashMe)
		buttonSubmit.grid(row=6,column=2,columnspan=2)
		
		
		
	def HashMe(self):
		inp=self.entryUserInput.get()
		if not self.varMD4.get() and not self.varMD5.get() and not self.varNTLM.get() and not self.varSHA1.get():
			tkMessageBox.showinfo("Selection Required", "Please Select an Algorithm")
		else:	
			if self.varMD4.get():
				op=hashlib.new('md4',inp).hexdigest()
				self.opvarMD4.set(op)
			if self.varMD5.get():
				op=hashlib.new('md5',inp).hexdigest()
				self.opvarMD5.set(op)
			if self.varNTLM.get():
				op=hashlib.new('md4',inp.encode('utf-16le')).hexdigest()
				self.opvarNTLM.set(op)
			if self.varSHA1.get():
				op=hashlib.new('sha1',inp).hexdigest()
				self.opvarSHA1.set(op)
			if not self.varMD4.get():
				self.opvarMD4.set('')
			if not self.varMD5.get():
				self.opvarMD5.set('')
			if not self.varNTLM.get():
				self.opvarNTLM.set('')
			if not self.varSHA1.get():
				self.opvarSHA1.set('')
		
		
root = Tk()
win = windows(root)
root.mainloop()