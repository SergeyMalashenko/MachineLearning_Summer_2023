import nbformat as nbf

import argparse
import mdutils
import random
import os


def ktx_to_dict(input_file, keystarter='<'):
    """ parsing keyed text to a python dictionary. """
    answer = dict()

    with open(input_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()

    k, val = '', ''
    for line in lines:
        if line.startswith(keystarter):
            k = line.replace(keystarter, '').strip()
            val = ''
        else:
            val += line

        if k:
            answer.update({k: val.strip()})

    return answer


def dict_to_ktx(input_dict, output_file, keystarter='<'):
    """ Store a python dictionary to a keyed text"""
    with open(output_file, 'w+') as f:
        for k, val in input_dict.items():
            f.write(f'{keystarter} {k}\n')
            f.write(f'{val}\n\n')


HEADERS = ktx_to_dict('headers.ktx')

QHA_1 = ktx_to_dict('exercises_1.ktx')
QHA_2 = ktx_to_dict('exercises_2.ktx')
QHA_3 = ktx_to_dict('exercises_3.ktx')

def create_jupyter_notebook_random_questions(destination_filename='ClassWork_[YourName].ipynb'):
    """ Programmatically create jupyter notebook with the questions (and hints and solutions if required)
    saved under source files """

    # Create cells sequence
    nb = nbf.v4.new_notebook()

    nb['cells'] = []
    
    nb['cells'].append(nbf.v4.new_markdown_cell( HEADERS['header'] ))
    
    random_key_s      = random.sample(list(QHA_1), 5)
    for random_question in ( QHA_1[k] for k in random_key_s ):
        nb['cells'].append(nbf.v4.new_markdown_cell( random_question ))
        nb['cells'].append(nbf.v4.new_code_cell(''))

    random_key_s      = random.sample(list(QHA_2), 3)
    for random_question in ( QHA_2[k] for k in random_key_s ):
        nb['cells'].append(nbf.v4.new_markdown_cell( random_question ))
        nb['cells'].append(nbf.v4.new_code_cell(''))

    random_key_s      = random.sample(list(QHA_3), 2)
    for random_question in ( QHA_3[k] for k in random_key_s ):
        nb['cells'].append(nbf.v4.new_markdown_cell( random_question ))
        nb['cells'].append(nbf.v4.new_code_cell(''))
        
    #nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["header"]))
    #nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["sub_header"]))
    #nb['cells'].append(nbf.v4.new_markdown_cell(HEADERS["jupyter_instruction_rand"]))
    # - Add initialisation
    #nb['cells'].append(nbf.v4.new_code_cell('%run initialise.py'))

    # Delete file if one with the same name is found
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # Write sequence to file
    nbf.write(nb, destination_filename)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Enter your name", type=str)
    args = parser.parse_args()
    
    name = args.name

    create_jupyter_notebook_random_questions(f"ClassWork_{name}.ipynb")
