def remove_char(string):
    string = list(string)
    string.remove('Brahma')
    return ' '.join(string)

remove_char('Brahma is a good boy ')