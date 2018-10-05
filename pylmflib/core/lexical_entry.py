#! /usr/bin/env python

"""! @package core
"""

from collections import OrderedDict

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



class LexicalEntry:
    """! "Lexical Entry is a class representing a lexeme in a given language and is a container for managing the Form and Sense classes.
    A Lexical Entry instance can contain one to many different forms and can have from zero to many different senses." (LMF)
    """
    ids = 0
    def __init__(self, id='0'):
        """! @brief Constructor.
        LexicalEntry instances are owned by Lexicon.
        @param id Unique IDentifier. If not provided, default value is 0.
        @return A LexicalEntry instance.
        """
        #increment the ids at each instantiation
        LexicalEntry.ids += 1
        if(id == '0'):
            id = LexicalEntry.ids
        ## UID is managed at the Lexicon level
        self.id = id
        # attribute from the DTD but not used in our case.
        self.morphologicalPatterns_id = None
        #attribute from the DTD but not used in our case
        self.mwePattern_id = None

        ## feat* elements stocked
        # There is 0,1..N feature for one LexicalEntry
        self.feat = {}
        ## Lemma instance is owned by LexicalEntry
        # There is one Lemma instance by LexicalEntry instance
        self.lemma = None # lemmatized form
        ## Sense instances are owned by LexicalEntry
        # There is zero to many Sense instances per LexicalEntry
        self.sense = []

    def __del__(self):
        """! @brief Destructor.
        Release Sense, Lemma, RelatedForm, WordForm, Stem, ListOfComponents instances.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "LexicalEntry : \n\t\t\tid: " + str(self.id) + "\n\t\t\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t\t - "+key +" : "+val + "\n"
        txt += "\t\t\t"+ str(self.lemma)
        txt += "\t\t\tSenses : \n"
        for sense in self.sense:
            txt += "\t\t\t - " + str(sense) + "\n"
        return txt

    def get_id(self):
        return self.id

    def get_lemma(self):
        return self.lemma

    def get_lexeme(self):
        return self.get_lemma().get_lexeme()
    def get_part_of_speech(self):
        return self.get_lemma().get_part_of_speech()


    def get_feat(self, name):
        """! @brief Get the value form a feat
        @param name The name from the feat to get
        @return The value of the feat asked or "None" if no feat exist with this name
        """
        if(name in self.feat):
            return self.feat[name]

        return None

    def set_feat(self, name, val, warning=False):
        """! @brief Get the value form a feat
        @param name The name from the feat to set
        @param val The value to set
        """
        if(warning):
            if (name in self.feat):
                print("Feat already present in the LexicalEntry.")
        self.feat[name] = val

    def get_sense(self, id=None):
        """! @brief Get the all the senses of the lexicalEntry
        @param id restrict the sense to the only one with the same id
        @return An array of sense that has been recovered
        """
        if(id is None):
            return self.sense
        for sense in self.sense:
            if sense.get_id() == id:
                return [sense]
        return []

    def add_sense(self, sense):
        """! @brief Add a new sense to the LexicalEntry
        @param sense The sense instance to add
        """
        self.sense.append(sense)

    def add_synonym(self, senseExample):
        """! @brief Add a new SenseExample/synonym to the LexicalEntry
        @param senseExample The instance to add to the LexicalEntry.
        @return True or False if the instance has been added to the sense corresponding to the id.
        """
        sense = self.get_sense(senseExample.get_id())
        if(sense is None):
            return False
        self.sense.add_sense_example(senseExample)
        return True

    def get_synonym(self, id=None):
        """! @brief Get the all the synonyms of the lexicalEntry
        @param id restrict the sense to the only one with the same id
        @return A dictionary grouping the synonyms by usage
        """
        dic = {}
        senses = self.get_sense(id)
        for tmp in senses:
            if (tmp.get_id() not in dic):
                dic[tmp.get_id()] = {}
            for syno in tmp.get_synonyms():
                if("usage" not in dic[tmp.get_id()]):
                    dic[tmp.get_id()]["usage"] = tmp.get_usage()
                if ("synonyms" not in dic[tmp.get_id()]):
                    dic[tmp.get_id()]["synonyms"] = []
                dic[tmp.get_id()]["synonyms"].append(syno)

        return OrderedDict(sorted(dic.items(), key=lambda t: natural_keys(t[0])))
