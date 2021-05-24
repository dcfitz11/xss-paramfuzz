# XSS-INSP3CT0R
A **Kali Linux** program to detect XSS vulnerabilities in web pages.

Replace the value in the URL for the parameter you wish to
fuzz with the keyword, "FUZZ".

# INSTALLATION
## Clone repository:
`git clone https://github.com/dcfitz11/xss-paramfuzz.git`

## Install requirements:
`pip3 install -r requirements.txt`

# GECKODRIVER INSTRUCTIONS
## xss.detector.py depends on FireFox and geckodriver to perform testing:
### Install:
`sudo apt-get FireFox`
### Download:
> Download geckodriver from the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases) for Linux
### Extract
> Extract the geckodriver tar file
### Copy to /usr/local/bin
`sudo mv geckodriver /usr/local/bin/`

# RUNNING THE PROGRAM
## To run the program:
`python3 xss-paramfuzz.py`