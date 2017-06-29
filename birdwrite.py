import wave

def tweety(array_notes):
	allowed = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	for x in array_notes:
		if x not in allowed:
			print(x, 'is not a valid note')

	new_notes = []
	for a in array_notes:
		tostrip = [s for s in a if s.isdigit()]
		new = a.strip(str(tostrip))
		new_notes.append(new)

	infiles = [x + '.wav' for  x in new_notes]
	# infiles = infiles[:5] # limiting it to five notes
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

# tweety(['E8', 'G9', 'A#9', 'F#9', 'D#9', 'A#7', 'C#6'])

