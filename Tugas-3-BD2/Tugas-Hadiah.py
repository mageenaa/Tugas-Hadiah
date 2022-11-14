import tkinter as tk                # Import tkinter untuk membuat aplikasi GUI (Graphical User Interface)
from time import strftime           # Import strftime untuk convert tanggal dan waktu kemudian merepresentasikannya sebagai string
from tkinter import ttk             # Import ttk untuk mengubah desain dari widget yang dihasilkan oleh tkinter
from tkinter.scrolledtext import ScrolledText       # Import scrolledtext untuk menghubungkan text widget dengan vertical scroll
from tkcalendar import Calendar         # Import Calendar untuk mendapatkan output kalender
from tkinter import *       # Import seluruh fungsi dan modul bawaan dalam library tkinter
from PIL import ImageTk, Image      # Import modul image dari library PIL untuk membuka file image
todos = {}      # Deklarasi todos sebagai dictionary

def detailTodo(cb = None):      # membuat fungsi none untuk pengembalian True apabila tidak ditemukan value apapun
    win = tk.Toplevel()     # membuat GUI dalam variabel win
    win.wm_title("Detail Kegiatan")
    win.configure(bg = '#1F7EA1')       # nambahin warna background pada output detailTodo
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text']
    selectedTodo = todos[tanggal][selectedIndex]
    judul = tk.StringVar(value = selectedTodo['Judul'])
                                                    ###################### 
                                                    ## Pembuatan widget ##
                                                    ######################
# menambah background color pada line 25, 26, 27, 30, dan 31
    tk.Label(win, text = "Tanggal\t\t:", bg = '#6FF7E8').grid(row = 0, column = 0, sticky="NW")        # sticky diubah jadi NW supaya letaknya ada di Top Left
    tk.Label(win, text = "{} | {}".format(tanggal, selectedTodo["Waktu"]), width = 38, bg = '#6FF7E8').grid(row = 0, column = 1, sticky = "NE", pady = 0)   # mengubah sticky menjadi NE supaya letaknya di Top Right, dan pady 3 untuk memberi jarak 3 px dengan baris lain
    tk.Label(win, text = "Judul\t\t:", bg = '#6FF7E8').grid(row = 1, column = 0, sticky="NW")          # sticky diubah jadi NW supaya letaknya ada di Top Left
# pada line 29 merubah state menjadi normal agar text terlihat jelas, menambahkan width dan bg
    tk.Entry(win, state = "normal", textvariable = judul, width = 45, bg = '#6FF7E8').grid(row = 1, column = 1, sticky = "NE", pady = 0)  # mengubah sticky menjadi NE supaya letaknya di Top Right, dan pady 3 untuk memberi jarak 3 px dengan baris lain
    tk.Label(win, text = "Keterangan\t:", bg = '#6FF7E8').grid(row = 2, column = 0, sticky="NW")     # sticky diubah jadi NW supaya letaknya ada di Top Left
    keterangan = ScrolledText(win, width = 30, height = 10, bg = '#6FF7E8')
    keterangan.grid(row = 2, column = 1, sticky = "NE", padx = 10)    # mengubah sticky menjadi NE supaya letaknya di Top Right, padx 10 untuk memperlebar output kolom keterangan, dan pady 3 untuk memberi jarak 3 px dengan baris lain
    keterangan.insert(tk.INSERT, selectedTodo["Keterangan"])
    keterangan.configure(state = "disabled")
    bg_univ = Image.open('bumi.png')        # membuka image yang sudah ada di github
    bg_end = ImageTk.PhotoImage(bg_univ)    # memberikan command ImageTk agar image dapat di proses oleh tkinter 
    win.geometry('1280x720')        # mengubah size output detailTodo
    tk.Label(win, image = bg_end).grid(row = 0, column = 2, columnspan = 3, rowspan = 3, padx = 5, pady = 5)    
    Label.pack()
def LoadTodos():        # membuat fungsi untuk load data yang sudah dibuat
    global todos 
    f = open('mytodo.dat','r')      # membaca file mode read only untuk melihat data-data yang sudah dibuat
    data = f.read()
    f.close()
    todos = eval(data)
    ListTodo()      # kembali ke fungsi ListTodo
def SaveTodos():    # membuat fungsi untuk menyimpan data yang dibuat
    f = open('mytodo.dat','w')      # membaca file mode write only untuk menyimpan data baru
    f.write(str(todos))
    f.close()
def delTodo():      # membuat fungsi untuk menghapus data yang sudah dibuat
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()
    todos[tanggal].pop(treev.item(selectedItem)['text'])        
    ListTodo()
def ListTodo(cb = None):        # membuat fungsi none untuk pengembalian True apabila tidak ditemukan value apapun
    for i in treev.get_children(): 
        treev.delete(i)
    tanggal = str(cal.selection_get())
    if tanggal in todos : 
        for i in range (len(todos[tanggal])): 
            treev.insert("","end",text = i, values = (todos[tanggal][i]['Waktu'], todos[tanggal][i]['Judul']))
