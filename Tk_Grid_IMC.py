from tkinter import *

#criar a janela/window
janela = Tk()
janela.geometry('400x167+90+90')
janela.config(background='#B0C4DE')

#criar a função
def IMC():
    if entry1.get().replace('.', '', 1).isnumeric() and entry2.get().replace('.', '', 1).isnumeric():
        label3['text'] = float(entry1.get()) / (float(entry2.get())**2)
    else:
        label3['text'] = 'Valor Invalido!'

#criar os widgets
label1 = Label(janela, text='Peso:', font='Arial 20', background='#B0C4DE')
label2 = Label(janela, text='Altura:', font='Arial 20', background='#B0C4DE')
label3 = Label(janela, text=0, font='Arial 20')
entry1 = Entry(janela, font='Arial 18')
entry2 = Entry(janela, font='Arial 18')
btn1 = Button(janela, text='IMC', font='Arial 20', command=IMC)

#organizar os widgets/layout
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
btn1.grid(row=2, column=1)
label3.grid(row=3, column=1)

#executar a janela
janela.mainloop()