#! /usr/bin/env python

"""! @package core
"""
# import elements
from pylmflib.core.global_information import GlobalInformation

class LexicalResource:
    """! "Lexical Resource is a class representing the entire resource and is a container for one or more lexicons. There is only one Lexical Resource instance." (LMF)
    """

    def __init__(self, dtd_version=16):
        """! @brief Constructor.
        @return A LexicalResource instance.
        """
        self.dtdVersion = dtd_version
        ## feat* elements stocked
        # There is 0,1..N feature for one LexicalResource
        self.feat = {}
        ## GlobalInformation instance is owned by LexicalResource
        # There is 1 GlobalInformation for one LexicalResource
        self.global_information = GlobalInformation()
        ## Lexicon instance is owned by LexicalResource
        # There is 1..N Lexicon in a LexicalResource
        self.lexicon = []


    def __del__(self):
        """! @brief Destructor.
        Release GlobalInformation, Lexicon, Speaker instances.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "LexicalResource : \n\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t"+key +" : "+val + "\n"
        txt += str(self.global_information)
        for lexicon in self.lexicon:
            txt += str(lexicon)
        return txt

    def search(self, lexeme, pos=None):
        """! @brief Search the LexicalEntries that correspond to the criterions
        @param lexeme Word to search
        @param pos Part of Speech of the lexeme if None the methode will check with ['NC', 'ADJ', 'VER', 'ADV']
        @return An array of LexicalEntry that correspond to the criterions
        """
        if not lexeme:
            raise ValueError("The lexeme cannot be empty.")
        if len(self.get_lexicons()) > 0 :
            return self.get_lexicons()[0].search(lexeme, pos)

    def get_synonyms(self, lexeme, pos, sense_id=None):
        """! @brief Get the synonyms of a LexicalEntry that correspond to the criterions
        @param lexeme Word to search
        @param pos Part of Speech of the lexeme
        @param sense_id the sense of the synonyms that want to be found. If None, all the synonyms group by sense
        @return The number of lexical entries present in lexicon.
        """
        if not lexeme:
            raise ValueError("The lexeme cannot be empty.")
        if not pos:
            raise ValueError("The part of Speech cannot be empty.")
        return self.get_lexicons()[0].get_synonyms(lexeme, pos, sense_id)

    def get_lexicons(self):
        """! @brief Get all lexicons maintained by the lexical resource.
        @return A Python list of lexicons.
        """
        return self.lexicon

    def add_lexicon(self, lexicon):
        """! @brief Add a lexicon to the lexical resource.
        @param lexicon A Lexicon instance to add to the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.append(lexicon)
        return self

    def remove_lexicon(self, lexicon):
        """! @brief Remove a lexicon from the lexical resource.
        @param lexicon The Lexicon instance to remove from the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.remove(lexicon)
        return self

    def set_dtdVersion(self, dtd_version):
        """! @brief Set DTD version.
        @param dtd_version The DTD version to use.
        @return LexicalResource instance.
        """
        self.dtdVersion = dtd_version
        return self

    def get_dtdVersion(self):
        """! @brief Get DTD version.
        @return LexicalResource attribute 'dtdVersion'.
        """
        return self.dtdVersion

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
                print("Feat already present in the LexicalResource.")
                exit(0)
        self.feat[name] = val

    def find(self, lexeme, pos=None, sense_id=None):
        pass