def addTodo(win,key,jam,menit,judul,keterangan): 
    newTodo = {
        "Waktu":"{}:{}".format(jam.get(), menit.get()), 
        "Judul":judul.get(), 
        "Keterangan": keterangan.get("1.0", tk.END)
    }
    if key in todos: 
        todos[key].append(newTodo)
    else : 
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()
def AddForm():      # membuat fungsi untuk menambahkan detail kegiatan
    win = tk.Toplevel()
    win.configure(bg = '#1F7EA1')       # nambahin warna background pada output detailTodo
    win.wm_title("+")
    win.geometry('640x400')     # mengatur ukuran window detail kegiatan menjadi 640x400
    jam = tk.IntVar(value = 10)     # value default dari jam
    menit = tk.IntVar(value = 30)       # value default dari menit
    judul = tk.StringVar(value="")      # default judul dibuat kosong
    tk.Label(win, text="Waktu\t\t: ", bg = '#6FF7E8').grid(row=0, column = 0, sticky = 'NW') # menambahkan \t, bg, dan sticky
    tk.Spinbox(win, from_= 0, to = 23, textvariable = jam, width = 3, bg = '#6FF7E8').grid(row = 0, column = 1, columnspan = 3, rowspan = 4, sticky = 'N')  # menambahkan bg dan sticky
    tk.Spinbox(win, from_= 0, to = 59, textvariable = menit, width = 3, bg = '#6FF7E8').grid(row = 0, column = 2, columnspan = 3, rowspan = 4, sticky = 'NE')   # menambahkan bg dan sticky
    tk.Label(win, text = "Judul\t\t: ", bg = '#6FF7E8').grid(row = 1, column = 0, sticky = 'W')     # menambahkan \t, bg, dan sticky
    tk.Entry(win, textvariable = judul, bg = '#6FF7E8', width = 25).grid(row = 1, column = 2, columnspan = 1, sticky = 'E') # menambahkan bg, sticky, dan mengatur width agar lebih rapih 
    tk.Label(win, text = 'Keterangan\t: ', bg = '#6FF7E8').grid(row = 2, column = 0)       # menambahkan bg
    keterangan = ScrolledText(win, width = 20, height = 5, bg = '#6FF7E8')
    keterangan.grid(row = 3, column = 2)
    tanggal = str(cal.selection_get())
    tk.Button(win, text = "Tambah", command = lambda: addTodo(win, tanggal, jam, menit, judul, keterangan), bg = '#6FF7E8').grid(row = 6, columnspan = 3)
    bg_todo = Image.open('todolist.png')        # membuka image yang sudah ada di github
    bg_todo1 = ImageTk.PhotoImage(bg_todo)    # memberikan command ImageTk agar image dapat di proses oleh tkinter 
    tk.Label(win, image = bg_todo1).grid(row = 0, column = 6, columnspan = 5, rowspan = 5, padx = 8, pady = 8)    
    Label.pack()
def title():
    waktu = strftime("%H:%M")
    tanggal = str(cal.selection_get())
    root.title(tanggal + " | " + waktu + " | ")
    root.after(1000, title)
root = tk.Tk()
root.configure(bg = '#1F7EA1')  # nambahin warna background pada output title
cal = Calendar(root, font = "Verdana 20 italic", selectmode = 'day', locale = 'id_ID', cursor = 'hand2') #pada line ini kita bisa mengubah kalender mulai dari font, ukuran font, dan kursor sesuai keinginan)
cal.grid(row = 0, column = 0, sticky = 'W', rowspan = 100) #rowspan diubah agar tombolnya jaraknya berdekatan
cal.bind("<<CalendarSelected>>", ListTodo) #untuk mengikat antara calendar select dan fungsi listtodo
tanggal = str(cal.selection_get()) #mendeklarasi tanggal menjadi tipe data string
treev = ttk.Treeview(root) #memanggil treeview ke dalam variabel treev untuk mengubah desain UI dari GUI yang dibuat
treev.grid(row = 0, column = 1, sticky = 'WNE', rowspan = 1, columnspan = 2) #layouting bagan todo listnya, diubah menjadi 1 utk rowspan dan columnspan 2 agar pas
scrollBar = tk.Scrollbar(root, orient = "vertical", command = treev.yview) #membuat tombol scrollbar
scrollBar.grid(row = 0, column = 3, sticky = 'ENS') #menghapus rowspan karena tidak diperlukan
treev.configure(yscrollcommand = scrollBar.set)
treev.bind("<Double-1>", detailTodo)
treev["columns"] = ('1', '2')
treev["show"] = 'headings'
treev.column("1", width = 100)
treev.heading("1", text = "JAM")
treev.heading("2", text = "JUDUL")
#Menambahkan relief untuk mengubah bentuk button dan mengubah warna background dibawah.
#Mengubah ukuran width dan menambahkan ukuran height tombol
btnAdd = tk.Button (root, text='Tambah', width=30, height=2, bg='orange', fg='black', relief=GROOVE, command=AddForm)
btnAdd.grid(row = 4, column = 1, sticky = 'N')
btnDel = tk.Button (root, text='Hapus', width=30, height=2,bg='orange', fg='black', relief=GROOVE, command=delTodo)
btnDel.grid(row = 4, column = 2, sticky = 'N')
btnLoad = tk.Button (root, text='Load', width=30, height=2,bg='yellow', fg='black', relief=GROOVE, command=LoadTodos)
btnLoad.grid(row = 5, column = 1, sticky = 'S')
btnSave = tk.Button (root, text='Save', width=30, height=2,bg='yellow', fg='black', relief=GROOVE, command=SaveTodos)
btnSave.grid(row = 5, column = 2, sticky = 'S')
title()
root.mainloop()
