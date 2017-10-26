"""End-to-end test for a nodejs_binary

Simply find the binary and run it, asserting that it produces correct output.
"""

from subprocess import check_output
from sys import platform
import unittest

from build_bazel_rules_nodejs.internal.runfiles import resolve_runfile

class BinTest(unittest.TestCase):

  def testRuns(self):
    if platform == "win32" or platform == "win64":
      program = 'program_example/bin.exe'
    else:
      program = 'program_example/bin'
    actual = check_output([resolve_runfile(program)])
    self.assertEqual(actual, '2\n')

if __name__ == '__main__':
  unittest.main()
