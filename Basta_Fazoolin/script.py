class Menu:
  # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + "h to " + str(self.end_time) + "h."
  # Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items:
  def calculate_bill(self, purchased_items):
    total = 0
    for i in purchased_items:
      total += self.items.get(i, 0)
    return total

items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", items, 11, 16)
print(brunch)

items2 = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early-bird", items2, 15, 18)

items3 = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", items3, 17, 23)

items4 = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", items4, 11, 21)

print("The price of a breakfast order for one order of pancakes, one order of home fries, and one coffee is: " + str( brunch.calculate_bill(['pancakes', 'home fries', 'coffee']) ))

print("The price of a salumeria plate and the vegan mushroom ravioli is: " + str( early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']) ))


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "the address of the restaurant is: " + self.address
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
print(flagship_store)
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(new_installment)

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas_menu = Menu("arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
new_business = Business("Take a' Arepa", [arepas_place])

print(new_business.name)
print(new_business.franchises[0])
