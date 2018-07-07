from logging.config import fileConfig
from unittest import TestCase

import os

from pytorch_lambda_poc.lambda_handler import run_inference


class TestSitLoadLargeDataset(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), 'logger.ini'))


    def test_lambda_handler(self):
        #Arrange
        # Nothing

        #Act
        actual = run_inference(None, None)

        #Assert Nothing

