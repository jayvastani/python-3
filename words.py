"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""
from sys import argv
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words.

    Args:
        url: The URL of a UTF-8 document.

    Returns:
        A list of strings containing the words from the doc
    """
    story=urlopen(url)
    story_words=[]
    for line in story:
        line_words=line.decode('utf-8').split()
        for words in line_words:
            story_words.append(words)
    story.close()
    return story_words

def print_items(items):
    for word in items:
        print(word)

def main(url):
    words=fetch_words(url)
    print_items(words)

if __name__=='__main__':
    main(argv[1])
