# Python Module ReSyf


## Description

This module read an **XML-LMF** file and create a python object. On this object you can execute some action that will be described.
The module does not support all the xml-lmf file, but a sample of the file can be found [here](https://github.com/d4rk694/ReSyf/blob/master/ReSyf/resources/ReSyf.sample.xml) \
**This module use python 3**

## Fonctionnality
The module export some function:

 - **load(path=None)**: load the resource file from the config file from the folder situed at "path". If None, a ValueError will be raised. If there is a serialized version of the resource, this one will be loaded (to gain time at the loading).
 - **show_resources(lexicalRes)**: Return a string representation of **all** the resource loaded.
 - **search(lexicalRes, term, pos=None)**: search a term in the lexical entry of the resource. If the parameter "pos" isn't specified, the module will test with the elements [NC, VER, ADJ, ADV].
 - **get_synonyms(lexicalRes, term, pos, sense_id=None)**: Get all the synonyms of a term. If no sense_id is given, The synonyms are grouped by the usage of a sense.
 - **get_more_simple_synonyms(lexicalRes, term, pos, sense_id=None)**: Get the more simple synonyms based on his rank. If no sense_id is given, the synonyms are grouped by the usage of a sense.
 - **get_all_lexicalEntry(lexicalRes, path=None)**: Return a set of all the LexicalEntry present in the LexicalResource & export them into a file if the path isn't None. cfr "config.cfg"
 - **get_all_words(lexicalRes, path=None)**: Return a set of all words (LexicalEntry & Synonyms) presents in the LexicalResource & export them into a file if the path isn't None. cfr "config.cfg"
 - **def \_\_serialise\_\_(path=None, lexicalRes=None)** : Serialize the lexical resource to load it more quickly next time. Like the load method, the path is the path to the folder containing the config file.


## Configuration
You can modify the location of the resource ReSyf from the config file : "config.cfg"
<pre>
	[File_paths]
	resyf_path_xml_file : /Full/path/to/ReSyf.xml
  resyf_path_xml_file_serialized : /Full/path/to/ReSyf.serialized
	resyf_path_output_lexical_entry: /full/path/to/the/output/lexical_entries.txt
	resyf_path_output_words : /full/path/to/the/output/words.txt
</pre>
- **resyf_path_xml_file** : The path to the ReSyf file. It must be an xml file respecting the LMF format.
- **resyf_path_xml_file_serialized** : The path to the ReSyf serialized file.
- **resyf_path_output_lexical_entry**: Path to the file where to export the lexical entries from the lexical resources.
- **resyf_path_output_words** : Path to the file where to export all the word from the lexical resource.

## installation

To use ReSyf on your computer, you must first download the latest "tar.gz" file located in the "build" folder.
Once it is done, extract it and launch a terminal from the new folder created.
In the terminal type the following commands:
<pre>
$ python3 setup.py install --record files.txt --user
</pre>
The option "--record" will record all the files installed in the file "files.txt". If you desire to unistall ReSyf, simply type the following command from the installation folder:
<pre>
$ cat files.txt | sudo xargs rm -rf
</pre>

**WARNING** Be sure that the **outputs** folder has the right to be written by the module.

## Usage Sample

### Load the resource
Before the usage of any function of the module, you need to load the resource.
~~~python
import ReSyf

# Load the resource
lexicalRes = ReSyf.load(path_to_the_config_file)

# Get representation of the resource as a string
str = ReSyf.show_resources(lexicalRes)

# Print the representation of the resource
print(str)
~~~
**WARNING** If no path is provided of the file does not exist, a ValueError is raised.
Once loaded, you can use the function below.

### Print the resource Loaded
~~~python
import ReSyf

# Load the resource
lexicalRes = ReSyf.load(path_to_the_config_file)

# Get representation of the resource as a string
str = ReSyf.show_resources(lexicalRes)

# Print the representation of the resource
print(str)
~~~

### Search a lexical entry
~~~python
import ReSyf

# Load the resource
lexicalRes = ReSyf.load(path_to_the_config_file)

# Ask the user the word he want to search
term = input("word : ")

# Ask the user the Part of speech of the word
pos = input("pos : ")

if not pos:
    pos = None # If None, all the Part of Speech of the word will be returned


result = ReSyf.search(lexicalRes, term, pos)
~~~

### Get synonyms

~~~python
import ReSyf

# Load the resource
lexicalRes = ReSyf.load(path_to_the_config_file)

# Ask the user the word he want to search
term = input("word : ")

# Ask the user the Part of speech of the word
pos = input("pos : ")

# Ask the user the sense id of the word he want to get
sense_id = input("sense_id : ")
if not sense_id:
    sense_id = None # If None, all the senses of the word will be returned
result = ReSyf.get_synonyms(lexicalRes, term, pos, sense_id)
~~~

### Get More simple synonyms

~~~python
import ReSyf

# Load the resource
lexicalRes = ReSyf.load(path_to_the_config_file)

# Ask the user the word he want to search
term = input("word : ")

# Ask the user the Part of speech of the word
pos = input("pos : ")

# Ask the user the sense id of the word he want to get
sense_id = input("sense_id : ")
if not sense_id:
    sense_id = None# If None, all the senses of the word will
syno = ReSyf.get_more_simple_synonyms(lexicalRes, term, pos, sense_id)
~~~

## Authors
@Dorian Ricci - Student at Université Catholique de Louvain-la-Neuve (UCL)
