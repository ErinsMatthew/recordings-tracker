import os
import json


def json_file_stat(fp: str) -> str:
    s_obj = os.stat(fp)
    stat_dict = {k: getattr(s_obj, k) for k in dir(s_obj) if k.startswith("st_")}

    return json.dumps(stat_dict)


def object_to_json(obj: any) -> str:
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)
