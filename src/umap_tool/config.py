from umap_tool.tools import remove_leading_underscore
from pathlib import Path


def get_map_config_filename(map_name: str, root_directory: str, file_extension: str = ".yaml") -> str:
    name = f"{map_name.replace(" ", "_")}_config"
    if root_directory == "":
        return Path(name).with_suffix(file_extension)
    else:
        return Path(root_directory).joinpath(name).with_suffix(file_extension)

def create_dict_from_obj(obj):
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
    return remove_dataclass_metadata(obj.__dict__)