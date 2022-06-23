from vosk import Model, KaldiRecognizer
from pathlib import Path
import wave
import json

class Listener():

    def __wav_listen__(file_path):
        model = Model(r"vosk-model-ru-0.10") # russian model 
        file = wave.open(file_path)
        rec = KaldiRecognizer(model, 8000)
        result = ''
        last_n = False

        while True:
            data = file.readframes(8000)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())

                if res['text'] != '':
                    result += f" {res['text']}"
                    last_n = False
                elif not last_n:
                    result += '\n'
                    last_n = True
        
        res = json.loads(rec.FinalResult())
        result += f" {res['text']}"
        return result



    def write_file(file_path):
        #try to open audio file
        if (Path(file_path).is_file() == False) or (Path(file_path).suffix != '.wav'):
            return f'[-] Unable to listen the file! {Path(file_path).suffix}'
        
        match(Path(file_path).suffix):
            case '.wav':
                return Listener.__wav_listen__(file_path)



