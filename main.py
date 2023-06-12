import tkinter as tk



class HomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.title("Aeolian Home Page")

        #main Label
        self.title_Label = tk.Label(self.root, text="Home Page", font=("Sans Serif",20))
        self.title_Label.pack(padx=20,pady=20)

        #frames
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)

        #instantiateButton Frames -- Note to self : change this to pictureboxes or add Animations on Hover sa Buttons
        self.btn1 = tk.Button(self.buttonFrame, text="ChatBot Chatbox", font=("Arial", 15))
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)  # basically means first column
        self.btn2 = tk.Button(self.buttonFrame, text= "Chatbot Voice Recognition", font=("Arial", 15))
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)  # basically means first column
        self.btn3 = tk.Button(self.buttonFrame, text= "Projector Converter", font=("Arial", 15))
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E)  # basically means first column

        self.buttonFrame.pack(fill="x", pady=40)



        self.root.mainloop()


HomePage()