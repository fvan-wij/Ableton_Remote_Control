# Ableton_remote_control
Basic web-interface to control Ableton and my phone simultaneously. Useful when recording drums, synths, etc.

### Dependencies
- Flask (Python) 
- Scamp (Python)
- loopMIDI (https://www.tobias-erichsen.de/software/loopmidi.html)

### How to set it up
0. Git clone this repository
1. Configure virtual MIDI channel 
	- Install loopMIDI
	- Add a new loopback MIDI-port with the name 'Remote Control' in loopMIDI
2. Configure Ableton
	- Add a new midi channel in Ableton
	- Set input type to 'Remote Control'
	- Go to Ableton->Preferences->Link/MIDI and enable track & remote control for both input and output of 'Remote Control'
3. Set up the webserver and midi-map incoming midi signal to Ableton record
	- run 'python ./app.py'
	- Go to Ableton, right-click edit MIDI-map on record button
	- Go to localhost:8000, and press the 'start recording' button. The rec button should now be midi-mapped to Ableton's recording button.


### To dos
- [ ] Automate the configuration steps
- [ ] Add toggle for metronome
- [x] Integrate phone-camera recording
