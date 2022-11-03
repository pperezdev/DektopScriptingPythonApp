import json
from app.action import Action

class ReadConfig:
    def __init__(self, filename="default-config.json"):
        data = self.open_file(filename)
        self.actions = self.read_config(data)
    
    def open_file(self, filename):
        data = ""
        with open(filename) as f:
            data = json.load(f)
        return data
    
    def read_config(self, data):
        actions = []
        for d in data["actions"]:
            act = Action(**d)
            actions.append(act)
        return actions
    
    def do_action(self):
        for act in self.actions:
            act.action()
        