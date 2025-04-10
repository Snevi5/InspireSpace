class FurnitureCatalog:
    def __init__(self, catalog_name="Main Catalog"):
        self.catalog_name = catalog_name
        self.items = {}
        self.categories = set()

    def add_item(self, item_id, name, category, price, dimensions, in_stock=True):
        """Add a furniture item to the catalog"""
        self.items[item_id] = {
            'name': name,
            'category': category,
            'price': price,
            'dimensions': dimensions,  # dict with width, length, height
            'in_stock': in_stock
        }
        self.categories.add(category)
        return True

    def remove_item(self, item_id):
        """Remove an item from the catalog"""
        if item_id in self.items:
            del self.items[item_id]
            # Update categories
            self.categories = {item['category'] for item in self.items.values()}
            return True
        return False

    def update_price(self, item_id, new_price):
        """Update the price of an item"""
        if item_id in self.items:
            self.items[item_id]['price'] = new_price
            return True
        return False

    def toggle_stock_status(self, item_id):
        """Toggle the in-stock status of an item"""
        if item_id in self.items:
            self.items[item_id]['in_stock'] = not self.items[item_id]['in_stock']
            return True
        return False

    def get_item_details(self, item_id):
        """Get complete details of a specific item"""
        return self.items.get(item_id, None)

    def list_by_category(self, category):
        """List all items in a specific category"""
        return {item_id: details for item_id, details in self.items.items() 
                if details['category'] == category}

    def get_price_range(self):
        """Get minimum and maximum prices in catalog"""
        if not self.items:
            return None
        prices = [item['price'] for item in self.items.values()]
        return {'min': min(prices), 'max': max(prices)}

    def search_by_name(self, search_term):
        """Search items by name (case-insensitive)"""
        search_term = search_term.lower()
        return {item_id: details for item_id, details in self.items.items() 
                if search_term in details['name'].lower()}

    def get_available_items(self):
        """List all in-stock items"""
        return {item_id: details for item_id, details in self.items.items() 
                if details['in_stock']}

    def get_catalog_stats(self):
        """Get statistics about the catalog"""
        return {
            'total_items': len(self.items),
            'categories': len(self.categories),
            'in_stock': len([item for item in self.items.values() if item['in_stock']]),
            'out_of_stock': len([item for item in self.items.values() if not item['in_stock']])
        }