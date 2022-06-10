import os

for filename in os.listdir('./whitea/cogs'):
    if filename.endswith('.py'):
        print(f'cogs.{filename[:-3]}')
