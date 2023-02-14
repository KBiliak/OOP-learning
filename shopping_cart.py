
class ShoppingCart:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def adding_items(self, item, item_cost):
        self.items.append(item)
        self.total_cost += item_cost

    def removing_items(self, item, item_cost):
        self.items.remove(item)
        self.total_cost -= item_cost

    def describe_sc(self):
        print(f"Total cost is {self.total_cost}")
        all_items = ""
        for i in self.items:
            if len(all_items) != 0:
                all_items += ", "
            all_items += i

        print(f"All items: {all_items}")

sc = ShoppingCart()
sc.adding_items("item1", 20)
sc.adding_items("item2", 30)
sc.adding_items("item3", 40)
sc.describe_sc()

sc.removing_items("item1", 20)
sc.describe_sc()


