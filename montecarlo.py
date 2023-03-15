import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Montecarlo para Variables Aleatorias")
        
        # Crear los widgets
        self.label_n = tk.Label(self.master, text="Número de iteraciones:")
        self.entry_n = tk.Entry(self.master)
        self.label_resultado = tk.Label(self.master, text="Resultado:")
        self.button_calcular = tk.Button(self.master, text="Calcular", command=self.calcular)
        self.fig = Figure(figsize=(5, 4), dpi=100)
        
        self.grafica = self.fig.add_subplot(111)
        self.grafica.set_title("Gráfica de iteraciones")
        self.grafica.set_xlabel("Iteración")
        self.grafica.set_ylabel("Resultado")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        
        # Ubicar los widgets
        self.label_n.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)
        self.label_resultado.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.button_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def calcular(self):
        N = int(self.entry_n.get())
        resultados = self.montecarlo(N)
        resultado_final = resultados[-1]
        self.label_resultado.configure(text="Resultado: {}".format(resultado_final))
        self.grafica.clear()
        self.grafica.plot(resultados)
        self.canvas.draw()
        
    def montecarlo(self, N):
        sumatoria = 0
        resultados = []
        for i in range(N):
            x = random.uniform(0, 1) # generamos una variable aleatoria uniforme en el intervalo [0, 1]
            y = x ** 2 # función que queremos integrar
            sumatoria += y
            resultado_actual = sumatoria / (i+1)
            resultados.append(resultado_actual)
        return resultados

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
