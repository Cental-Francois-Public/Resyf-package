#!/usr/bin/pyhton2
"""! @pmodule ReSyf Contains the main functions: load(), search(), get_synonyms(), show_resources(), that use the pylmflib module & manage the allowed behavior of the module.
    This code has been inspired from the pytlmflib 1.0 module. It has been adapted to our needs and to python3.
"""

import sys
import xml.etree.ElementTree as ET
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import os

#to order dictionary
from collections import OrderedDict

from pathlib import Path

#serialization
import pickle

#Path to the local libraries
dir_path_src = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.join(dir_path_src, "..")
sys.path.append(dir_path)


import pylmflib.input.xml_lmf

# sort function to have a natural sort
#https://stackoverflow.com/a/5967539
import re

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]




def __serialise__(path=None, lexicalRes=None):
    """
    """
    if lexicalRes is None:
        return False
    config = ConfigParser.ConfigParser()

    if path is None:
        raise ValueError("The path to the configuration file cannot be None.")

    config_path = os.path.join(path, "config.cfg")
    config_file = Path(config_path)
    try:
        my_abs_file = config_file.resolve()
    except FileNotFoundError:
        raise ValueError("The configuration file provided doesn't exist");
        return False

    # dir_path_config = os.path.join(path, "config.cfg")
    config.read(config_path)
    #append the local path from the config file to the current
    serialized_path = config.get('File_paths', 'resyf_path_xml_file_serialized')

    with open(serialized_path, 'wb') as f:
        pickle.dump(lexicalRes, f)

    return True



def load(path=None):
    """! @brief Load the resource.
    @param path The path to the xml file to load. By default it will load the file specified in the config.
    @return An instance created from the xml loaded.
    """

    #recover the xml path from the config file
    config = ConfigParser.ConfigParser()
    has_been_serialized = False

    if path is None:
        raise ValueError("The path to the configuration file cannot be None.")
    else:
        config_path = os.path.join(path, "config.cfg")
        config_file = Path(config_path)
        try:
            my_abs_file = config_file.resolve()
        except FileNotFoundError:
            raise ValueError("The configuration file provided doesn't exist");
            return None

        # dir_path_config = os.path.join(path, "config.cfg")
        config.read(config_path)
        #append the local path from the config file to the current
        xml_path = config.get('File_paths', 'resyf_path_xml_file')
        serialized_path = config.get('File_paths', 'resyf_path_xml_file_serialized')
        try:
            serialized_file = Path(serialized_path)
            my_abs_file = serialized_file.resolve()
            has_been_serialized = True
            # print("load serialized")
            with open(serialized_path, 'rb') as f:
                lexicalRes = pickle.load(f)
        except FileNotFoundError:
            # print("The serialized file does not exist")
            has_been_serialized = False


    if(has_been_serialized == False):
        print("load xml")
        lexicalRes = pylmflib.input.xml_lmf.xml_lmf_read(xml_path)



    return lexicalRes

def search(lexicalRes, term, pos=None):
    """! @brief Search LexicalEntry in the resource.
    @param lexicalRes The LexicalResource instance in wich we want to search.
    @param term The term that we want to find.
    @param pos The part of speech of the term. If None, the methode will try with ['NC', 'VER', 'ADJ', 'ADV']
    @return An array with the LexicalEntry instances corresponding.
    """
    for lexicon in lexicalRes.get_lexicons():
        result = lexicalRes.search(term, pos)
    return result

def get_synonyms(lexicalRes, term, pos, sense_id=None):
    """! @brief Search SenseExample/synonyms in the resource.
    @param lexicalRes The LexicalResource instance in wich we want to search.
    @param term The term that we want to find the synonyms.
    @param pos The part of speech of the term.
    @param sense_id The id of the sense of the synonyms that will be returned. If None, all the synonyms group by sense will be returned
    @return A dictionary containing the usage and all the SenseExample/synonyms group by the sense_id.
        ex: {sense_id_1: {'usage', "....", [SenseExample1, SenseExample2, ...]}, ... }
    """
    d = lexicalRes.get_synonyms(term, pos, sense_id)
    return OrderedDict(sorted(d.items(), key=lambda t: natural_keys(t[0])))

def show_resources(lexicalRes):
    """! @brief String representation of the instance.
    @param lexicalRes The LexicalResource instance that want to be visualised.
    @return The string representation of the lexicalRes.
    """
    return str(lexicalRes)

def get_all_lexicalEntry(lexicalRes, path=None):
    """ !@brief Recover all the lexical entries presents in the resource & export the result to the output file ReSyf/outputs/lexical_entries.txt.
    It can be modified via the config file..
    @param lexicalRes The lexical resource
    @return A set of word of each lexical entry
    """

    lexicalEntries = {}
    string = ""
    for lexicon in lexicalRes.get_lexicons():
        for key, lexicalEntry in lexicon.get_lexical_entries().items():
            lexeme = lexicalEntry.get_lexeme()
            if lexeme not in lexicalEntries:
                lexicalEntries[lexeme] = True
                string += lexeme + "\n"

    wordsList = string.split("\n")
    #wordsList.sort()

    string = ""
    for word in wordsList:
        string += word + "\n"

    if path is None:
        return wordsList
    else:
        config_path = os.path.join(path, "config.cfg")
        config_file = Path(config_path)
        try:
            my_abs_file = config_file.resolve()
        except FileNotFoundError:
            raise ValueError("The configuration file provided doesn't exist");
            return None

    config = ConfigParser.ConfigParser()

    # dir_path_config = os.path.join(path, "config.cfg")
    config.read(config_path)
    output_path = config.get('File_paths', 'resyf_path_output_lexical_entry')

    write_file(output_path, string, 'w+')
    return wordsList

def get_all_words(lexicalRes, path=None):
    """ !@brief Recover all the lexical entries & synonyms presents in the resource & export the result to the output file ReSyf/outputs/words.txt.
    It can be modified via the config file..
    @param lexicalRes The lexical resource
    @return A set of word for each lexical entry & synonymss
    """
    words = {}
    string = ""
    cpt = 0;
    for lexicon in lexicalRes.get_lexicons():
        for key, lexicalEntry in lexicon.get_lexical_entries().items():
            lexeme = lexicalEntry.get_lexeme()
            if lexeme not in words:
                words[lexeme] = True
                string += lexeme + "\n"
            for key2, synonyms in lexicalEntry.get_synonym().items():
                for syno in synonyms["synonyms"]:
                    word = syno.get_word()
                    if word not in words:
                        words[word] = True
                        string += word + "\n"


    wordsList = string.split("\n")
    wordsList.sort()

    string = ""
    for word in wordsList:
        string += word + "\n"

    if path is None:
        return wordsList
    else:
        config_path = os.path.join(path, "config.cfg")
        config_file = Path(config_path)
        try:
            my_abs_file = config_file.resolve()
        except FileNotFoundError:
            raise ValueError("The configuration file provided doesn't exist");
            return None

    config = ConfigParser.ConfigParser()

    # dir_path_config = os.path.join(path, "config.cfg")
    config.read(config_path)
    output_path = config.get('File_paths', 'resyf_path_output_words')

    write_file(output_path, string, 'w+')
    return wordsList

def write_file(path, string, mode='r+'):
    """!@brief Utility methode to write a string in a file.
    @param path The path to the file
    @param string The string to write
    @param mode The mode in wich the file will be open. By default it's 'r+'
    """
    print("writing file...")
    config_file = Path(path)
    try:
        my_abs_file = config_file.resolve()
    except FileNotFoundError:
        print("The output file doesn't except.")
    with open(path, mode, encoding="utf-8") as f:
        f.write(string);
