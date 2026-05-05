# bookbot

A Python CLI tool that reads any text file and reports word count and letter frequency — sorted from most to least common. Built to analyze classic novels from [Project Gutenberg](https://www.gutenberg.org/).

## Example Output

```
Filename: books/frankenstein.txt
Found 78122 total words
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
...
```

## Tech Stack

- Python 3.x
- No external dependencies

## Getting Started

```bash
git clone https://github.com/B0OGI3/bookbot.git
cd bookbot
python3 main.py path/to/your/book.txt
```

Any `.txt` file works. To try it with a classic novel, grab one from [Project Gutenberg](https://www.gutenberg.org/) and pass the path as the argument.

## Project Structure

```
bookbot/
├── main.py    # Entry point — reads the file and prints the report
└── stats.py   # Word count and character frequency logic
```
