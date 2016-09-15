#!/usr/bin/env python
import os
import speech_recognition
from local_recognizer import LocalRecognizer
from listener import MutableMicrophone, ResponsiveRecognizer

def create_key_recognizer(rate, lang):
    wake_word = "blanky"
    phonemes = "B L AE NG K IY"
    threshold = "1e-1"
    return LocalRecognizer(wake_word, phonemes, threshold, rate, lang)

def _audio_length(audio):
        return float(len(audio.frame_data)) / (
            audio.sample_rate * audio.sample_width)

MIN_AUDIO_SIZE = 0.5
rate = 16000
device_index=None
lang = "en-us"

def dengarkan():
    microphone = MutableMicrophone(sample_rate=rate,
                                    device_index=device_index)

    key_recognizer = create_key_recognizer(rate, lang)
    remote_recognizer = ResponsiveRecognizer(key_recognizer)
    google_sr = speech_recognition.Recognizer()

    with microphone as source:
        remote_recognizer.adjust_for_ambient_noise(source)
        try:
            audio = remote_recognizer.listen(source)
            if _audio_length(audio) > MIN_AUDIO_SIZE:
                text = google_sr.recognize_google(audio, language='ID', show_all=False)
                print 'Blanky: %s' % text
            else:
                print 'Blanky: Tidak ada perintah'
        except Exception as ex:
            print(ex)

while True:
    dengarkan()
