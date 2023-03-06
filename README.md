# pdf-to-mp3
This project can convert a pdf file to mp3 file.

## Information on libraries used
https://pypi.org/project/pyttsx3/   
https://pypi.org/project/pypdf/   
https://mypy.readthedocs.io/en/stable/getting_started.html   
https://flake8.pycqa.org/en/latest/index.html#quickstart   
https://pycqa.github.io/isort/   
https://pypi.org/project/autopep8/   

## Voices Information 
There are multiple voices available some of them are   
afrikaans, aragonese, bulgarian, bengali, bosnian, catalan, czech, welsh, danish, german, greek, default, english, en-scottish, english-north...

```
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
```

## Installation additional applications/program

### FFmpeg is a separate program that is required for pyttsx3 to convert the speech output to MP3 format.

On Ubuntu/Debian-based systems, you can install FFmpeg using the following command:  
```
sudo apt-get install ffmpeg
```
On CentOS/Fedora-based systems, you can install FFmpeg using the following command:  
```
sudo yum install ffmpeg
```

### Espeak text-to-speech engine used by  pyttsx3 library  

For Ubuntu/Debian:
```
sudo apt-get install espeak
```
For CentOS/Fedora:
```
sudo yum install espeak
```

## Run using make
```
make help

convert-pdf                    Converts pdf to mp3
help                           Show available targets
lint                           Lint the code
test                           Run tests
tidy                           Tidy code
```

