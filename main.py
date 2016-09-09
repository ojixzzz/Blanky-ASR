#!/usr/bin/env python
import os
from local_recognizer import LocalRecognizer
from listener import MutableMicrophone, ResponsiveRecognizer

def create_mycroft_recognizer(rate, lang):
    wake_word = "blanky"
    phonemes = "B L AE NG K IY"
    threshold = "1e-5"
    return LocalRecognizer(wake_word, phonemes, threshold, rate, lang)

rate = 16000
device_index=None
lang = "en-us"
microphone = MutableMicrophone(sample_rate=rate,
                                    device_index=device_index)

mycroft_recognizer = create_mycroft_recognizer(rate, lang)
remote_recognizer = ResponsiveRecognizer(mycroft_recognizer)

with microphone as source:
    remote_recognizer.adjust_for_ambient_noise(source)
    while True:
        try:
            audio = remote_recognizer.listen(source)
            print('BLANKY: ROGER THAT')
        except IOError, ex:
        	print(ex)
