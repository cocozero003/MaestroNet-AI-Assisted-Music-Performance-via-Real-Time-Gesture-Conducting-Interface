import time
import mido

def play_midi_file(filepath, bpm=120, dynamic="mf"):
    """
    Play MIDI file at specified BPM and dynamic level.
    Args:
        filepath (str): Path to MIDI file.
        bpm (float): Desired BPM.
        dynamic (str): Dynamic level key (pp, p, mp, mf, f, ff).
    """
    mid = mido.MidiFile(filepath)
    # Extract original tempo or default
    tempo = None
    for msg in mid.tracks[0]:
        if msg.type == "set_tempo":
            tempo = msg.tempo
            break
    if tempo is None:
        tempo = mido.bpm2tempo(120)
    original_bpm = mido.tempo2bpm(tempo)
    ratio = original_bpm / bpm

    # Map dynamics to MIDI velocity
    velocity_map = {"pp": 32, "p": 48, "mp": 64, "mf": 80, "f": 96, "ff": 112}
    velocity = velocity_map.get(dynamic, 80)

    port = mido.open_output()
    for msg in mid.play():
        time.sleep(msg.time * ratio)
        if not msg.is_meta:
            if msg.type == "note_on":
                msg.velocity = velocity
            port.send(msg)
    port.close()
