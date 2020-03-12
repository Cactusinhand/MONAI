# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
from parameterized import parameterized

from monai.transforms import Flip, Flipd
from tests.utils import NumpyImageTestCase2D

INVALID_CASES = [("wrong_axis", ['s', 1], TypeError),
                 ("not_numbers", 's', TypeError)]

VALID_CASES = [("no_axis", None),
               ("one_axis", 1),
               ("many_axis", [0, 1, 2])]


class FlipTest(NumpyImageTestCase2D):

    @parameterized.expand(INVALID_CASES)
    def test_invalid_inputs(self, _, axis, raises):
        with self.assertRaises(raises):
            flip = Flip(axis)
            flip(self.imt)

    @parameterized.expand(INVALID_CASES)
    def test_invalid_cases_dict(self, _, axis, raises):
        with self.assertRaises(raises):
            flip = Flipd(keys='img', axis=axis)
            flip({'img': self.imt}) 

    @parameterized.expand(VALID_CASES)
    def test_correct_results(self, _, axis):
        flip = Flip(axis=axis)
        expected = np.flip(self.imt, axis)
        self.assertTrue(np.allclose(expected, flip(self.imt)))

    @parameterized.expand(VALID_CASES)
    def test_correct_results_dict(self, _, axis):
        flip = Flipd(keys='img', axis=axis)
        expected = np.flip(self.imt, axis)
        res = flip({'img': self.imt})
        assert np.allclose(expected, res['img'])


if __name__ == '__main__':
    unittest.main()