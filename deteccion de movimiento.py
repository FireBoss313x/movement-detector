import cv2
import datetime as dt
import tkinter as tk

ventana = tk.Tk()

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

ventana.title('Programa para detección de movimiento')
ventana.geometry('720x420')

etiqueta1 = tk.Label(ventana, text='---DETECCION DE MOVIMIENTO DE UN VIDEO---', bg='sky blue',fg='black')
etiqueta1.pack(fill=tk.X)

etiqueta2 = tk.Label(ventana, text='Ingrese el nombre del video que desea analizar', fg='black')
etiqueta2.pack(padx=1,pady=20)
etiqueta2.pack(ipadx=5,ipady=5)

texto = tk.Entry(ventana)
texto.pack(ipadx=10,ipady=5)

boton1 = tk.Button(ventana, text='Examinar', padx = 10, pady = 5,command = obtencion, bg = 'cyan')
boton1.pack(pady=10)

ventana.mainloop()
