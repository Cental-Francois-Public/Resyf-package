#! /usr/bin/env python

"""! @package morphology
"""

class SenseExample:
    """! "Sense Example TODO!\n is a Form subclass representing a word form or a morph that can be related to the Lexical Entry. There is no asumption that the Related Form is associated with the Sense class in the Lexical Entry." (LMF)
    """
    def __init__(self, id=None):
        """! @brief Constructor.
        RelatedForm instances are owned by LexicalEntry.
        @param lexeme Related lexeme. If not provided, default value is None.
        @return A RelatedForm instance.
        """
        # Id of the sense
        self.id = id
        ## feat* elements stocked
        # There is 0,1..N feature for one RelatedForm
        self.feat = {}

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "SenseExample : \tid: " + self.get_id() + "\n\t\t\t\t\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t\t\t\t - "+key +" : "+val + "\n"
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
                print("Feat already present in the SenseExample.")
                exit(0)
        self.feat[name] = val

    def get_id(self):
        """! @brief Get the id of the Sense linked to this SenseExample
        """
        return self.id

    def get_type(self):
        """! @brief Get the feat of the SenseExample corresponding to "type"
        """
        return self.get_feat('type')

    def get_annotation(self):
        """! @brief Get the feat of the SenseExample corresponding to "annotation"
        """
        return self.get_feat('annotation')

    def get_score_lemma(self):
        """! @brief Get the feat of the SenseExample corresponding to "score_lemma"
        """
        return self.get_feat('score_lemma')

    def get_score_sense(self):
        """! @brief Get the feat of the SenseExample corresponding to "score_sense"
        """
        return self.get_feat('score_sense')

    def get_word(self):
        """! @brief Get the feat of the SenseExample corresponding to "word"
        """
        return self.get_feat('word')

    def get_rank(self):
        """! @brief Get the feat of the SenseExample corresponding to "word"
        """
        return self.get_feat('rank')




















def test(self):
    return None
