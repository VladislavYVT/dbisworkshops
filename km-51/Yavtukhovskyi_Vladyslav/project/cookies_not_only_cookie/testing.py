from flask import Flask
from flask import render_template_string, render_template
from flask_menu import Menu, register_menu
from datetime import datetime, date
from matplotlib import pyplot as plt
from matplotlib import dates


from db import User

user = User()
hmm = User().stat_weak_by_date('good day sir')
keys = [k for k, v in hmm if k is not None]
values = [v for k, v in hmm if k is not None]
print(keys)
print(values)
datesq = dates.date2num(keys)
plt.plot_date(datesq, values, 'go--')
plt.show()