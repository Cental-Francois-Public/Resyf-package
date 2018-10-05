#! /usr/bin/env python

"""! @package ReSyf Package to read the resource ReSyf or other xml file respecting the LMF format.

    Usage:
    >>> import ReSyf

"""

# Add ReSyf/ folder to path
import sys
sys.path.append(sys.path[-1] + '/ReSyf')

import ReSyf.src.ReSyf as ReSyf

def __serialise__(path=None, lexicalRes=None):
    return ReSyf.__serialise__(path, lexicalRes)

def load(path=None):
    """! @brief Load the resource.
    @param path The path to the xml file to load. By default it will load the file specified in the config.
    @return An instance created from the xml loaded.
    """
    return ReSyf.load(path)

def show_resources(lexicalRes):
    """! @brief String representation of the instance.
    @param lexicalRes The LexicalResource instance that want to be visualised.
    @return The string representation of the lexicalRes.
    """
    if not lexicalRes:
        raise ValueError("The LexicalResource can't be None.")
    return ReSyf.show_resources(lexicalRes)

def search(lexicalRes, term, pos=None):
    """! @brief Search LexicalEntry in the resource.
    @param lexicalRes The LexicalResource instance in wich we want to search.
    @param term The term that we want to find.
    @param pos The part of speech of the term. If None, the methode will try with ['NC', 'VER', 'ADJ', 'ADV']
    @return An array with the LexicalEntry instances corresponding.
    """

    if not lexicalRes:
        raise ValueError("The LexicalResource can't be None.")
    if not term or term.strip() == "":
        raise ValueError("The term to search can't be None or empty.")

    if pos:
        pos = pos.upper()
    return ReSyf.search(lexicalRes, term, pos)

def get_synonyms(lexicalRes, term, pos, sense_id=None):
    """! @brief Search SenseExample/synonyms in the resource.
    @param lexicalRes The LexicalResource instance in wich we want to search.
    @param term The term that we want to find the synonyms.
    @param pos The part of speech of the term.
    @param sense_id The id of the sense of the synonyms that will be returned. If None, all the synonyms group by sense will be returned
    @return A dictionary containing the usage and all the SenseExample/synonyms group by the sense_id.
        ex: {sense_id_1: {'usage' :  "...."; 'synonyms' : [SenseExample1, SenseExample2, ...]}, ... }
    """
    if not lexicalRes :
        raise ValueError("The LexicalResource can't be None.")
    if not term or term.strip() == "":
        raise ValueError("The term to search can't be None or empty.")
    if not pos or pos.strip() == "":
        raise ValueError("The part of speech of the term to search can't be None or empty.")
    if pos:
        pos = pos.upper()
        return ReSyf.get_synonyms(lexicalRes, term, pos, sense_id)

def get_more_simple_synonyms(lexicalRes, term, pos, sense_id=None):
    """! @brief Search SenseExample/synonyms in the resource based on the function get_synonyms.
    @param lexicalRes The LexicalResource instance in wich we want to search.
    @param term The term that we want to find the synonyms.
    @param pos The part of speech of the term.
    @param sense_id The id of the sense of the synonyms that will be returned. If None, all the synonyms group by sense will be returned
    @return A dictionary containing the usage and the the SenseExample/synonyms with the more little rank for the sense_id.
        ex: {sense_id_1: {'usage' :  "...."; 'synonyms' : [SenseExample1]}, ... }
    """
    listSimple = []
    syno = get_synonyms(lexicalRes, term, pos, sense_id)
    for key, val in syno.items():
        del val['synonyms'][1:]
    return syno

def get_all_lexicalEntry(lexicalRes, path=None):
    """ !@brief Recover all the lexical entries presents in the resource & export the result to the output file ReSyf/outputs/lexical_entries.txt.
    It can be modified via the config file..
    @param lexicalRes The lexical resource
    @return A set of word of each lexical entry
    """
    if not lexicalRes :
        raise ValueError("The LexicalResource can't be None.")
    return ReSyf.get_all_lexicalEntry(lexicalRes, path)

def get_all_words(lexicalRes, path=None):
    """ !@brief Recover all the lexical entries & synonyms presents in the resource & export the result to the output file ReSyf/outputs/words.txt.
    It can be modified via the config file..
    @param lexicalRes The lexical resource
    @return A set of word for each lexical entry & synonymss
    """
    if not lexicalRes :
        raise ValueError("The LexicalResource can't be None.")
    return ReSyf.get_all_words(lexicalRes, path)
