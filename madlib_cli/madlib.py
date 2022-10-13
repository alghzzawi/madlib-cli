import re

def read_template(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
    except FileExistsError as err:
        raise err
    except FileNotFoundError as err:
        raise err
    return content 

def parse_template(story):
    array_of_parts= re.findall(r"(?<=\{).+?(?=\})",story)
    newText=story
    for word in array_of_parts:
        newText = str(newText.replace(word,''))
    return newText,tuple(array_of_parts)

def merge(newText,parts):
    mergeStory = newText.format(*parts)
    return mergeStory

if __name__ == '__main__':
    print('''
*************************************************************************
**  Welcome to madlibs game, Mad Lib is a game that replacement game.  **
**                                                                     **
**  rules this game:                                                   **
**  you will enter some words and then it will replaced in a paragraph,**
**  it may be a funny, just anser the questions and press enter.       **
*************************************************************************''')
    path = "assets/make_me_a_video_game_template.txt"
    story=read_template(path)
    newText,array_of_parts=parse_template(story)
    parts=[]
    for part in array_of_parts:
        parts.append(input('Enter {} ==>  '.format(part)))
    # parts=("dark", "stormy", "night")
    newStory= merge(newText,parts)
    
    with open('assets/response.txt','wt') as new_funny_Story:
        new_funny_Story.write(newStory)
    with open('assets/response.txt') as read_text:
        print(read_text.read())