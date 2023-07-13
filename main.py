from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from PIL import ImageTk, Image
from tkinter import PhotoImage

c_negro = '#100010'
c_azul = '#000051'
c_verde = '#157f0d'

root = CTk()
root.geometry('500x600+600+20')
root.minsize(480,500) 
root.config(bg = c_negro)
root.title('Detección de movimiento dentro de un video')

logo = PhotoImage(file = 'sensor.png')

frame = CTkFrame(root, fg_color = c_negro)
frame.grid(column = 0, row = 0, sticky = 'nsew', padx = 50, pady = 50)

frame.columnconfigure([0,1], weight =1)
frame.rowconfigure([0,1,2,3,4,5], weight =1)

root.columnconfigure(0, weight =1)
root.rowconfigure(0, weight =1)

CTkLabel(frame, image = logo).grid(columnspan = 2, row = 0)

video = CTkEntry(frame, text_font = ('sans serif',12), placeholder_text = 'Nombre del video',
                border_color = c_verde, fg_color = c_negro, width=220, height=40)
video.grid(columnspan =2,row=1, padx=4, pady=4)

bt_iniciar = CTkButton(frame, text_font=('sans serif',12), border_color = c_verde, fg_color=c_negro,
                       hover_color = c_verde, corner_radius=12, border_width=2, text= 'Analizar video',height=40)

bt_iniciar.grid(columnspan=2,row=4, pady=4, padx=4)

root.call('wm', 'iconphoto', root._w, logo)
root.mainloop()
