"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """"""

    def __init__(self, species, qty, order_type, tax, country_code):  #parameters
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type  #not needed here even though they share commonality.
        self.tax = tax         #values are different
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    # order_type = "domestic"
    # tax = 0.08


    def __init__(self, species, qty): #number of arguments we enter when the class is being instantiated
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08, "USA") #These parameters need to match super class parameters)
        # because they are the ones being passed into the AbstractMelonOrder(parent)
    



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # order_type = "international"
    # tax = 0.17

    # creating an instance of InternationalMelonOrder Class
    def __init__(self, species, qty, country_code): # When we instanciate InternationalMelonOrder these are the parameters we need provide arguments for.
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17, country_code)  #arguments
        # Because we are calling the parent class in this dunder init, the arguments neeed to match the parent class parameters.

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10:
            total += 3

        return total

    # need to add a dunder init like above or undo the dunder init above in order for the bottom to work. 
    # both ways work

    #Don't need this now because we pass country_code in the __init__
    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
