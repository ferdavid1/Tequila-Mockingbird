# Tequila Mockingbird
- Program that can 'listen' to any short melody and identify notes, create a short song from it
- Run on Raspberry Pi 3
- Written in Python using Google Cloud Voice
- Utilizing USB Microphone and MIDI input
- Pi servo controls beak of 3D printed bird
	- Servo wiring:
		- bottom (purply grey) wire of servo -> GPIO (Header 8)
		- middle (red) wire of servo -> Header 5
		- top (orange) wire of servo -> Header 1 
- tensorflow neural network generates songs from MIDI input
	- To run on raspberry pi, you must use the Pi version of tensorflow! https://github.com/samjabrahams/tensorflow-on-raspberry-pi
- program initializes with command 'Tequila'
- Inspired by the Neuropsychology of birdsong creation
- Bird Whistling Tequila source: The Jon and Zach Show, 2/25/1999 (https://www.youtube.com/watch?v=PyVJzcA1Kds)
- Name inspired by the novel To Kill a Mockingbird

- TO DO:
  -Set up MIDI interfacing
  	- Use WAV to midi script! (Use BPM script to get BPM parameter)
  -Write tensorflow music generator script (adapt from Siraj Raval's music generation tutorial on youtube) (https://github.com/samjabrahams/tensorflow-on-raspberry-pi)
  	- to do this, use tensorflow for raspberry pi module on github
  - Determine if output will be just playing the wave file from python, or some kind of synthetic bird song (optimal, but wayyyy harder. You'd have to find a library of birds singing certain keys, and map the midi note output to each bird note)

