import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_resize(self):
        # read csv of artist info, list of image file names.
        # The physical dimensions are part of each image file name.
        # Format:
        # artist_name, artist_desc, image_file_name, image_desc, image_file_name, image_desc, ...

        L = ["Pablo Picasso,Great Artist,Dream.jpeg,20,30,Dream\n",
             # "Vincent VanGough,Another Great Artist,StarryNight.jpeg,30,40,Starry Night\n",
             "Leonardo da Vinci,Yet Another Great Artist,MonaLisa.jpeg,40,50,Mona Lisa\n"]

        # writing to file
        file1 = open('myfile.txt', 'w')
        file1.writelines(L)
        file1.close()

        # Using readlines()
        file1 = open('myfile.txt', 'r')
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            print(line.strip())
            print("Line{}: {}".format(count, line.strip()))
            count = count + 1


        # list of strings
        lst = ['Geeks', 'For', 'Geeks', 'is',
               'portal', 'for', 'Geeks']

        # Calling DataFrame constructor on list
        df = pd.DataFrame(lst)
        print(df)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
