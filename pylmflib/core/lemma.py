#! /usr/bin/env python

"""! @package morphology
"""


class Lemma:
    """! "Lemma is a Form subclass representing a form chosen by convention to designate the Lexical Entry. The lemma is usually equivalent to one of the inflected forms, the root, stem or compound phrase." (LMF).
    """
    def __init__(self):
        """! @brief Constructor.
        Lemma instance is owned by LexicalEntry.
        @return A Lemma instance.
        """
        ## feat* elements stocked
        # There is 0,1..N feature for one Lemma
        self.feat = {}
        #FormRepresentation has not been implemented.

    def __del__(self):
        """! @brief Destructor.
        """
        pass


    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "Lemma :\n\t\t\t\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t\t\t - "+key +" : "+val + "\n"
        return txt

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
                print("Feat already present in the Lemma.")
                exit(0)
        self.feat[name] = val

    def get_lexeme(self):
        return self.get_feat('lexeme')

    def get_part_of_speech(self):
        return self.get_feat('partOfSpeech')
