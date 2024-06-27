from scamp import *

s = Session()
midi_channel = s.new_midi_part("Controller", "Remote Control", start_channel=0, num_channels=1)

def trigger_recording(midi_channel):
	midi_channel.play_note(0x90, 1, 1)

trigger_recording(midi_channel)