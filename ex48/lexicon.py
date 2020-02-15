from ex48.convert import convert_number

def scan(words):
    dic = {'direction':('north','south','east', 'west', 'down', 'up', 'left', 'right', 'back'),
        'verb':('go','stop','kill','eat'),
        'stop':('the','in','of','from','at','it'),
        'noun':('door','bear','princess','cabinet')}

    word = words.split()
    result = []
    for item in word:
        if convert_number(item):
            result.append(('number', int(item)))

        else:
            for key,value in dic.items():
                if item in value:
                    result.append((key,item))
                    break
            else:
                result.append(('error', item))
    return result
