import sims4.commands

@sims4.commands.Command('hello_jaewon', command_type=sims4.commands.CommandType.Live)
def hello(command: str="Default", _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Hello, Jaewon! _connection is ' + command)
