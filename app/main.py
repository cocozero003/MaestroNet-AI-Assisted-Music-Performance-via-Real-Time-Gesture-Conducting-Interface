import streamlit as st
from app.gesture_handler import process_video_for_bpm
from music.midi_utils import play_midi_file
from core.evaluator import evaluate_beat_coherence
from core.pose_estimation import get_wrist_y_series

st.set_page_config(page_title="MaestroNet", layout="centered")
st.title("MaestroNet – Conductor BPM & Dynamics & Coherence")

st.markdown(
    "Upload a conducting video (MP4 or MOV) and a reference audio (WAV) "
    "to estimate tempo, dynamics, and beat coherence."
)

video_input = st.file_uploader("Upload Conducting Video", type=["mp4", "mov"])
audio_input = st.file_uploader("Upload Reference Audio", type=["wav"])

if video_input and audio_input:
    try:
        with st.spinner("Analyzing conducting gestures..."):
            bpm, dynamic = process_video_for_bpm(video_input)
            wrist_y = get_wrist_y_series(video_input)
            # Save audio to file
            audio_path = os.path.join("music", "reference_audio.wav")
            with open(audio_path, "wb") as af:
                af.write(audio_input.read())
            coherence = evaluate_beat_coherence(audio_path, wrist_y)
        if bpm > 0:
            st.success(f"Detected Tempo: {bpm:.2f} BPM")
            st.info(f"Estimated Dynamics: {dynamic}")
            st.write(f"Beat Coherence Score: {coherence:.3f} (lower is better alignment)")
            if st.button("Play MIDI"):
                play_midi_file(os.path.join("music", "example_score.mid"), bpm=bpm, dynamic=dynamic)
        else:
            st.warning("Unable to detect a consistent beat pattern.")
    except Exception as e:
        st.error(f"Error during analysis: {e}")
