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

