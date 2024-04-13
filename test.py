import unittest
import numpy as np
import naloga2

class TestNaloga2(unittest.TestCase):
    def setUp(self):
        # Create a sample image for testing
        self.test_image = np.zeros((100, 100), dtype=np.uint8)
    
    def test_konvolucija(self):
        # Test konvolucija function
        kernel = np.ones((3, 3), dtype=np.float32)
        result = naloga2.konvolucija(self.test_image, kernel)
        self.assertEqual(result.shape, (100, 100))  # Check output shape
        
        # Add more specific tests for konvolucija function if needed
        
    def test_filtriraj_z_gaussovim_jedrom(self):
        # Test filtriraj_z_gaussovim_jedrom function
        sigma = 1.5
        result = naloga2.filtriraj_z_gaussovim_jedrom(self.test_image, sigma)
        self.assertEqual(result.shape, (100, 100))  # Check output shape
        
        # Add more specific tests for filtriraj_z_gaussovim_jedrom function if needed
        
    def test_filtriraj_sobel_smer(self):
        # Test filtriraj_sobel_smer function
        result = naloga2.filtriraj_sobel_smer(self.test_image)
        self.assertEqual(result.shape, (100, 100))  # Check output shape
        
        # Add more specific tests for filtriraj_sobel_smer function if needed

if __name__ == '__main__':
    unittest.main()