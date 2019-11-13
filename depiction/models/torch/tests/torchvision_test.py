"""Test TorchVisionModel."""
import unittest
import numpy as np
import torchvision.models as models

from ....core import Task, DataType
from ..torchvision import TorchVisionModel


class TorchVisionModelTestCase(unittest.TestCase):
    """Test TorchVisionModel."""

    def test_prediction(self):
        model = TorchVisionModel(
            model=models.mobilenet_v2(pretrained=True),
            task=Task.CLASSIFICATION,
            data_type=DataType.IMAGE
        )
        image = np.random.randn(1, 3, 224, 224)
        self.assertEqual(model.predict(image).shape, (1, 1000))
