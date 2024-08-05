#Multiple modules

from Priv import Privileges, Admin
from User import User

Darth_Vader = Admin('Darth', 'Vader', '30', ["can delete"])
Darth_Vader.show_privileges()