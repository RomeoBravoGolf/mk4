from pytube import YouTube

video = input('ingrese url del video ')
#stream de tn
#yt = YouTube('https://www.youtube.com/watch?v=-1xif50QMr4')
yt = YouTube(video)

print(yt.title, ' fue descragado ATR')
stream = yt.streams.first()
stream.download()

