from pytube import YouTube

inPath = 'YoutubeDownloader/links.txt'
outPath = 'YoutubeDownloader/DownloadedVideos'

# Links are written in the txt file (1 link per line)
f = open(inPath,'r')
links = f.readlines()

for link in links:
    yt = YouTube(link)

    # log
    print(f'Title: {yt.title}\nViews: {yt.views}\nAuthor: {yt.author}')

    yd = yt.streams.get_lowest_resolution()
    yd.download(outPath)