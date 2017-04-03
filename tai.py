#! python3
'''CpS 110 Program 5: Text Adventures

Completed by YOURNAME_HERE (YOUR_LOGIN)
'''

class Phrase:
    """A pair of strings: .verb and .info
    
    .verb is the action to perform (always lowercase).
    .info is extra information the action may need.
    """
    def __init__(self, verb: str, info: str):
        raise NotImplementedError()
    
    def is_chapter(self, label: str) -> bool:
        """Is this Phrase of the form "chapter <label>"?"""
        raise NotImplementedError()
    
    def is_end(self) -> bool:
        """Is this Phrase's verb "end"?"""
        raise NotImplementedError()


class Line:
    """A list of one or more Phrase objects.
    """
    def __init__(self):
        raise NotImplementedError()
    
    def add(self, p: Phrase):
        """Add a Phrase to the end of our list."""
        raise NotImplementedError()
    
    def length(self) -> int:
        """Return the number of Phrases in our list."""
        raise NotImplementedError()
    
    def get(self, i: int) -> Phrase:
        """Return the <i>'th Phrase from our list.
        
        Precondition: <i> is a valid, 0-based index
        """
        raise NotImplementedError()
    
    def is_chapter(self, label: str) -> bool:
        """Does this Line begin with a Phrase of the form "chapter <label>"?"""
        raise NotImplementedError()


class Script:
    """A list of Line objects comprising a TAIL script.
    """
    def __init__(self):
        raise NotImplementedError()
    
    def add(self, line: Line):
        """Add <line> to the end of our list IF <line> is not empty."""
        raise NotImplementedError()
    
    def length(self) -> int:
        """Return the number of Lines in this script."""
        raise NotImplementedError()
    
    def get(self, i: int) -> Line:
        """Return the <i>'th Line of the script.
        
        Precondition: <i> is a valid, 0-based index
        """
        raise NotImplementedError()
    
    def find_chapter(self, label: str) -> int:
        """Return the index of the Line containing the Phrase "chapter <label>".
        
        If no such Line can be found, raises a ValueError exception.
        """
        raise NotImplementedError()
    
    def next_phrase(self, iline: int, iphrase: int) -> (int, int):
        """Return the line/phrase indices of the next phrase after <iline>/<iphrase>.
        
        Precondition:
            * <iline> is a valid, 0-based index into our list of Lines
            * <iphrase> is a valid, 0-based index into that Line's list of Phrases
        """
        raise NotImplementedError()
    
    def next_line(self, iline: int, iphrase: int) -> (int, int):
        """Return the line/phrase indices of the next line after <iline>/<iphrase>.

        Precondition:
            * <iline> is a valid, 0-based index into our list of Lines
            * <iphrase> is a valid, 0-based index into that Line's list of Phrases
        """
        raise NotImplementedError()


def load_script(stream) -> Script:
    """Return the Script created by parsing the contents of the file <stream>."""
    raise NotImplementedError()


class Interpreter:
    """The logic and context required to interpret a TAIL script.
    
    Keeps a copy of the script being interpreted, along
    with all "state" required to keep track of where we
    are in the script, etc.
    
    Interpreters keep track of the current location in
    the TAIL script with a "bookmark": a pair of integers,
    one telling us the current LINE of the script,
    the other telling us the current PHRASE within that LINE.
    
    Each .step() call will
        * get the Phrase indicated by the "bookmark"
        * interpret that Phrase
        * and, depending on the Phrase, advance the "bookmark" to
            - the next phrase in that line, or
            - the next line, or
            - another line altogether (i.e., a "chapter" line)
    """
    def __init__(self, s: Script):
        raise NotImplementedError()
    
    def _advance_phrase(self):
        """Move the "bookmark" forward to the next phrase.
        
        If there IS no next phrase (i.e., we were at the last
        phrase in the line), advance to the beginning of the
        next line instead.
        """
        raise NotImplementedError()
    
    def _advance_line(self):
        """Move the "bookmark" forward to the beginning of the next line."""
        raise NotImplementedError()
    
    def _skip_to_line(self, iline: int):
        """Move the "bookmark" to the beginning of line <iline>."""
        raise NotImplementedError()
    
    def next_phrase(self) -> Phrase:
        """Get whatever Phrase the "bookmark" is pointing at."""
        raise NotImplementedError()
    
    def step(self):
        """Get the current Phrase, "interpret" it, and advance the "bookmark" appropriately."""
        # TODO: add logic to
        #   - get current phrase
        #   - "execute" that phrase (i.e., carry out the described action)
        #   - advance the bookmark to indicate the next phrase to interpret
    
    def run(self):
        """Repeatedly step until an "end" Phrase is encountered."""
        while not self.next_phrase().is_end():
            self.step()


if __name__ == "__main__":
    # TODO: add logic to
    #  - get filename from command line argument 1 (or print an error/usage message if that argument is missing)
    #  - load script from that file
    #  - create interpreter to run the loaded script
    #  - run the interpreter to completion
    pass