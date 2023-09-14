from prettytable import PrettyTable

t = PrettyTable()
t.add_column("Pokemon",["Pikachu","Squirtle","Charmender"])
t.add_column("Type",["Electric","Water","Fire"])
t.align = "l"
print(t)