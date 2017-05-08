# Tequila Mockingbird
- Program that can 'listen' to any short melody and identify notes, create a short song from it
- Run on Raspberry Pi 3
- Written in Python using Google Cloud Voice
- PiAUISuite for voicecommand
- Utilizing USB Microphone and MIDI input, voicecommand C++ module
- Pi servo controls beak of 3D printed bird
- tensorflow neural network generates songs from MIDI input
- program initializes with command 'Tequila'
- Inspired by the Neuropsychology of birdsong creation
- Name inspired by the novel To Kill a Mockingbird

# Current Progress:
- Setting up voicecommand C++ module to accurately respond to keyword 'tequila': changing threshold for best audio capture
- TO DO:
  -Set up MIDI interfacing
  -Write tensorflow music generator script (adapt from Siraj Raval's music generation tutorial on youtube)
