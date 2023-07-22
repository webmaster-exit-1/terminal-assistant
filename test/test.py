"""
Module is the main entry point for running the terminal assistant tests.
"""

import unittest

if __name__ == "__main__":
    test_suite = unittest.TestLoader().discover(".", pattern="test_terminal_assistant.py")
    unittest.TextTestRunner().run(test_suite)
