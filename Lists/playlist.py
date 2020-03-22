playlist={
	'title':"not a phase",
	'author':'Canyon Evenson',
	'songs':[
		{'title':'song1', 'artist':['blue'], 'duration':2.5},
		{'title':'song1' ,'artist':['kitty','djcat'], 'duration':5.25},
		{'title':'meowmeow', 'artist':['garfield'], 'duration':2.0}
	]
}

len=0
for song in playlist['songs']:
	len+=song['duration']

print(len)

