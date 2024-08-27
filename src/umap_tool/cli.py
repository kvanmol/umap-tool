import argparse
import os

# Clearing the Screen
# os.system('cls')

parser = argparse.ArgumentParser(prog="umap-tool",
                                 description="to do",
                                 epilog="to do")

subparsers = parser.add_subparsers(help="custom sub-command help",
                                   dest="sub_command")

# initialize umap
parser_new = subparsers.add_parser("init", help="help for the 'init' command")

# Create new map
parser_new = subparsers.add_parser("new", help="help for the 'new' command")
parser_new.add_argument("map_name",
                        type=str,
                        help="""Name of the new map
                        """)
parser_new.add_argument("root_directory",
                        type=str,
                        help="""root-directory of the new map.
                        """)

# remove map
parser_new = subparsers.add_parser("remove-map", help="help for the 'remove-map' command")
parser_new.add_argument("map_name",
                        type=str,
                        help="""Name of the map
                        """)

# Add layer
parser_new = subparsers.add_parser("add-layer", help="help for the 'add layer' command")
parser_new.add_argument("map_name",
                        type=str,
                        help="""Name of the map
                        """)
parser_new.add_argument("layer_name",
                        type=str,
                        help="""Name of the layer
                        """)
parser_new.add_argument("source_directory",
                        type=str,
                        help="""source-directory of the data used for the layer
                        """)

# remove layer
parser_new = subparsers.add_parser("remove-layer", help="help for the 'remove-layer' command")
parser_new.add_argument("map_name",
                        type=str,
                        help="""Name of the map
                        """)
parser_new.add_argument("layer_name",
                        type=str,
                        help="""Name of the layer
                        """)

# update map
parser_new = subparsers.add_parser("update-map", help="help for the 'update-map' command")
parser_new.add_argument("map_name",
                        type=str,
                        help="""Name of the map
                        """)

# Testing commands
# args = parser.parse_args(["init"])
# args = parser.parse_args(["new", "myTestMap", r"D:\Temp\umap"])
# args = parser.parse_args(["add-layer", "myTestMap","layer1", r"D:\Temp\umap_source\layer1"])
# args = parser.parse_args(["add-layer", "myTestMap","layer2", r"D:\Temp\umap_source\layer2"])
# args = parser.parse_args(["add-layer", "myTestMap","layer3", r"D:\Temp\umap_source\layer3"])
# args = parser.parse_args(["remove-layer", "mynewmap", "mynewlayer"])
# args = parser.parse_args(["remove-map", "mynewmap"])
# args = parser.parse_args(["update-map", "myTestMap"])





