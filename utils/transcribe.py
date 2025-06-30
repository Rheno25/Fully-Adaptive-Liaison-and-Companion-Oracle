def transcribe(filename, chat_now):
    audio_file= open(filename, "rb")
    transcript = client.audio.transcriptions.create(
        file=(filename, audio_file.read()),
        model="whisper-large-v3"
    )
    chat_now = transcript.text
    print ("Question: " + chat_now)