class Texture:
    def __init__(self, name, file_path=None):
        self.name = name
        self.file_path = file_path
        self.repeat_u = 1.0
        self.repeat_v = 1.0
        self.scale_x = 1.0
        self.scale_y = 1.0
        self.opacity = 1.0
        self.bump_map = None
        self.reflectivity = 0.5
        self.roughness = 0.5
        self.applied_surfaces = []

    def load_texture(self, file_path):
        self.file_path = file_path
        print(f"[Texture] Loaded texture from {file_path}")

    def apply_to_surface(self, surface_id):
        self.applied_surfaces.append(surface_id)
        print(f"[Texture] Applied '{self.name}' to surface: {surface_id}")

    def set_repeat(self, u, v):
        self.repeat_u = u
        self.repeat_v = v
        print(f"[Texture] Repeat set to (U: {u}, V: {v})")

    def set_scale(self, scale_x, scale_y):
        self.scale_x = scale_x
        self.scale_y = scale_y
        print(f"[Texture] Scale set to (X: {scale_x}, Y: {scale_y})")

    def set_opacity(self, opacity):
        self.opacity = max(0.0, min(1.0, opacity))
        print(f"[Texture] Opacity set to {self.opacity}")

    def set_bump_map(self, bump_map_path):
        self.bump_map = bump_map_path
        print(f"[Texture] Bump map set from {bump_map_path}")

    def preview(self):
        print(f"[Texture] Previewing texture: {self.name} from {self.file_path}")

    def set_material_properties(self, reflectivity, roughness):
        self.reflectivity = reflectivity
        self.roughness = roughness
        print(f"[Texture] Reflectivity: {reflectivity}, Roughness: {roughness}")

    def get_texture_info(self):
        return {
            "name": self.name,
            "file_path": self.file_path,
            "repeat": (self.repeat_u, self.repeat_v),
            "scale": (self.scale_x, self.scale_y),
            "opacity": self.opacity,
            "bump_map": self.bump_map,
            "reflectivity": self.reflectivity,
            "roughness": self.roughness,
            "applied_surfaces": self.applied_surfaces
        }

    def remove_from_surface(self, surface_id):
        if surface_id in self.applied_surfaces:
            self.applied_surfaces.remove(surface_id)
            print(f"[Texture] Removed '{self.name}' from surface: {surface_id}")
        else:
            print(f"[Texture] Texture not applied to surface: {surface_id}")
