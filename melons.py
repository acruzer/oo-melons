"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty, country_code=None):

        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    country_code = "USA"

    def get_total_price(self):
        if self.species.title() == "Christmas Melon":
            base_price = 7.5
        else:     
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    country_code = "NA"
    order_type = "international"
    tax = 0.17


    def get_total_price(self):
        """Calculate price, including tax."""

        subtotal = super().get_total_price()
        if self.qty < 10:
            total = subtotal + 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an inspection has been passed."""
        if passed == True:
            self.passed_inspection = True