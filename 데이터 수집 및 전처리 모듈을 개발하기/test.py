python
import unittest
from feature_extraction import extract_features  # 예시 함수

class TestFeatureExtraction(unittest.TestCase):
    def test_extract_features(self):
        test_data = 'test_video.mp4'
        result = extract_features(test_data)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
