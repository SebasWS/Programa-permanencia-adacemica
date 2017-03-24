# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import Tkinter as tk
import ttk

#Definición de parámetros para los estudiantes:



LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Software de ayuda para la permanencia en educación superior")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Estudiante1, Estudiante2, Estudiante3):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="\n \n \n Bienvenido \n \n \n", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Estudiante1",
                            command=lambda: controller.show_frame(Estudiante1))
        button.pack()

        button2 = ttk.Button(self, text="Estudiante2",
                            command=lambda: controller.show_frame(Estudiante2))
        button2.pack()

        button3 = ttk.Button(self, text="Estudiante3",
                            command=lambda: controller.show_frame(Estudiante3))
        button3.pack()
        
        label = tk.Label(self, text="\n \n \n \n \n \n Este software estima la probabilidad de que un estudiante que se encuentra \n adelantando sus estudios en una institución de educación superior deserte. \n Para ello se han usado varias referencias estadisticas, las cuales han permitido \n llegar a un promedio ponderado donde las diferentes variables que lo componen \n tienen diferentes porcentajes de influencia en función de lo que los estudios dicen."
        , font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


class Estudiante1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Estadisticas Estudiante 1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Adrian Santiago Gamboa Giraldo", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Sexo: Masculino", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Código: 3625395766", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Regresar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,10,15,10,11,14,17,20])

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        label = tk.Label(self, text="\n \n \n La probabilidad ha sido calculada como un promedio ponderado de varias variables que \n influyen en la permanencia estudiantil tales como el estado de animo del estudiante, \n su situación económica, promedio académico entre otros. De 0-15 se considera pro- \n babilidad baja, de 15-30 se considera probabilidad media-baja, de 30 a 55 se considera \n probabilidad media, de 55 a 70 se considera probabilidad media-alta, de 70 a 100 se con- \n sidera probabilidad alta. Para esta demostración se ha tomado un periodo de 8 semestres.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)



class Estudiante2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Estadisticas Estudiante 2", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Carlos Andres Pedrazo Piedrahita", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Sexo: Masculino", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Código: 3562051896", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        button1 = ttk.Button(self, text="Regresar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[10,5,4,3,5,6,7,3])

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        label = tk.Label(self, text="\n \n \n La probabilidad ha sido calculada como un promedio ponderado de varias variables que \n influyen en la permanencia estudiantil tales como el estado de animo del estudiante, \n su situación económica, promedio académico entre otros. De 0-15 se considera pro- \n babilidad baja, de 15-30 se considera probabilidad media-baja, de 30 a 55 se considera \n probabilidad media, de 55 a 70 se considera probabilidad media-alta, de 70 a 100 se con- \n sidera probabilidad alta. Para esta demostración se ha tomado un periodo de 8 semestres.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

class Estudiante3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Estadisticas Estudiante 3", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="laura Melisa Sanchez Gómez", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Sexo: Femenino", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text="Código: 2571825026", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        button1 = ttk.Button(self, text="Regresar",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[2,4,23,36,20,15,11,9])

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        label = tk.Label(self, text="\n \n \n La probabilidad ha sido calculada como un promedio ponderado de varias variables que \n influyen en la permanencia estudiantil tales como el estado de animo del estudiante, \n su situación económica, promedio académico entre otros. De 0-15 se considera pro- \n babilidad baja, de 15-30 se considera probabilidad media-baja, de 30 a 55 se considera \n probabilidad media, de 55 a 70 se considera probabilidad media-alta, de 70 a 100 se con- \n sidera probabilidad alta. Para esta demostración se ha tomado un periodo de 8 semestres.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        

app = SeaofBTCapp()
app.mainloop()

        