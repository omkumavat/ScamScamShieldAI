import whisper
model = whisper.load_model("large")  # or "medium" or "large"
result = model.transcribe("output_clean_audio.wav", task="translate", language="hi")
print("Translated Text:", result["text"])
