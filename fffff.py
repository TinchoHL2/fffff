meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "una respuesta muy comun a algo gracioso",
            "LMAO": "una respuesta rara a algo gracioso", 
            }
            
            
word = input("Usando mayusculas escribe una palabra que no entiendas")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("esa palabra todavia no fue procesada, lo sentimos.")
