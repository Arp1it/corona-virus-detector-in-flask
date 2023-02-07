from tkinter import *
from tkinter.messagebox import showinfo
import pickle


class Corona(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("755x600")

        with open('model.pkl', 'rb') as file:
            self.clf = pickle.load(file)

    def sub(self):
        print(self.s)
        # Code for inference
        infProb = self.clf.predict_proba([[int(self.var5.get()), int(self.var3.get()), int(self.var2.get()), int(self.var6.get()), int(self.var4.get())]])[0][1]

        showinfo("Probability of infection", f"{self.var} Probability of Infection is {round(infProb*2, 5)}. Thanks for testing")

        print(infProb)
        # print(f"Hello World {str(int(infProb * 1000))}/1000")

    
    def form(self):
        H = Label(text = "Corona Testing", padx=20, pady=10, font="lucida 30 bold").grid()

        name = Label(text = "Patience Name", padx=20, pady=10).grid(row=1)
        Age = Label(text = "Age of Patience", padx=20, pady=10).grid(row=2)

        self.var = StringVar()
        self.var2 = StringVar()

        a = Entry(self, textvariable=self.var).grid(row=1, column=1)
        b = Entry(self, textvariable=self.var2).grid(row=2, column=1)

        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var6.set(" ")
        self.var5.set(" ")
        self.var3.set(" ")
        self.var4.set(" ")

        H = Label(text = "Do you have fever?", padx=20, pady=10, font="lucida 10 bold").grid(row=4)
        v = ["Yes", "No"]
        k = 1
        for i in v:
            self.s = Radiobutton(self, text = i, padx=10, pady=10, variable=self.var5,value=k).grid()
            k -= 1

        H = Label(text = "Do you have bodypain?", padx=20, pady=10, font="lucida 10 bold").grid(row=7)
        v = ["Yes", "No"]
        k = 1
        for i in v:
            self.s = Radiobutton(self, text = i, padx=10, pady=10, variable=self.var3,value=k).grid()
            k -= 1

        H = Label(text = "Do you have breathing problem?", padx=20, pady=10, font="lucida 10 bold").grid(row=10)
        v = ["Normal", "Less", "Sever"]
        k = -1
        for i in v:
            self.s = Radiobutton(self, text = i, padx=10, pady=10, variable=self.var4,value=k).grid()
            k += 1

        H = Label(text = "Do you have runny nose?", padx=20, pady=10, font="lucida 10 bold").grid(row=15)
        v = ["Yes", "No"]
        k = 1
        for i in v:
            self.s = Radiobutton(self, text = i, padx=10, pady=10, variable=self.var6,value=k).grid()
            k -= 1

        butt = Button(self, text="Submit", command=self.sub).grid(row=14, column=11)

if __name__=="__main__":
    Gui = Corona()

    Gui.form()

    Gui.mainloop()
