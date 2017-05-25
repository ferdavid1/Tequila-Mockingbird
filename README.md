# Tequila Mockingbird
- Program that can 'listen' to any short melody and identify notes, create a short song from it
- Run on Raspberry Pi 3
- Written in Python using Google Cloud Voice
- Utilizing USB Microphone and MIDI input
- Pi servo controls beak of 3D printed bird
- tensorflow neural network generates songs from MIDI input
- program initializes with command 'Tequila'
- Inspired by the Neuropsychology of birdsong creation
- Name inspired by the novel To Kill a Mockingbird

# Current Progress:
- Setting up voicecommand C++ module to accurately respond to keyword 'tequila': changing threshold for best audio capture
	- Set it up to use the proper google cloud voice credentials, now that you have access to that.
	- If this still does not work, let's set up Google Cloud Voice constant listening module to respond instead 
- TO DO:
  -Set up MIDI interfacing
  	- Use WAV to midi script! (Use BPM script to get BPM parameter)
  -Write tensorflow music generator script (adapt from Siraj Raval's music generation tutorial on youtube) (https://github.com/samjabrahams/tensorflow-on-raspberry-pi)
  	- to do this, use tensorflow for raspberry pi module on github
  - Determine if output will be just playing the wave file from python, or some kind of synthetic bird song (optimal, but wayyyy harder. You'd have to find a library of birds singing certain keys, and map the midi note output to each bird note)

