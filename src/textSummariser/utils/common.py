import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from textSummariser.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    This function reads yaml file and returns configuration object
    
    Parameters:
    -----------
    path_to_yaml: string
        path like input

    Returns:
    ---------
    ConfigBox: ConfigBox type
        resulting configuration object from yaml file
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

def create_directories(path_to_directories: list, verbose = True) -> None:
    """
    This function creates a list of directories

    Parameters:
    -----------
    path_to_directories: list of strings
        List of the paths of the directories to be created
    verbose: boolean
        if True log this event in log file

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)

        if verbose:
            logger.info(f"created directory at: {path}")
    


def get_size(path:Path) -> int:
    """
    This functions returns the size of a file in kb

    Parameters:
    -----------
    path: string
        path to the input file
    
    Returns: 
    ---------
    size_in_kb: int
        size in kb of the path
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return size_in_kb