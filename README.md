<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="readme-assets/jarvis-lite.png" alt="Logo">
  </a>

  <h1 align="center">Jarvis Lite</h1>
</div>

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/himalayasharma/jarvis-lite?style=social"> <img alt="GitHub forks" src="https://img.shields.io/github/forks/himalayasharma/jarvis-lite?style=social"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/himalayasharma/jarvis-lite"> <img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/himalayasharma/jarvis-lite">

An AI-powered virtual assistant that answer your questions just about anything.

Project Organization
------------

Project Organization
------------

    ├── LICENSE
    ├── Makefile                  <- Makefile with commands like `make environment` or `make requirements`
    ├── README.md                 <- The top-level README for developers using this project
    ├── test_environment.py       <- Script to test virtual environment
    ├── readme-assets             <- Contains images to be used in README.md
    ├── data
    │   └── audio-recording       <- Contains audio recordings of user's questions
    │
    ├── reports                   <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures               <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt          <- The requirements file for reproducing the analysis environment
    │
    └── src                       <- Source code for use in this project
        ├── __init__.py           <- Makes src a Python module
        │
        ├── audio-processing      <- Scripts to get basic audio data and visualizations
        │   ├── audio_processing_basics.py
        │   └── plot_audio.py
        │
        ├── record_mic.py         <- Script to record 4-second audio clips (containing questions)
        ├── speech_to_text.py     <- Script to convert speech to text with AssemblyAI API
        ├── openai_response.py    <- Script to feed transcribed question to OpenAI API to get response                    
        ├── main.py               <- Driver program
        └── api_secrets.py        <- Used to store API keys for OpenAI and AssemblyAI
    
Prerequisites
------------
Before you begin, ensure you have met the following requirements:
* You have a `Linux/Mac/Windows` machine.
* You have installed a `python` distribution. `conda` is preferred.
* You have installed `pip`.
* You have installed `make`.

Setup
------------
1. Clone the repo
	```
	git clone https://github.com/himalayasharma/jarvis-lite.git
	```
2. Traverse into project directory.
3. Create virtual environment.
	```make
	make create_environment
	```
4. Activate virtual environment.
5. Download and install all required packages.
	```make
	make requirements
	```
6. Start application.
	```make
    make app
	```

Contributing
------------
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

License
------------
Distributed under the MIT License. See `LICENSE.txt` for more information.

Ackowledgements
------------
* [Mısra Turp](https://github.com/misraturp)
* [Patrick Loeber](https://github.com/ploeber)
* [AssemblyAI API Docs](https://www.assemblyai.com/docs/)
* [OpenAI API Docs](https://beta.openai.com/examples)
--------
