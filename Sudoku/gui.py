import tkinter as tk
from solve import Solve

DIM_COL = 75
NUM_COL = 9


def risolvi():
    lista=[]
    print(lista)
    for i in range(NUM_COL):
        lista.append([])
        for j in range(NUM_COL):
            val = str(listaTexts[i][j].get())
            if val == "":
                num = 0
            else:
                num = int(val)
            lista[i].append(num)

    """lista = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 4, 1, 6, 2, 9, 0, 0], [2, 0, 0, 0, 3, 0, 0, 7, 0],
             [0, 9, 0, 0, 0, 0, 0, 6, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 6, 0, 0, 1, 3, 0, 0, 7],
             [9, 0, 6, 0, 0, 5, 0, 0, 0], [8, 5, 0, 7, 0, 6, 4, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 0]]"""

    print(lista)
    solve = Solve(lista)
    tab = solve.tabella

    for i in range(NUM_COL):
        for j in range(NUM_COL):
            listaTexts[i][j].delete(0, "end")
            listaTexts[i][j].insert(0, str(tab[i][j]))
    print(tab)
    
def pulisci():
    for i in range(NUM_COL):
        for j in range(NUM_COL):
            listaTexts[i][j].delete(0, "end")


master = tk.Tk()
master.geometry(str(DIM_COL*NUM_COL+200) + "x" + str(DIM_COL*NUM_COL))

listaTexts = []
for i in range(NUM_COL):
    listaTexts.append([])
    for j in range(NUM_COL):
        testo = tk.Entry(master=master, bd=5, font=("Arial", 32), justify='center')
        testo.place(width = DIM_COL, height = DIM_COL, x = j * DIM_COL, y = i * DIM_COL)

        listaTexts[i].append(testo)

bottoneRis = tk.Button(master=master, text="Risolvi", command=risolvi, justify="center")
bottoneRis.place(width=200, height=75, x = DIM_COL*9, y=DIM_COL*3)

bottonePul = tk.Button(master=master, text="Pulisci", command=pulisci, justify="center")
bottonePul.place(width=200, height=75, x =DIM_COL*9, y=DIM_COL*5)
master.mainloop()


