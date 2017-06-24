import wave

def tweety(array_notes):
	allowed = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	for x in array_notes:
		if x not in allowed:
			print(x, 'is not a valid note')


	infiles = [x + '.wav' for  x in array_notes]
	outfile = "birdsong.wav"

	data= []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	for x in range(len(data)):
		output.writeframes(data[x][1])
	output.close()

# the beginning of iron man
# tweety(['E', 'G', 'G', 'A', 'A', 'C', 'B','C','B','C','G','G','A','A'])


