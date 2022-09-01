<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://raw.githubusercontent.com/tataraba/igtie/main/app/static/images/igtie.png" alt="Project logo"></a>
</p>

<h1 align="center">I'LL GET TO IT... EVENTUALLY</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/tataraba/igtie.svg)](https://github.com/tataraba/igtie/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/tataraba/igtie.svg)](https://github.com/tataraba/igtie/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> <strong><em>IGTIE</em></strong> is a project devoted to all those things I want to get to, eventually. It is powered with FastAPI and MongoDB and tracks anything you may want to come back to later. It could be a book, a movie, a TV series, an album, an article, hobby... you name it.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Igtie is short for *I'll get to it eventually*. It's meant to provide a central hub for all those mental notes and bookmarks stored away in the back of your head. Let's face it, you already forgot the name of that show your best friend told you about last week.

Have a new album you want to listen to? Save it here and even give yourself a timeframe to help motivate you. Want to learn a new python library? Add it to your _Coding Playlist_ so you don't forget about it later. Anything's game! 

## 🏁 Getting Started <a name = "getting_started"></a>

If you want to get a copy of this project up and running on your local machine, follow the instructions below.

### Prerequisites

The project requires Python 3.10 and a few dependencies. I use [PDM](https://pdm.fming.dev/latest/) as my package manager, but it is not required. However, it might make installation easier.

Your first step, however, is to clone project and access the local directory in your terminal.
```
cd igtie
```

### Installing (using pipx and PDM)

Although pipx is not required, having an isolated environment for certain tools can make a big difference in your workflow. To install pipx:

On macOS
```
brew install pipx
pipx ensurepath
```
On Windows:
```
python -m pip install --user pipx

# or if you have py installer
py -m pip install --user pipx
```
>>Note: The pipx command now works within any directory in your terminal. It is not directly tied to the igtie project.

Next, install PDM with pipx:

```
pipx install pdm
```

Lastly, install your project dependencies with PDM:
```
pdm install
```
This will create a virtual environment for the project and install the dependencies noted in `pyproject.toml` (which means you do not need to install from the requirements.txt file).

>> Note: You can use other package managers to install dependencies if they are able to read from the pyproject.toml file.


### Installing (using requirements.txt)

If you're unsure about using pipx and PDM as noted above, you can follow these instructions (after navigaing to the project root): 

Create a virtual environment.

```
# macOS
python3 -m venv .venv

# Windows
python -m venv .venv
```

Activate the environment.

```
# macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv/Scripts/activate
```

Install dependencies.
```
# macOS
$ python3 -m pip install -r requirements.txt
# Windows
$ python -m pip install -r requirements.txt
```
>> Note: A package manager (like PDM) will use a lock file to ensure that there are no clashes in dependencies. Installing from the requirements.txt file does not provide that safety. The file may also not be cross-platform, and could cause unexpected results.

## ⚙️ Settings <a name="settings"></a>

The application uses a MongoDB instance for storage. The configuration file looks for specific environment variables to define your database instance (among other things). 

If no environment variables are found, it will look in "localhost" for an instance of MongoDB and spin up the application in "Dev" mode.

You can download the Community Edition of MongoDB and run it locally. Or, you can update the configuration file with URI parameters for an Atlas instance (MongoDB provides a free tier of 512 MB).

>> Note: More info on configuration is forthcoming.

## 🎈 Usage <a name="usage"></a>

Once you have installed all the dependencies, you should be able to run the project locally. First, make sure you have activated your virtual environment.

Then, use the uvicorn library to spin up the application.

```
uvicorn app.main:app --reload
```


## 🔧 Running Tests <a name = "tests"></a>

I'll be using pytest for testing. Instructions to follow.


### Coding Styles

I will be using flake8, mypy, black, and isort


<!-- ## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system. -->

## ⛏️ Built Using <a name = "built_using"></a>

- [FastAPI](https://fastapi.tiangolo.com) - Python Web Framework
- [MongoDB](https://www.mongodb.com/) - Database
- [TailwindCSS](https://tailwindcss.com) - CSS Framework

## ✍️ Author <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Doing Python by night...


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- The FastAPI documentation!
- Ditto on pydantic!
- Rednafi's [article on configuration settings](https://rednafi.github.io/digressions/python/2020/06/03/python-configs.html)
- The Python Community!
