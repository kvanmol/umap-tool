# Umap-tool

# CLI commands

## "init" - initialize the Umap-tool
First time use off the app "init" command need to be used to create necessary configuration.
If the init command is used, first check if the "umap_main_config.yaml" file exist, if not create it.
The file is create in a default location and at the moment the user cannot change the location.
default location is defined by: Path.home() and on windows this is "C:\Users\username"
The init command takes no extra arguments.

## "new" - creating a nem map
A new map can be created by a "new" command followed by "map-name" and a path to the "root-directory". If the root-directory doesn't exist it will be created (the parent directory need to exist). The folder structure will also be created together with a configuration file specific for that map.

Root directory is structured like this:
```
├───icons
    ├───<icon_name_1>.cvg
    ├───<icon_name_2>.cvg
    ├───...
├───layers
    ├───<name_layer-1>.geojson
    ├───<name_layer-2>.geojson
    ├───...
└───map_config.yaml
```

## "add layer" - adding a layer to the map
"add layer" "map name" "layer name" "source-dir"

## "update" - update an existing map


## "remove-map"

## "remove-layer"
"map name" "layer name"






## OLD - Folder structure - fileserver
Root directory of the fileserver is structured like this:
```
├───icons
    ├───<icon_name_1>.csv
    ├───<icon_name_2>.csv
    ├───...
├───layers
    ├───<name_layer-1>.geojson
    ├───<name_layer-2>.geojson
    ├───...
└───raw
    ├───<name_layer-1>
        ├───<track_or_waypoints_1>.gpx
        ├───<track_or_waypoints_2>.gpx
    ├───<name_layer-2>
        ├───<track_or_waypoints_1>.gpx
        ├───<track_or_waypoints_2>.gpx
    ├───...
```

- ```icons``` directory is used to collect all customized icons. Recommended format for an icon is ".svg".
- Each ".geojson" file in the directory ```layers``` represents a single layer in umap. The name of the ".geojson" file is used as the name of the layer (underscores are replaced by a blank space). These files are automatically generated.
- Each folder in the ```raw``` directory represents a layer and should contain a one or more ".gpx" files. The ".gpx" files can contain multiple tracks and/or waypoints. The ".gpx" files are provided by the user.

Example:
```
├───icons
    ├───campground.csv
    ├───shelter.csv
    ├───...
├───layers
    ├───Eurasia.geojson
    ├───Scandinavia.geojson
    ├───Sleeping_Places.geojson
└───raw
    ├───Eurasia
    |   ├───europe.gpx
    |   ├───asia.gpx
    ├───Scandinavia
    |   ├───sweden.gpx
    |   ├───finland.gpx
    └───Sleeping_Places
        ├───eurasia_sleeping.gpx
        └───scandinavia_sleeping.gpx
```

## Naming convention - ".gpx" files

