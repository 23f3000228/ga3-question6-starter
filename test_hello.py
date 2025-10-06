from hello import say_hello
import io
import sys

def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
