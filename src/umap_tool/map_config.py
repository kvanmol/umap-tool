from dataclasses import dataclass, field
from typing import List, Optional
import yaml
from pathlib import Path
import re

# TODO: Check datatype for weight and opacity
# TODO: Implement getters and setter for some properties like "_icon_filename" (should end with .svg)
# TODO: Implement Docstrings for classes and methods
# TODO: Write unittests

def remove_leading_underscore(s: str) -> str:
    if s and s[0] == '_':
        return s[1:]
    return s

def is_hex_color(string):
    pattern = r"^#[0-9A-Fa-f]{6}$" # The regex pattern definition for a hex color
    return bool(re.match(pattern, string))

@dataclass
class Icon:
    icon_filename: str
    icon_color: str

    @property
    def icon_filename(self) -> str:
        return self._icon_filename
    
    @icon_filename.setter
    def icon_filename(self, filename: str):
        if not filename.endswith(".svg"):
            raise ValueError("Icon filename must end with '.svg'")
        self._icon_filename = filename

    @property
    def icon_color(self) -> str:
        return self._icon_color
    
    @icon_color.setter
    def icon_color(self, color: str):
        if not is_hex_color(color):
            raise ValueError("Icon color is not a valid hex color")
        self._icon_color = color

@dataclass
class Waypoint:
    name: str
    icon: Icon

@dataclass
class Track:
    name: str
    weight: float 
    opacity: float
    color: str

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        if not is_hex_color(color):
            raise ValueError("color is not a valid hex color")
        self._color = color


@dataclass
class MapStyle:
    waypoints: List[Waypoint] = field(default_factory=list)
    tracks: List[Track] = field(default_factory=list)

@dataclass
class Layer:
    name: str
    source_directory: str

@dataclass
class MapConfig:
    map_name: Optional[str] = None
    root_directory: Optional[str] = None
    layers: List[Layer] = field(default_factory=list)
    map_style: MapStyle = field(default_factory=MapStyle)
    _file_extension = ".yaml"

    @property
    def filename(self) -> str:
        if self.map_name is None or self.root_directory is None:
            if self.map_name is None:
                print("The field 'map_name' is not defined!")
            if self.root_directory is None:
                print("The field 'root_directory' is not defined!")
        else:
            name = f"{self.map_name.replace(" ", "_")}_config"
            if self.root_directory == "":
                return Path(name).with_suffix(self._file_extension)
            else:
                return Path(self.root_directory).joinpath(name).with_suffix(self._file_extension)

    @staticmethod
    def from_yaml(filename: str) -> 'MapConfig':
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        
        layers = [Layer(**layer) for layer in data['layers']]
        waypoints = [Waypoint(name=wp['name'], icon=Icon(**wp['icon'])) for wp in data['map_style']['waypoints']]
        tracks = [Track(**track) for track in data['map_style']['tracks']]
        
        map_style = MapStyle(
            waypoints=waypoints,
            tracks=tracks
        )
        
        return MapConfig(
            map_name=data['map_name'],
            root_directory=data['root_directory'],
            layers=layers,
            map_style=map_style
        )
    
    def _create_dict(self):
        def remove_dataclass_metadata(obj):
            if isinstance(obj, list):
                # return [remove_dataclass_metadata(i) for i in obj]
                result = []
                for i in obj:
                    result.append(remove_dataclass_metadata(i))
                return result
            elif isinstance(obj, dict):
                # return {k: remove_dataclass_metadata(v) for k, v in obj.items()}
                result = {}
                for k, v in obj.items():
                    result[k] = remove_dataclass_metadata(v)
                return result
            elif hasattr(obj, '__dict__'):
                # return {k: remove_dataclass_metadata(v) for k, v in obj.__dict__.items()}
                result = {}
                for k, v in obj.__dict__.items():
                    # Fix: leading underscore
                    if k.startswith("_"):
                        # without this fix, the .yaml file will contain the 
                        # leading underscore for every "private" attribute.
                        k = remove_leading_underscore(k)
                    result[k] = remove_dataclass_metadata(v)
                return result
            else:
                return obj
            
        return remove_dataclass_metadata(self.__dict__)

    def to_yaml(self):
        data_dict = self._create_dict()
        with open(self.filename, 'w') as file:
            yaml.dump(data_dict, file, sort_keys=False)

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def delete_layer(self, layer_name: str):
        self.layers = [layer for layer in self.layers if layer.name != layer_name]

    def get_layer(self, layer_name: str) -> Optional[Layer]:
        for layer in self.layers:
            if layer.name == layer_name:
                return layer
        return None

    def add_waypoint(self, waypoint: Waypoint):
        self.map_style.waypoints.append(waypoint)

    def delete_waypoint(self, waypoint_name: str):
        self.map_style.waypoints = [wp for wp in self.map_style.waypoints if wp.name != waypoint_name]

    def get_waypoint(self, waypoint_name: str) -> Optional[Waypoint]:
        for wp in self.map_style.waypoints:
            if wp.name == waypoint_name:
                return wp
        return None

    def add_track(self, track: Track):
        self.map_style.tracks.append(track)

    def delete_track(self, track_name: str):
        self.map_style.tracks = [track for track in self.map_style.tracks if track.name != track_name]

    def get_track(self, track_name: str) -> Optional[Track]:
        for track in self.map_style.tracks:
            if track.name == track_name:
                return track
        return None

    def add_icon_to_waypoint(self, waypoint_name: str, icon: Icon):
        waypoint = self.get_waypoint(waypoint_name)
        if waypoint:
            waypoint.icon = icon

    def update_waypoint_icon(self, waypoint_name: str, 
                             icon_filename: str, 
                             icon_color: str):
        waypoint = self.get_waypoint(waypoint_name)
        if waypoint:
            waypoint.icon.icon_filename = icon_filename
            waypoint.icon.icon_color = icon_color
        else:
            raise ValueError(f"waypoint with name: {waypoint_name} doesn't exist.")



