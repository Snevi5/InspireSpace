class LightingDesigner:
    def __init__(self, designer_name="Anonymous"):
        self.designer_name = designer_name
        self.projects = {}
        self.materials = {}
        self.next_project_id = 1

    def create_project(self, project_name, room_dimensions):
        """Create a new lighting project"""
        project_id = f"PRJ{self.next_project_id:04d}"
        self.projects[project_id] = {
            'name': project_name,
            'dimensions': room_dimensions,  # dict with width, length, height
            'lighting_zones': {},
            'budget': 0
        }
        self.next_project_id += 1
        return project_id

    def add_lighting_zone(self, project_id, zone_name, area):
        """Add a lighting zone to a project"""
        if project_id in self.projects:
            self.projects[project_id]['lighting_zones'][zone_name] = {
                'area': area,
                'fixtures': [],
                'cost': 0
            }
            return True
        return False

    def assign_fixture_to_zone(self, project_id, zone_name, fixture_type, cost):
        """Assign a fixture to a specific zone"""
        if (project_id in self.projects and 
            zone_name in self.projects[project_id]['lighting_zones']):
            zone = self.projects[project_id]['lighting_zones'][zone_name]
            zone['fixtures'].append(fixture_type)
            zone['cost'] += cost
            self.projects[project_id]['budget'] += cost
            return True
        return False

    def set_project_budget(self, project_id, budget):
        """Set or update project budget"""
        if project_id in self.projects:
            self.projects[project_id]['budget'] = budget
            return True
        return False

    def calculate_zone_coverage(self, project_id, zone_name):
        """Calculate percentage of room covered by a zone"""
        if (project_id in self.projects and 
            zone_name in self.projects[project_id]['lighting_zones']):
            room = self.projects[project_id]['dimensions']
            room_area = room['width'] * room['length']
            zone_area = self.projects[project_id]['lighting_zones'][zone_name]['area']
            return (zone_area / room_area) * 100 if room_area > 0 else 0
        return 0

    def get_project_cost(self, project_id):
        """Get total cost of all fixtures in project"""
        if project_id in self.projects:
            return sum(zone['cost'] for zone in 
                      self.projects[project_id]['lighting_zones'].values())
        return 0

    def add_material(self, material_id, name, unit_cost):
        """Add a lighting material to inventory"""
        self.materials[material_id] = {
            'name': name,
            'unit_cost': unit_cost
        }
        return True

    def get_project_details(self, project_id):
        """Get complete project specifications"""
        return self.projects.get(project_id, None)

    def remove_zone(self, project_id, zone_name):
        """Remove a lighting zone from a project"""
        if (project_id in self.projects and 
            zone_name in self.projects[project_id]['lighting_zones']):
            zone_cost = self.projects[project_id]['lighting_zones'][zone_name]['cost']
            self.projects[project_id]['budget'] -= zone_cost
            del self.projects[project_id]['lighting_zones'][zone_name]
            return True
        return False

    def generate_project_report(self, project_id):
        """Generate a detailed project report"""
        if project_id not in self.projects:
            return None
        project = self.projects[project_id]
        report = {
            'project_id': project_id,
            'name': project['name'],
            'total_cost': self.get_project_cost(project_id),
            'budget': project['budget'],
            'zones': len(project['lighting_zones']),
            'zone_details': {}
        }
        for zone_name, zone in project['lighting_zones'].items():
            report['zone_details'][zone_name] = {
                'coverage': self.calculate_zone_coverage(project_id, zone_name),
                'fixture_count': len(zone['fixtures']),
                'cost': zone['cost']
            }
        return report