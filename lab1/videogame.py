class VideoGame:
    name = ''
    quantity_of_heroes = 0
    imbd_rate = 0.0

    def __init__(self, m_name='', m_quantity_of_heroes=0, m_imbd_rate=0):
        self.name = m_name
        self.quantity_of_heroes = m_quantity_of_heroes
        self.imbd_rate = m_imbd_rate

    def __str__(self):
        return self.name + ", " + str(self.quantity_of_heroes) + ", " + str(self.imbd_rate)
