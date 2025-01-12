import sqlite3

import pandas as pd

conn = sqlite3.connect('data\\results.db')

c = conn.cursor()

query = """select people.first_name, people.state, states.division

from people

JOIN states

on people.state=states.state_abbrev

where first_name like 'J%'"""

c.execute(query)

all = c.fetchall()

df = pd.DataFrame(all)

print(df.to_string())

conn.close()
