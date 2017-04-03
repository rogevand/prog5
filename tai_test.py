import io
import pytest

# Import everything from tai.py
from tai import *


def test_Phrase():
    p = Phrase("print", "hello world")
    assert (p.verb == "print")
    assert (p.info == "hello world")
    assert not p.is_end()
    
    p = Phrase("PRint", "hello+world")
    assert (p.verb == "print")
    assert (p.info == "hello+world")
    
    p = Phrase("CHAPTER", "Nowhere")
    assert (p.verb == "chapter")
    assert (p.info == "Nowhere")
    assert not p.is_end()
    assert not p.is_chapter("NOWHERE")
    assert p.is_chapter("Nowhere")
    
    p = Phrase("end", "game")
    assert p.is_end()

    
def test_Line():
    line = Line()
    assert line.length() == 0
    
    line.add(Phrase("chapter", "somewhere"))
    assert line.length() == 1
    assert line.is_chapter("somewhere")
    assert not line.is_chapter("out there")
    
    p = Phrase("println", "yo")
    line.add(p)
    assert line.length() == 2
    assert line.get(1) == p

    
def test_Script():
    s = Script()
    assert s.length() == 0
    with pytest.raises(ValueError):
        s.find_chapter("somewhere")
    
    line = Line()
    line.add(Phrase("goto", "skippy"))
    s.add(line)
    
    line = Line()
    line.add(Phrase("println", "you don't see me"))
    s.add(line)
    
    line = Line()
    line.add(Phrase("chapter", "skippy"))
    s.add(line)
    
    line = Line()
    line.add(Phrase("prompt", "what's up?"))
    s.add(line)
    
    line = Line()
    line.add(Phrase("on", "nothing"))
    line.add(Phrase("print", "too bad..."))
    s.add(line)
    
    line = Line()
    line.add(Phrase("end", "game"))
    s.add(line)
    
    assert s.length() == 6
    assert s.get(s.length() - 1) == line
    assert s.find_chapter("skippy") == 2
    assert s.next_line(0, 0) == (1, 0)
    assert s.next_line(1, 0) == (2, 0)

    index = s.find_chapter("skippy")
    index, _ = s.next_line(index, 0)
    index, _ = s.next_line(index, 0)
    line = s.get(index)
    line.add(Phrase("end", "game"))
    
    assert s.next_phrase(index, 0) == (index, 1)
    assert s.next_phrase(index, 1) == (index, 2)
    assert s.next_phrase(index, 2) == (index + 1, 0)

    
TEST_SCRIPT1 = """\
# this is a comment, followed by a blank line

chapter start
println Hello+world!
goto skippy

     # another comment, with leading whitespace


chapter skippy
>This is a "literal print" line.  With + characters...
if wat print Yahoo!
end game

"""
   
   
def test_load_script():
    src = io.StringIO(TEST_SCRIPT1)
    
    script = load_script(src)
    assert script.length() == 7
    assert script.get(0).is_chapter("start")
    assert script.get(1).get(0).info == "Hello world!"
    assert script.get(4).get(0).verb == "println"
    assert script.get(4).get(0).info == 'This is a "literal print" line.  With + characters...'


def test_Intepreter():
    src = io.StringIO(TEST_SCRIPT1)
    script = load_script(src)
    
    terp = Interpreter(script)
    assert terp.next_phrase().is_chapter("start")
    terp._advance_phrase()
    assert terp.next_phrase().verb == "println"
    assert terp.next_phrase().info == "Hello world!"
    
    terp._skip_to_line(script.length() - 2)
    assert terp.next_phrase().verb == "if"
    terp._advance_phrase()
    assert terp.next_phrase().verb == "print"
    terp._advance_phrase()
    assert terp.next_phrase().is_end()
    
    terp._skip_to_line(script.length() - 2)
    terp._advance_line()
    assert terp.next_phrase().is_end()