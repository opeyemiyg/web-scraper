# web-scraper
![example workflow](https://github.com/opeyemiyg/web-scraper/actions/workflows/python-app.yml/badge.svg) <br>

A web scraping tool for videx landing page.

### Tools and Resources
1. Python 3.7 [link](https://www.python.org/downloads/)
1. Virtualenv

##### Requirements (using pip)
1. beautifulsoup4==4.10.0 [link](https://pypi.org/project/beautifulsoup4/)



Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below

1. Create the virtual environment.
```shell script
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.


1. Activate the environment and install dependencies.
    - #### Linux
    ```shell script
    source /path/to/venv/bin/activate
    pip install -r requirements.txt
    ```

    - #### Windows
    ```cmd
    ./path/to/venv/bin/activate
    pip install -r requirements.txt
    ```
1. Launch the app
    ```shell script
    python main.py
    ```
   
## Testing
Use command below to run unit test
```shell script
python tests.py
```
`
##Description
An hierarchical approach is taken, where the section of the extracted data is identified as the "grandfather" (a div that holds all options), and the individual options of the section is referred to as the "father", while the "children" is the attributes of the options
