#! /usr/bin/env python

"""! @package core
"""

from pylmflib.utils.error_handling import Warning
from pylmflib.utils.io import ENCODING

class Lexicon:
    """! "Lexicon is a class containing all the lexical entries of a given language within the entire resource." (LMF)
    """
    def __init__(self, id=None):
        """! @brief Constructor.
        Lexicon instances are owned by LexicalResource.
        @return A Lexicon instance.
        """
        ## feat* elements stocked
        # There is 0,1..N feature for one Lexicon
        self.feat = {}
        ## All LexicalEntry instances are maintained by Lexicon
        # There is 1..N LexicalEntry instances per Lexicon
        # dict ((word, pos) => LexicalEntry)
        self.lexical_entry = {}


    def __del__(self):
        """! @brief Destructor.
        Release LexicalEntry instances.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "\tLexicon : \n\t\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t"+key +" : "+val + "\n"
        for key, val in self.lexical_entry.items():
            txt += "\t\t"+ str(key) +" : \n\t\t" + str(val) + "\n"
        return txt

    def get_lexical_entries(self):
        """! @brief Get all lexical entries maintained by the lexicon.
        @return A Python set of lexical entries.
        """
        return self.lexical_entry

    def get_lexical_entry(self, key):
        """! @brief Get all lexical entries maintained by the lexicon.
        @param key The lemma to find in the lexicalEntries
        @return The lexicalEntry instance or None if not present in the lexicon.
        """
        if(key in self.lexical_entry):
            return self.lexical_entry[key]
        return None

    def add_lexical_entry(self, lexical_entry, key):
        """! @brief Add a lexical entry to the lexicon.
        @param lexical_entry A LexicalEntry instance to add to the Lexicon.
        @param key The lemma of the LexicalEntry to add
        @return Lexicon instance.
        """
        self.lexical_entry[key] = lexical_entry
        return self

    def remove_lexical_entry(self, key):
        """! @brief Remove a lexical entry from the lexicon.
        @param key The lemma of the LexicalEntry instance to remove from the Lexicon.
        @return Lexicon instance.
        """
        del self.lexical_entry[key]
        return self

    def count_lexical_entries(self):
        """! @brief Count number of lexical entries of the lexicon.
        @return The number of lexical entries present in lexicon.
        """
        # return len(self.get_lexical_entries())
        raise NotImplementedError("TODO!")

    def search(self, lexeme, pos=None):
        """! @brief Search the LexicalEntries that correspond to the criterions
        @param lexeme Word to search
        @param pos Part of Speech of the lexeme if None the methode will check with ['NC', 'ADJ', 'VER', 'ADV']
        @return An array of LexicalEntry that correspond to the criterions
        """
        #search via lexeme only
        result = []
        partOfSpeech = [pos]
        if pos is None:
            partOfSpeech = ['NC', 'ADJ', 'VER', 'ADV']
        for p in partOfSpeech:
            res = self.get_lexical_entry((lexeme, p))
            if res :
                result.append(res)

        # return tab of LexicalEntry
        return result

    def get_synonyms(self, lexeme, pos, sense_id=None):
        """! @brief Get the synonyms of a LexicalEntry that correspond to the criterions
        @param lexeme Word to search
        @param pos Part of Speech of the lexeme
        @param sense_id the sense of the synonyms that want to be found. If None, all the synonyms group by sense
        @return The number of lexical entries present in lexicon.
        """
        lexicalEntry = self.get_lexical_entry((lexeme, pos))
        if lexicalEntry is None:
            return {}
        synonyms = lexicalEntry.get_synonym(sense_id)
        return synonyms

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
                print("Feat already present in the Lexicon.")
                exit(0)
        self.feat[name] = val
