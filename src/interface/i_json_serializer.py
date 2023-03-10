import json


class JsonSerializer:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def from_json(self):
        return json.loads(self.to_json())
