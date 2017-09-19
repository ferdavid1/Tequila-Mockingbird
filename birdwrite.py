import wave

def tweety(array_notes):
	allowed = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	for x in array_notes:
		if array_notes.count(x) > 1:
			for y in range(array_notes.count(x) - 1):
				array_notes.remove(x)

	new_notes = []
	for a in array_notes:
		tostrip = [s for s in a if s.isdigit()]
		new = a.strip(str(tostrip))
		new_notes.append(new)

	infiles = ['song_notes/' + x + '.wav' for  x in new_notes]
	infiles = infiles[:4] # limiting it to five notes
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

# tweety(['A8', 'A8', 'A8', 'A8', 'A8', 'A8', 'A8', 'A8', 'F#9', 'A#9', 'D#9', 'B8', 'C8'])

