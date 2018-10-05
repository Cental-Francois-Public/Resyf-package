#! /usr/bin/env python

"""! @pmodule wrapper Contains one main function, wrapper_rw(), which runs another function which should be a user function. If the library raises an exception, wrapper_rw() will restore the terminal to a sane state so you can read the resulting traceback.
    This code has been inspired from the pytlmflib 1.0 module. It has been adapted to our needs and to python3
"""

__version__ = '1.0'

# Add pylmflib/pylmflib/ folder to path
import sys
sys.path.append('./pylmflib')

## Functions to read from a file: MDF, XML LMF, sort order, XML config
from input.xml_lmf import xml_lmf_read as lmf_read



from pylmflib.utils.error_handling import Error
from pylmflib.utils.log import log

## Module variable
lexical_resource = None

def wrapper_rw(func, *args, **kwds):
    """! @brief Wrapper function that calls another function, restoring normal behavior on error.
    @param func Callable object.
    @param args Arguments passed to 'func' as its first argument.
    @param kwds Other arguments passed to 'func'.
    """
    import wrapper
    ## As this is a user function, it is executed under 'try' statement to catch and handle exceptions
    try:
        object = func(*args, **kwds)
        if object.__class__.__name__ == "LexicalResource":
            wrapper.lexical_resource = object
            return object
        elif object.__class__.__name__ == "Lexicon":
            from core.lexical_resource import LexicalResource
            if wrapper.lexical_resource is None:
                # Create a Lexical Resource only once
                wrapper.lexical_resource = LexicalResource()
            # Attach lexicon to the lexical resource if not yet done
            if wrapper.lexical_resource.get_lexicon(object.get_id()) is None:
                wrapper.lexical_resource.add_lexicon(object)
            return wrapper.lexical_resource
        elif type(object) == type(dict()) or type(object) == type(tuple()):
            return object
    except Error as exception:
        ## A library error has occured
        exception.handle()
    except SystemExit:
        ## The library decided to stop execution
        raise
    except:
        ## A system error has occured
        import sys
        sys.stderr.write("Unexpected error: " + str(sys.exc_info()[0]) + "\n")
        raise
    else:
        ## Nominal case
        pass
    finally:
        ## Set everything back to normal and release created objects if any
        pass


