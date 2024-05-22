from faster_whisper import WhisperModel

model = WhisperModel("jerichosiahaya/faster-whisper-medium-id")

segments, info = model.transcribe("audio/3.mp3")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
