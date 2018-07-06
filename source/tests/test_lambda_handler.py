from logging.config import fileConfig
from unittest import TestCase

import os

from source.lambda_handler import test_pytorch


class TestSitLoadLargeDataset(TestCase):

    def setUp(self):
        fileConfig(os.path.join(os.path.dirname(__file__), 'logger.ini'))


    def test_lambda_handler(self):
        #Arrange
        # Nothing

        #Act
        actual = test_pytorch(None, None)

        #Assert Nothing

