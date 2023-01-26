1. Copy this folder and cd into the folder
2. Install poetry:
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
3. Open data/input/input_file.csv in excel and enter your configuration details, starting line #2. Please do not delete line #1.
each line per site.
4. Setup authentication mechanism to invoke these API and based on that change file name under 'confgure_sites.py' or 
    use default mechanism by just entering your "access token" in data/auth/input_token_only.json file. More details
    on how to get these tokens and how to use them https://youtu.be/W5DslAZETAk?t=228
5. Run "poetry install"
6. Run script "poetry run python3 configure_sites.py"
6. Logs can be seen at data/log.log
7. Log level can be changed for debugging 
    log level can be set under "configure_sites.py" script  change INFO on "logger.setLevel(logging.INFO)" to "DEBUG"
8. In order to get configuration using group and mac. USe following 
    "poetry run python site_get_configuration.py"


 