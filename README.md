# Fetch_Rewards_Text_Similarity
This code is intended as a solution for the following challenge:
This challenge will focus on the similarity between two texts. Your objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

It can be tested on text files using the following syntax:
python3 text_compare.py <text_file_path> <text_file_path> <shingle_factor>

For example:
python3 text_compare.py sample_1.txt sample_2.txt 3

Alternatively, text_compare_example.py can be used to run predefined comparisons using a range of options for shingle_factor:
python3 text_compare_example.py

I tested it using both python 2.7 and python 3.6, so either should work.
