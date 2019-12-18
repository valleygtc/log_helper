import unittest
from unittest.mock import Mock

from log_helper import log


class TestLog(unittest.TestCase):
    def test_normal(self):
        logger = Mock()

        @log(logger=logger)
        def add(a, b):
            return a + b
        
        add(1, 2)
        logger.debug.assert_called()

    def test_raise_exception(self):
        logger = Mock()

        @log(logger=logger)
        def add(a, b):
            return a + b
        
        with self.assertRaises(TypeError):
            add(1, '2')
        
        logger.debug.assert_called()
