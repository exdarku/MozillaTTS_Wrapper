# MozillaTTS_Wrapper
A very small wrapper for beginners who want to use Mozilla TTS on their project, but cant figure out how to do so.

## Installation

Install requirements first

```bash
pip install TTS==0.3.1 pygame
```

Use GIT to download this file to your local drive.

```bash
git clone https://github.com/exdarku/MozillaTTS_Wrapper
```

## Usage

```python
import aitts

aitts.speak("Hello world! Mozilla TTS here!")
```

You can also use the module to loop through a list. This can be useful if you want the TTS to read long lines continuously. 

```python
import aitts

list = ["Hello! This is a list", "This is just a test for this code", "Goodbye!"]

for i in list:
    aitts.speak(i)

```

Note that Mozilla TTS has a limit on how long your string can be, you may or may not get the result you want. If you want the TTS to read long lines, use a list and loop it.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
If you can, please credit me. It's not necessary, but atleast you'll make me happy. Thank you!
License: [Creative Commons Zero](https://creativecommons.org/publicdomain/zero/1.0/)
