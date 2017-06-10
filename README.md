# Tequila Mockingbird: Birdsong Melody Acquisition and Kinetic Origami
- Program that can 'listen' to any short melody, create its own original song from it using a LSTM neural net and Reinforcement Learning
- Run on Raspberry Pi 3
- Written in Python using Google Cloud Voice
- Utilizing USB Microphone and MIDI input
- Pi servo controls beak of an origami bird!
	- Servo wiring:
		- bottom (brown) wire of servo -> Header 5 
		- middle (red) wire of servo -> Header 1
		- top (orange) wire of servo -> GPIO (Header 8) 
	- Bird model: https://www.youtube.com/watch?v=QZfz_5NCYGg
	- Kinetic Origami example: https://www.youtube.com/watch?v=QZfz_5NCYGg
- tensorflow LSTM Neural Network generates songs from MIDI input
	- To run on raspberry pi, you must use the Pi version of tensorflow! https://github.com/samjabrahams/tensorflow-on-raspberry-pi
- program initializes with command 'Tequila'
- Inspired by the Neuropsychology of birdsong creation
- Bird Whistling Tequila source: The Jon and Zach Show, 2/25/1999 (https://www.youtube.com/watch?v=PyVJzcA1Kds)
- Name inspired by the novel To Kill a Mockingbird

- TO DO:
  - Set up pi server (from sensei)! You're not going to be able to run this super long script on the pi. Pi server will execute servo motion from cpu script. This also means you don't have to have any of the data on the raspberry pi, which I don't think it would even be able to hold that much data in the first place. Try to setup GPU on laptop.
  - Set up MIDI interfacing
  	- Use WAV to midi script! (Use BPM script to get BPM parameter)
    - Write tensorflow music generator script (adapt from Siraj Raval's music generation tutorial on youtube) (https://github.com/llSourcell/AI_Composer)
      - to use the demo script, use 'import _pickle as cPickle' to use pickle
      - to do this, use tensorflow for raspberry pi module on github
  	- How to get a large dataset to train on from just the input file? 
  		- get a ton of wavs of bird songs, convert to MIDI using script
  		- copy the input midi file a ton of times, put into dataset
  		- scramble the midi file somehow and save each midi scramble as a file and put it in the dataset
  - Determine if output will be just playing the wave file from python, or some kind of synthetic bird song (optimal, but wayyyy harder. You'd have to find a library of birds singing certain keys, and map the midi note output to each bird note)

# Future Developments
 - Use Reinforcement learning techniques to teach the LSTM model harmony (https://magenta.tensorflow.org/2016/11/09/tuning-recurrent-networks-with-reinforcement-learning) (https://github.com/tensorflow/magenta/tree/master/magenta/models/rl_tuner)

