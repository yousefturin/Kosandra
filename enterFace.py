from tkinter import *

root = Tk()
root.title('Kosandra')
root.iconbitmap('C:/Users/ENVY/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/mic.png')
root.geometry("500x500")


mic_btn = PhotoImage(file='C:/Users/ENVY/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/mic.png')
# img_label = Label(image=mic_btn, background="black")
Label(text="Kosandra", font=("Arial", 32, "bold"), fg="black").pack()


# img_label.pack(pady=20)

mic = Button(root, image=mic_btn, command='', borderwid=0)
mic.pack(padx=10, pady=10)

mainloop()
