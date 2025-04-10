class SpacePlanner:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.items = []
        self.occupied_space = 0

    def calculate_volume(self):
        """Calculate total volume of the space"""
        return self.width * self.length * self.height

    def add_item(self, item_name, item_width, item_length, item_height):
        """Add an item to the space if there's enough room"""
        item_volume = item_width * item_length * item_height
        if (self.occupied_space + item_volume) <= self.calculate_volume():
            self.items.append({
                'name': item_name,
                'width': item_width,
                'length': item_length,
                'height': item_height
            })
            self.occupied_space += item_volume
            return True
        return False

    def remove_item(self, item_name):
        """Remove an item from the space"""
        for item in self.items:
            if item['name'] == item_name:
                self.occupied_space -= (item['width'] * item['length'] * item['height'])
                self.items.remove(item)
                return True
        return False

    def get_remaining_space(self):
        """Calculate remaining available space"""
        return self.calculate_volume() - self.occupied_space

    def get_item_count(self):
        """Return total number of items in the space"""
        return len(self.items)

    def list_items(self):
        """Return list of all items in the space"""
        return [item['name'] for item in self.items]

    def calculate_usage_percentage(self):
        """Calculate percentage of space used"""
        total_volume = self.calculate_volume()
        if total_volume == 0:
            return 0
        return (self.occupied_space / total_volume) * 100

    def can_fit(self, width, length, height):
        """Check if an item of given dimensions can fit"""
        item_volume = width * length * height
        return (self.occupied_space + item_volume) <= self.calculate_volume()

    def get_dimensions(self):
        """Return dimensions of the space"""
        return {'width': self.width, 'length': self.length, 'height': self.height}

    def clear_space(self):
        """Remove all items from the space"""
        self.items = []
        self.occupied_space = 0

