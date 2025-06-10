# MaestroNet

MaestroNet is a real-time AI-assisted music interface that estimates tempo and dynamics from conducting gestures in uploaded videos.

## Features

- Upload MP4 or MOV video to detect tempo (BPM) and dynamics (pp to ff).
- Pose estimation with MediaPipe.
- Tempo estimation via peak detection.
- Gesture-based dynamic level mapping.
- MIDI playback at detected tempo and velocity using Mido and python-rtmidi.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app/main.py
```

Upload a short conducting video when prompted.

## License

This project is licensed under Jukkapan Wirunrat License.
