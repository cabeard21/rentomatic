import json


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = o.to_dict()
            to_serialize["code"] = str(to_serialize["code"])
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
