import sims4.commands

@sims4.commands.Command('hello_jaewon', command_type=sims4.commands.CommandType.Live)
def hello(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Hello, Jaewon!')
