from pytube import YouTube

# Write the links in the file links.txt (one link per line) and create DownloadedVideos folder
inPath = 'YoutubeDownloader/links.txt'
outPath = 'YoutubeDownloader/DownloadedVideos'

f = open(inPath,'r')
links = f.readlines()

for link in links:
    yt = YouTube(link)

    # log
    print(f'Title: {yt.title}\nViews: {yt.views}\nAuthor: {yt.author}')

    yd = yt.streams.get_lowest_resolution()
    yd.download(outPath)
