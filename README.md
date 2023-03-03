# pdf-to-mp3
This project can convert a pdf file to mp3 file.

## Information on libraries used
https://pypi.org/project/pyttsx3/
https://pypi.org/project/pypdf/


## Installtion additional applications/program

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