# Create Configuration file
# =========================
# map_config = MapConfig()

# # Set map name and root directory
# map_config.map_name = 'My New Map'
# map_config.root_directory = ''

# # Add a new layer
# new_layer = Layer(name='layer1', source_directory='/path/to/layer1')
# map_config.add_layer(new_layer)

# new_layer = Layer(name='layer2', source_directory='/path/to/layer2')
# map_config.add_layer(new_layer)

# new_layer = Layer(name='layer3', source_directory='/path/to/layer3')
# map_config.add_layer(new_layer)

# # Add a new waypoints with an icon
# new_waypoint = Waypoint(name='camping', icon=Icon(icon_filename='tent.svg', icon_color='#FFFFFF'))
# map_config.add_waypoint(new_waypoint)

# new_waypoint = Waypoint(name='hostel', icon=Icon(icon_filename='accommodation.svg', icon_color='#FFFAAA'))
# map_config.add_waypoint(new_waypoint)

# new_waypoint = Waypoint(name='Wildcamping', icon=Icon(icon_filename='tent.svg', icon_color='#000000'))
# map_config.add_waypoint(new_waypoint)

# # Add a new tracks
# new_track = Track(name='Cycled', color='#555666', weight=10, opacity=0.9)
# map_config.add_track(new_track)

# new_track = Track(name='Public Transport', color='#999999', weight=5, opacity=0.7)
# map_config.add_track(new_track)

# # Save the updated Mapconfiguration to a YAML file
# map_config.to_yaml()


# Read existing config file and save it again
# ===========================================
map_config = MapConfig.from_yaml("My_New_Map_config.yaml")
print(map_config.filename)
map_config.map_name = "second map"
print(map_config.filename)
new_waypoint = Waypoint(name='Wildcamping', icon=Icon(icon_filename='tent.svg', icon_color='#000000'))
map_config.add_waypoint(new_waypoint)
map_config.to_yaml()




# try to update a waypoint icon with a wrong color value
# ======================================================

# Update the icon of the existing waypoint
# map_config.update_waypoint_icon('camping', icon_filename='new_tent.svg', icon_color='#000000')
# map_config.update_waypoint_icon('hostel', icon_filename='new_acco.svg', icon_color='#000333')
# map_config.update_waypoint_icon('Wildcamping', icon_filename='new_tent.svg', icon_color='#000555')

# Get a waypoint and its icon
# waypoint = map_config.get_waypoint('camping')
# if waypoint:
#     icon = waypoint.icon
#     print(f"Waypoint name: {waypoint.name}, Icon Name: {icon.icon_filename}, Icon Color: {icon.icon_color}, Icon Location: {icon.icon_location}")



