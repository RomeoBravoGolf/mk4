# mk4
mk4
tube scrapper te baja videos de youtube; input: URl del video, Output, elvideoen.mp4
streamscrapper.sh te baja un stream acotado, creo que esta hardcodeado para 30secs, input: URL, output streambajado.ts 
(nose que es .ts pero anda)
main.py es lo que hace la movidita, input: ubicacion del video, output: log.csv

main.sh es un script de bash para ejecutar todo, esta hecho por la mitad, la idea es que primero ejecute streamscrapper por x tiempo despues mande ese
archivo a main.py y ponga a bajar otro, finalmente que sume todos los log.csv y que corra todo eso por y cantidad de tiempo

para la proxima version:
   conectar main.py con streamscrapper.sh
   terminar main.sh
   
   
   
sentiment.py es el sentiment analyzer, toma un string y tira un numero, esta explicado en el output
