"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from src.ensae_teaching_cs.td_1a.optimisation_contrainte import exercice_particulier2


class TestOptimisation (ExtTestCase):

    def test_optimisation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        sol2 = exercice_particulier2()
        x2 = sol2['x']
        d = abs(x2[0] - 0.428571428055853) + abs(x2[1] - 0.2857142848749249)
        self.assertLesser(d, 1e-5)


if __name__ == "__main__":
    unittest.main()
