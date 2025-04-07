import unittest
import os


def read_maze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return None


def is_valid_maze(maze):
    if not maze:
        return False
    row_length = len(maze[0])
    for row in maze:
        if len(row) != row_length:
            return False
    return True


class TestMazeGame(unittest.TestCase):

    def test_read_existing_maze_file(self):
        test_file = 'valid_maze.txt'
        with open(test_file, 'w') as f:
            f.write('####\n#  #\n####')
        result = read_maze_file(test_file)
        self.assertIsNotNone(result)
        os.remove(test_file)

    def test_read_nonexistent_maze_file(self):
        result = read_maze_file('nonexistent_file.txt')
        self.assertEqual(result, None)

    def test_valid_maze(self):
        valid_maze = [
            '####',
            '#  #',
            '####'
        ]
        result = is_valid_maze(valid_maze)
        self.assertEqual(result, True)

    def test_empty_maze(self):
        empty_maze = []
        result = is_valid_maze(empty_maze)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
    
