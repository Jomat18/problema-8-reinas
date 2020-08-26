from Tkinter import *
import tkMessageBox
import time

class Problema:
    def __init__(self):
        self.N = 8
        self.n_soluciones = 0
        self.velocidad = 0.001 #0.01  #Valor velocidad mas chico, mas rapido las reinas en la simulacion 
        self.tabla = [ [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]         


    def reiniciar(self):
        for i in range(self.N): 
            for j in range(self.N):         
                self.tabla[i][j] = 0

    def es_seguro(self, tablero, fila, columna, manual=False): 

        if not manual:
                time.sleep(self.velocidad)
                t.agregar_reina(1, fila, columna)    
                t.tablero.update()

        for i in range(self.N):
            if tablero[fila][i] == 1: 
                return False

        for i in range(self.N): 
            if tablero[i][columna] == 1: 
                return False        

        for i, j in zip(range(fila-1, -1, -1), 
                        range(columna+1, self.N, 1)): 
            if tablero[i][j] == 1: 
                return False

        for i, j in zip(range(fila-1, -1, -1), 
                        range(columna-1, -1, -1)): 
            if tablero[i][j] == 1: 
                return False

        for i, j in zip(range(fila+1, self.N, 1), 
                        range(columna+1, self.N, 1)): 
            if tablero[i][j] == 1: 
                return False                

        for i, j in zip(range(fila+1, self.N, 1), 
                        range(columna-1, -1, -1)): 
            if tablero[i][j] == 1: 
                return False

        return True

    def solucion(self, tablero, columna): 

        if columna >= self.N:
            self.n_soluciones = self.n_soluciones + 1
            print ("Solucion N: ", self.n_soluciones)
            for i in range(self.N):          
                print (self.tabla[i])

            return False
    
        for i in range(self.N): 

            if self.es_seguro(tablero, i, columna): 
                
                tablero[i][columna] = 1

                soluciones = self.solucion(tablero, columna + 1) 
                    
                if soluciones or self.n_soluciones==92:
                    return True

                tablero[i][columna] = 0
    
                time.sleep(self.velocidad)
                t.agregar_reina(0, i, columna)    
                t.tablero.update()
                
            else:
                
                time.sleep(self.velocidad)
                t.agregar_reina(0, i, columna)    
                t.tablero.update()    
                
        return False    



class Dibujar(Frame):
    def __init__(self, parent, reina, filas=8, columnas=8, size=75, color1="white", color2="black"):

        self.filas = filas
        self.columnas = columnas
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.reina = reina
        self.problema = Problema()
        self.img = [] 
        self.n_reinas = 0
        self.manual = False

        tablero_ancho = columnas * size
        tablero_alto = filas * size

        Frame.__init__(self, parent)
        self.tablero = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=tablero_ancho, height=tablero_alto)
        self.tablero.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        color = self.color2
        for fila in range(self.filas):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columnas):
                x1 = (col * self.size)
                y1 = (fila * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.tablero.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="cuadrado")
                color = self.color1 if color == self.color2 else self.color2

        self.tablero.tag_lower("cuadrado")  

        self.tablero.bind("<1>", self.jugar)


    def jugar(self, event):

        if self.manual:
            if self.n_reinas<8:
                for fila in range(self.filas):
                    for col in range(self.columnas):
                        x1 = (col * self.size)
                        y1 = (fila * self.size)
                        x2 = x1 + self.size
                        y2 = y1 + self.size

                        if (x1<event.x<x2 and y1<event.y<y2):

                            if self.problema.es_seguro(self.problema.tabla, fila, col, True):
                                self.problema.tabla[fila][col] = 1
                                self.agregar_reina(1, fila, col)
                                self.n_reinas = self.n_reinas + 1
                                if self.n_reinas==8:
                                    tkMessageBox.showinfo("Ganaste", "8-reinas")                                     

                            else:
                                tkMessageBox.showinfo("Movimiento", "Posicion incorrecta")      

                            return       

    def activar_jugar(self):
        self.manual = True                  
            

    def mostrar(self):
        self.reiniciar()
        self.manual = False
        self.problema.n_soluciones = 0
        self.problema.solucion(self.problema.tabla, 0)  

    def reiniciar(self):
        self.manual = False
        for i in range(len(self.img)):             
            self.tablero.delete(self.img[i])

        del self.img[:]           
        self.problema.reiniciar()
        self.n_reinas = 0                                    

    def agregar_reina(self, colocar, fila=0, columna=0):

        if colocar==1:
            img = self.tablero.create_image(0,0, image=self.reina)
            self.img.append(img)
            x0 = (columna * self.size) + int(self.size/2)
            y0 = (fila * self.size) + int(self.size/2)
            self.tablero.coords(self.img[len(self.img)-1], x0, y0)        
            
        else:    
            self.tablero.delete(self.img[len(self.img)-1])
            del self.img[-1]


if __name__ == "__main__":

    root = Tk()
    root.title("Problema 8: reinas")
    root.geometry("750x610")
    root.configure(background='black')
    root.resizable(0,0)

    #ancho = root.winfo_screenwidth()
    #alto = root.winfo_screenheight()

    reina = PhotoImage(file="reina.ppm")
    t = Dibujar(root, reina)
    t.pack(side="right", fill="both", expand="true", padx=4, pady=4)

    iniciar = Button(root, text="Jugar", command=t.activar_jugar, width=50, fg="black")
    iniciar.pack( side = LEFT)

    reiniciar = Button(root, text="Reiniciar", command=t.reiniciar, fg="black").place(x=0, y=100, width=140)

    soluciones = Button(root, text="Soluciones", command=t.mostrar, fg="black").place(x=0, y=200, width=140)
                    
    root.mainloop()
