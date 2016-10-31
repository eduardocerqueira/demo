"""
Simple script testing argparse
@author: Eduaro Cerqueira <eduardomcerqueira@gmail.com>
"""
import argparse
import logging

# Setting logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def get_parameters_input():
    """
    Get user args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="a name")
    parser.add_argument("word", help="a word")
    return parser.parse_args()

if __name__ == '__main__':
    params = get_parameters_input()
    logging.info("-" * 80)
    logging.info("ARGS: %s", params)
    logging.info("-" * 80)
