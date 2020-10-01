# Word Definer
This project is made by Anish Govind. Other projects can be found at my [GitHub](https://github.com/anishg24).
Huge thank you to the contributors of this [api](https://github.com/meetDeveloper/googleDictionaryAPI) because it handles the dictionary required for this script

![GitHub followers](https://img.shields.io/github/followers/anishg24?label=Follow&style=social)

## Project Description
This is a script designed to generate a text file of definitions of a given input text file of words to define.

## The Why behind this Project
I recently got assigned the task of defining 60+ words in my English class. Instead of googling each one and copy and pasting,
I decided it would be more efficient to use a script. It only took me 45 minutes to make and functional to the point where I liked it.
Now, for any future assignments that require me to do something similar, I can just use this script again!

### Methods Used
* API calls 

### Technologies Involved
* Python 3

## Getting Started
1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Install dependency "requests" (`pip install requests` or see [here](https://requests.readthedocs.io/en/master/user/install/#install))
3. Create an input file that follows the following rules:
   - Words should be on different lines (newline seperated).
   - Having numbers to denote what word you are on should end in a period. (More endings to come later)
   - Odd spacing doesn't matter **unless** its in the word.
   - Capitalization doesn't matter.
   
   Example input file:
   ```
   1. Ambivalent
   3. Hello
   World
   1231251161. nIcE
   ```
3. `python ~/PATH/TO/REPO/main.py input.txt output.txt`
4. Wait for the script to say `DONE`.
5. Open `output.txt` however you feel is best.

Note: Larger input files means you'll have to wait longer for the definitions.

### Features/To-Do:
- [x] Take an input file.
- [x] Produce an output file of definitions.
- [ ] Ignore some definitions based on user input.

## Releases
- 1.0.0 (10/1/2020): First working release.

## Contributors
Creator: [Anish Govind](https://github.com/anishg24)

Ways to contact:
* [E-Mail](anishg24@gmail.com)

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
