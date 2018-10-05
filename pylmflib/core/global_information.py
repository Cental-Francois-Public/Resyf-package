#! /usr/bin/env python

"""! @package core
"""

class GlobalInformation:
    """! "Global Information is a class for administrative information and other general attributes, such as /language coding/ or /script coding/, which are valid for the entire lexical resource." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        GlobalInformation instance is owned by LexicalResource.
        @return A GlobalInformation instance.
        """
        self.feat = {}

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "\tGlobalInformation : \n\t\tfeat:"
        for key, val in self.feat.items():
            txt += "\t\t\t"+key +" : "+val + "\n"
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
                print("Feat already present in the GlobalInformation.")
                exit(0)
        self.feat[name] = val
