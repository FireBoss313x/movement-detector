from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from PIL import ImageTk, Image
from tkinter import PhotoImage
import cv2
import datetime as dt

def obtencion():
    eltexto = str(texto.get())
    body = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    capture = cv2.VideoCapture(eltexto,0)
    tiempoA = dt.datetime.now()

    while capture.isOpened():
        ret, frame = capture.read()
        tiempoB = dt.datetime.now()
        tiempo_transcurrido = tiempoB - tiempoA
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        bodys = body.detectMultiScale(gray,1.1,4)
    
        for (x, y, w ,h) in bodys:
            cv2.rectangle(frame, (x, y),(x+w, y+h), (97, 255, 51),2)
            cv2.imwrite(dt.datetime.now().strftime("IMG-%Y-%m-%d-%H-%M-%S")+ ".jpg", frame)

        cv2.imshow('Video Examinado',frame)
    
        k = cv2.waitKey(30)
        if k == 27:
           break
        
    capture.release()

c_negro = '#2d3436'
c_azul = '#000051'
c_verde = '#3fff7c'
c_gris = '#636e72'
c_neon_verde = '#3ffbe0'
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

texto = CTkEntry(frame, text_font = ('sans serif',12), placeholder_text = 'Nombre del video',
                border_color = c_verde, fg_color = c_negro, width=220, height=40)
texto.grid(columnspan =2,row=1, padx=4, pady=4)

bt_iniciar = CTkButton(frame, text_font=('sans serif',12), border_color = c_neon_verde, fg_color=c_gris,
                       hover_color = c_verde, corner_radius=12, border_width=2, text= 'Analizar video',height=40, command = obtencion)

bt_iniciar.grid(columnspan=2,row=4, pady=4, padx=4)

root.call('wm', 'iconphoto', root._w, logo)
root.mainloop()











