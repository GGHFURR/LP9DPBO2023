from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image



hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3,1300,"apartemen.jpeg"))
hunians.append(Rumah("Sekar MK", 5, 2,900,"rumah.jpeg"))
hunians.append(Indekos("Bp. Romi",1,100,"Cahya",900,"kosan.jpg"))
hunians.append(Rumah("Satria", 1, 2,900,"rumah.jpeg"))

root = Tk()
root.title("Praktikum DPBO Python")

listGambar = []

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    #d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    # d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail(), justify=CENTER).grid(row=0, column=0, sticky="w")
    image = Image.open('images/' + hunians[index].get_image()) 
    image = image.resize((200, 200)) 
    image = ImageTk.PhotoImage(image)
    listGambar.append(image)
    image_label = Label(d_frame, image=image)
    image_label.grid(row=1, column=0)

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def datalist():
    landingPage.destroy()   
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

label = Label(root, text="Selamat Datang Ges", font=('Arial', 16))
label.pack()
landingPage = Frame(root,padx=10,pady=10)
landingPage.pack(padx=5, pady=5)

image = Image.open('images/meme.jpg') 
image = image.resize((200, 200)) 
image = ImageTk.PhotoImage(image)
image_label = Label(landingPage, image=image)
image_label.pack()
button = Button(landingPage, text='DAFTAR RESIDEN', font=('Arial', 16), command=datalist)
button.pack(side=RIGHT)





root.mainloop()
