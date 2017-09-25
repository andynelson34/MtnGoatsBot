import twython, time, sys, random, os, calendar

# Twitter keys stored as config vars in Heroku
client = twython.Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'], os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])

albums = {
	1: "TheSunsetTree.txt",
	2: "Tallahassee.txt",
	3: "AllHailWestTexas.txt",
	4: "BeatTheChamp.txt",
	5: "Goths.txt",
	6: "TranscendentalYouth.txt",
	7: "AllEternalsDeck.txt"
}
numAlbums = len(albums)

# Randomly select an album to tweet from
lyricsFile = albums[random.randint(1, numAlbums)]

# Read the lyrics file
filename = open(lyricsFile,'r')
f = filename.readlines()
filename.close()

startLine = random.randint(0, len(f) - 1)
# Don't use blank lines
while f[startLine] == "\n":
	startLine += 1

tweet = f[startLine]
# Add the next line if there is one, it's not blank, and the resulting tweet isn't over 140 characters
if (startLine < len(f) - 1) and (f[startLine + 1] != "\n") and (len(tweet + f[startLine + 1]) <= 140):
	tweet += f[startLine + 1]

# Print lyric(s) to log and post tweet
print(tweet)
client.update_status(status=tweet)
