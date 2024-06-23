"""Testing Commands"""

import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command(capfd):
    command = AddCommand()
    command.execute("2" , "2")
    out, err = capfd.readouterr()
    assert out == "4\n", "The AddCommand should print '4'"

def test_subtract_command(capfd):
    command = SubtractCommand()
    command.execute("2" , "2")
    out, err = capfd.readouterr()
    assert out == "0\n", "The SubtractCommand should print '0'"

def test_multiply_command(capfd):
    command = MultiplyCommand()
    command.execute("2" , "2")
    out, err = capfd.readouterr()
    assert out == "4\n", "The MultiplyCommand should print '4'"

def test_divide_command(capfd):
    command = DivideCommand()
    command.execute("2" , "2")
    out, err = capfd.readouterr()
    assert out == "1\n", "The DivideCommand should print '1'"

def test_app_exit_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"