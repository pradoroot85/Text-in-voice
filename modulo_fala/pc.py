from gtts import gTTS
import os
 
    

def falar():
    while True: 
        texto = input('Digite a frase: ')    
        frase = gTTS(text=texto, lang='pt')
        frase.save("./audio1.mp3")
        os.system("mpg321 ./audio1.mp3")
                                                    

#falar()
