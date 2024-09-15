import os
import json


def json_file_stat(fp: str) -> str:
    stats = os.stat(fp)

    stat_dict = {k: getattr(stats, k) for k in dir(stats) if k.startswith("st_")}

    return json.dumps(stat_dict)


def object_to_json(obj: any) -> str:
    return json.dumps(obj, default=lambda o: o.__dict__)
