import os

"""
single configuration class for all environments
defines all keys that will exist in all environments
(some keys may not be being used in some environments but that is OK)
The values for all keys are loaded from environment variables defined
in each environment. If the env var is not defined the key value will default
to None. A separate bash script that is not checked in to public
source control repo, should be created for each environment
which will set the environmet vars for that specific environment
"""
class Config:
    #ENV can be set to "DEV" or "TEST" or "STAGE" or "PROD"
    ENV = os.environ.get('FLASK_ENVIRONMET')
    DEBUG = bool(os.environ.get('FLASK_DEBUG'))

    #python script for generating secret key from command line
    #python xxxxxx
    #SECRET_KEY = os.environ.get('FLASK_DEBUG')



"""
Alteratively load a configuration file path for each environment
based on a path set by an env var
and load configuration from that file using
app.config.load_frompyfile(ConfigFile.CONFIG_FILE_PATH)
class ConfigFile:
    CONFIG_FILE_PATH = os.environ.get('FLASK_CONFIG_FILE_PATH')
"""
