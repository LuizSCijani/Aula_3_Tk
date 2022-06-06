from tkinter import *

#criar a janela/window
janela = Tk()

#criar a função
def Converte():
    if entry.get().isnumeric():
        label2['text'] = float(entry.get()) * 1.8 + 32
    else:
        label2['text'] = 'Valor Invalido!'

#criar os widgets
label1 = Label(janela, text='Cº', font='Arial 17')
label2 = Label(janela, text=0, font='Arial 16')
entry = Entry(janela, font='Arial 20')
btn = Button(janela, text='Converte ºF', font='Arial 17', command=Converte)

#organizar os widgets/layout
label1.grid(row=0, column=0)
entry.grid(row=0, column=1)
btn.grid(row=1, column=0)
label2.grid(row=1, column=1)

#executar a janela
janela.mainloop()