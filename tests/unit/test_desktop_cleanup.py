import unittest
import os
import shutil
from src.desktop_cleanup import move_files

class TestDesktopCleanup(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for testing
        self.source_dir = "test_source"
        self.target_dir = "test_target"
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.target_dir, exist_ok=True)

    def tearDown(self):
        # Clean up after each test
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_move_files(self):
        # Create some test files in the source directory
        test_file1 = os.path.join(self.source_dir, "file1.txt")
        test_file2 = os.path.join(self.source_dir, "file2.txt")
        with open(test_file1, "w") as f1, open(test_file2, "w") as f2:
            f1.write("Test content 1")
            f2.write("Test content 2")

        # Call the move_files function
        move_files(self.source_dir, self.target_dir)

        # Check if files were moved
        self.assertFalse(os.path.exists(test_file1))  # File1 should not exist in source
        self.assertFalse(os.path.exists(test_file2))  # File2 should not exist in source
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "file1.txt")))  # File1 should exist in target
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, "file2.txt")))  # File2 should exist in target

if __name__ == "__main__":
    unittest.main()