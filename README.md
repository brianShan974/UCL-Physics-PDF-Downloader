# UCL-Physics-PDF-Downloader
A simple python script to download all pdfs in UCL physics courses on moodle. 

This script can be used to download all resources including lecture notes, past papers and all files in pdf format. This script was originally written for and tested with the moodle platform for UCL physics students, but now it also supports other subjects such as computer science.

In order to run this script, `beautifulsoup4`, `lxml` and `requests` have to be installed. They can be installed with by running
```
pip install beautifulsoup4 lxml requests
```
After that, just put all files in the same folder as `main.py`, run
```
python main.py
```
and follow the prompts. The files will then start downloading.

On macOS, you may need to substitute `pip` and `python` in the commands with `pip3` and `python3`.
