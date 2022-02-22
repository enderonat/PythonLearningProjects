class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        print(f'This is {self.name} restaurant.\nThey mainly make {self.type} as a dish.')

    def open_restaurant(self):
        print(f'{self.name} is open.')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['strawberry', 'watermelon', 'chocolate', 'vanilla', 'mint', 'cock']

    def display_flavours(self):
        print(f'These are the flavours we have {self.flavours}')


this_restaurant = Restaurant('komagene', 'çiğköfte')
that_restaurant = IceCreamStand('avcılar dondurmacısı', 'dondurma')
