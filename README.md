# Tequila Mockingbird: Birdsong Melody Acquisition and Kinetic Origami
- Program that can 'listen' to any short melody, recreate it from scratch using Reinforcement Learning
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
- program initializes with command 'Tequila'
- Inspired by the Neuropsychology of birdsong creation
- Bird Whistling Tequila source: The Jon and Zach Show, 2/25/1999 (https://www.youtube.com/watch?v=PyVJzcA1Kds)
- Name inspired by the novel To Kill a Mockingbird

- TO DO:
  - Set up MIDI interfacing
  	- Use WAV to midi script! (Use BPM script to get BPM parameter)
  	- How to get a large dataset to train on from just the input file? 
      - Use the lakh midi dataset for melody generation
  		- copy the input midi file a ton of times, put into dataset
      - after the neural net is trained, determine how similar the output file is to the input original, as opposed to random other ones from the lakh dataset. 
  - Determine if output will be just playing the wave file from python, or some kind of synthetic bird song (optimal, but wayyyy harder).
     You'd have to find a library of birds singing certain keys, and map the midi note output to each bird note)
     Create it! using https://academy.allaboutbirds.org/birdsong/
     For:
      white-throated sparrows song, transposed across all keys

# Future Developments
 - Use Reinforcement learning techniques to teach the LSTM model harmony (https://magenta.tensorflow.org/2016/11/09/tuning-recurrent-networks-with-reinforcement-learning) (https://github.com/tensorflow/magenta/tree/master/magenta/models/rl_tuner)
 - Compare to https://github.com/shiba24/birdsong-generation-project

