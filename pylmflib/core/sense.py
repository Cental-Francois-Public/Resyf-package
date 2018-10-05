#! /usr/bin/env python

"""! @package core
"""


class Sense:
    """! "Sense is a class representing one meaning of a lexical entry. The Sense class allows for hierarchical senses in that a sense may be more specific than another sense of the same lexical entry." (LMF)
    """
    ids = 0
    def __init__(self, id=0):
        """! @brief Constructor.
        Sense instances are owned by LexicalEntry.
        @param id IDentifier. If not provided, default value is 0.
        @return A Sense instance.
        """
        Sense.ids +=1
        # ID is managed at the LexicalEntry level
        if(id == 0):
            id = Sense.ids
        self.id = id

        ## feat* elements stocked
        # There is 0,1..N feature for one Sense
        self.feat = {}
        self.sense_example = []

    def __del__(self):
        """! @brief Destructor.
        Release Definition, Sense, Equivalent, Context, SubjectField, Paradigm instances.
        """
        pass

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        txt = "Sense : id: " + self.get_id() + "\n\t\t\t\tfeat:\n"
        for key, val in self.feat.items():
            txt += "\t\t\t\t - "+key +" : "+val + "\n"
        txt += "\t\t\t\tSenseExamples : \n"
        for example in self.sense_example:
            txt += "\t\t\t\t - " + str(example)
        return txt

    def get_id(self):
        """! @brief IDentifier.
        @return Sense attribute 'id'.
        """
        return self.id

    def add_sense_example(self, sense_example):
        """! @brief Add a new SenseExample to the Sense
        @param sense_example Instance to add
        """
        self.sense_example.append(sense_example)

    def get_sense_example(self):
        return self.sense_example

    def get_synonyms(self):
        """! @brief Get all the synonym corresponding to the Sense
        """
        tab = []
        for example in self.sense_example:
            if(example.get_type() == 'synonyms'):
                tab.append(example)
        tab = sorted(tab, key=lambda example :example.get_rank())
        # for e in tab:
        #     print("\t syno: ", e)
        return tab

    def get_usage(self):
        """! @brief Get the feat of the sense corresponding to "usage"
        """
        return self.get_feat('usage')

    def get_poids(self):
        """! @brief Get the feat of the sense corresponding to "poids"
        """
        return self.get_feat('poids')

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
                print("Feat already present in the Sense.")
                exit(0)
        self.feat[name] = val
