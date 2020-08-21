import numpy as np

class Solve:

    def __init__(self, gr):
        self.tabella = []
        self.NUM_COLS = 9
        self.NUMS = list(range(1, 10))

        self.griglia = gr.copy()

        self.possibilita()
        for self.iter in range(20):
            print(self.iter)
            self.numDaSolo()
            self.controllaOrizzontali()
            self.controllaVerticali()
            self.controllaQuadrante()
            #self.tabella = self.griglia.copy()

        self.tabella = self.griglia.copy()
       # print(self.griglia)

    def guardaPossibilita(self, i, j):
        poss = []

        for num in self.NUMS:
            if num in self.tabella[i]:
                continue

            if num in np.array(self.tabella).transpose()[j]:
                continue

            if num in np.array(self.tabella)[i - i%3 : i - i%3 +3, j - j%3 : j - j%3 +3]:
                continue

            poss.append(num)

        return poss

    def possibilita(self):
        self.tabella = self.griglia.copy()
        gr = []

        for i in range(self.NUM_COLS):
            gr.append([])
            for j in range(self.NUM_COLS):
                if self.tabella[i][j] == 0 or type(self.tabella[i][j]) == list:
                    poss = self.guardaPossibilita(i, j)
                    gr[i].append(poss)
                else:
                    gr[i].append(self.tabella[i][j])

        self.griglia = gr.copy()

    def numDaSolo(self):
        for i in range(self.NUM_COLS):

            for j in range(self.NUM_COLS):
                if type(self.griglia[i][j]) == list and len(self.griglia[i][j]) == 1:
                    self.griglia[i][j] = self.griglia[i][j][0]
                    self.possibilita()
                    self.numDaSolo()

    def controllaOrizzontali(self):
        for i in range(self.NUM_COLS):

            poss = dict().fromkeys(self.NUMS, 0)            #dizionario con i num da 0 a 9 inizializzati a 0
            for j in range(self.NUM_COLS):
                if type(self.griglia[i][j]) == list:
                    for num in self.griglia[i][j]:          #incrementa il dizionario se il num è possibile
                        poss[num] += 1

            numDaInserire = [n for n in poss.keys() if poss[n] == 1]    #verifica se un num compare da solo

            for n in numDaInserire:
                for j in range(self.NUM_COLS):                          #sostituisce la lista dei possibili con il num reale
                    if type(self.griglia[i][j]) == list and n in self.griglia[i][j]:
                        self.griglia[i][j] = n
                        self.possibilita()


    def controllaVerticali(self):
        gr = np.array(self.griglia).transpose().tolist()
        for i in range(self.NUM_COLS):

            poss = dict().fromkeys(self.NUMS, 0)  # dizionario con i num da 0 a 9 inizializzati a 0
            for j in range(self.NUM_COLS):
                if type(gr[i][j]) == list:
                    for num in gr[i][j]:  # incrementa il dizionario se il num è possibile
                        poss[num] += 1

            numDaInserire = [n for n in poss.keys() if poss[n] == 1]  # verifica se un num compare da solo

            for n in numDaInserire:
                for j in range(self.NUM_COLS):  # sostituisce la lista dei possibili con il num reale
                    if type(gr[i][j]) == list and n in gr[i][j]:
                        gr[i][j] = n
                        self.griglia = np.array(gr).transpose().tolist()
                        self.possibilita()

    def controllaQuadrante(self):
        gr = np.array(self.griglia)

        for i in range(0, self.NUM_COLS, 3):
            for j in range(0, self.NUM_COLS, 3):
                quad = gr[i - i%3 : i - i%3 +3, j - j%3 : j - j%3 +3].flatten().tolist()

                poss = dict().fromkeys(self.NUMS, 0)
                for nums in quad:
                    if type(nums) == list:
                        for num in nums:
                            poss[num] += 1

                numDaInserire = [n for n in poss.keys() if poss[n] == 1]

                for n in numDaInserire:
                    for k in quad:
                        if type(k) == list and n in k:
                            k = n
                            l = np.array(quad).reshape((3, 3))
                            gr = np.array(self.griglia)
                            gr[i - i%3 : i - i%3 +3, j - j%3 : j - j%3 +3] = l
                            self.griglia = gr.tolist()

    