#permitir ejecucion desde consola
chmod +x /home/main/Desktop/irjuan/MK2/streamscrapper.sh
#elejir calidad
youtube-dl --list-formats https://www.youtube.com/watch\?v\=6aXR-SL5L2o
#descargar
ffmpeg -i $(youtube-dl -f 94 -g https://www.youtube.com/watch?v=-1xif50QMr4) streambajado.ts
