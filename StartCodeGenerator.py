import os.path

FILE_NAME = 'tweets.py'


def create_fun_block(name):
    '''
    '''

    return "def {0}():\n    '''{1} -> {2}\n    '''\n    pass\n\n".format(name, '', '')


def create_functions(names):
    '''
    '''
    content = ''
    for name in names:
        content += create_fun_block(name)
        
    return content

def file_writer(file_name, content):
    '''
    '''
    
    f = open(file_name, 'w')
    f.write(content)
    f.close()
        

def generate(file_name, function_names):
    '''
    '''
    
    content = create_functions(function_names)
    file_writer(file_name, content)

if __name__ == '__main__':
    generate(FILE_NAME, ['extract_mentions', 'extract_hashtags'])