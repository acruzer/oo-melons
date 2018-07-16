"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total_price(self):
        if self.species.title() == "Christmas Melon":
            base_price = 7.5
        else:     
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    # get_total = super().get_base_price()
    # def get_total(self):
    #     """Calculate price, including tax."""
    #     if self.species.title() == "Christmas Melon":
    #         base_price = 7.5
    #     else:     
    #         base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

        # return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # def __init__(self, species, qty, country_code):


        # self.species = species
        # self.qty = qty
        # self.shipped = False
    country_code = "NA"
    order_type = "international"
    tax = 0.17


    def get_total_price(self):
        """Calculate price, including tax."""

        # if self.species.title() == "Christmas Melon":
        #     base_price = 7.5
        # else:     
        #     base_price = 5
        # total = (1 + self.tax) * self.qty * base_price
        subtotal = super().get_total_price()
        if self.qty < 10:
            total = subtotal + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
