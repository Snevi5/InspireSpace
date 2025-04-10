class DesignThemeManager:
    def __init__(self, theme_name="default"):
        self.theme_name = theme_name
        self.colors = {}
        self.fonts = {}
        self.spacing = {}
        self.current_styles = {}
        
    def set_color_scheme(self, primary, secondary, accent, background):
        """Set the main color scheme for the theme"""
        self.colors = {
            'primary': primary,
            'secondary': secondary,
            'accent': accent,
            'background': background
        }
        return True

    def add_font_style(self, style_name, font_family, size, weight="normal"):
        """Add a font style to the theme"""
        self.fonts[style_name] = {
            'family': font_family,
            'size': size,
            'weight': weight
        }
        return True

    def set_spacing(self, padding, margin, gap):
        """Set spacing values for the theme"""
        self.spacing = {
            'padding': padding,
            'margin': margin,
            'gap': gap
        }
        return True

    def apply_theme(self):
        """Generate complete style dictionary from current settings"""
        self.current_styles = {
            'colors': self.colors.copy(),
            'fonts': self.fonts.copy(),
            'spacing': self.spacing.copy()
        }
        return self.current_styles

    def get_color(self, color_name):
        """Retrieve a specific color from the theme"""
        return self.colors.get(color_name, None)

    def get_font(self, style_name):
        """Retrieve a specific font style"""
        return self.fonts.get(style_name, None)

    def update_property(self, category, key, value):
        """Update a specific property in the theme"""
        if category == 'colors':
            self.colors[key] = value
        elif category == 'fonts':
            self.fonts[key] = value
        elif category == 'spacing':
            self.spacing[key] = value
        return True

    def save_theme(self, file_name):
        """Save current theme settings to a file (simulated)"""
        theme_data = {
            'name': self.theme_name,
            'colors': self.colors,
            'fonts': self.fonts,
            'spacing': self.spacing
        }
        # In a real implementation, this would write to a file
        print(f"Saving theme to {file_name}: {theme_data}")
        return True

    def load_theme(self, file_name):
        """Load theme settings from a file (simulated)"""
        # In a real implementation, this would read from a file
        print(f"Loading theme from {file_name}")
        return True

    def preview_theme(self):
        """Display a preview of current theme settings"""
        preview = {
            'Theme Name': self.theme_name,
            'Colors': self.colors,
            'Fonts': self.fonts,
            'Spacing': self.spacing
        }
        return preview

