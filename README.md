# Ableton_Remote_Control
Basic interface to control Ableton with my phone. Useful when recording drums, synths, etc.

### Dependancies
- Flask (Python) 
- Scamp (Python)
- loopMIDI (https://www.tobias-erichsen.de/software/loopmidi.html)


### How to set it up
0. Git clone this repository
1. Configure virtual MIDI channel 
	- Install loopMIDI
	- Add a new loopback MIDI-port using loopMIDI
2. Configure Ableton
	- Add a new midi channel
	- Set input type to the newly created loopback MIDI-port (loopMIDI)
	- Enable track & remote control for both input and output of the virtual MIDI-port: Ableton->Preferences->Link/MIDI
3. Set up the webserver and midi-map incoming midi signal to Ableton record
	- run 'python Backend.py'
	- Go to Ableton, right-click edit MIDI-map on record button
	- Go to localhost:5000, and press the 'start recording' button. The rec button should now be midi-mapped to Ableton's recording button.


### To dos
- [] Automate the configuration steps
- [] Add toggle for metronome
- [] Integrate phone-camera recording
