import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer
import json
import datetime

class DBList(rpyc.Service):
    value = []
    history = []

    def log(self, action):
        timestamp = datetime.datetime.now().isoformat()
        self.history.append(f"{timestamp} - {action}")

    def exposed_append(self, data):
        self.value.append(data)
        self.log(f"append({data})")
        return self.value

    def exposed_remove(self, data):
        if data in self.value:
            self.value.remove(data)
            self.log(f"remove({data})")
            return True
        self.log(f"remove({data}) - not found")
        return False

    def exposed_clear(self):
        self.value.clear()
        self.log("clear()")

    def exposed_value(self):
        return self.value

    def exposed_size(self):
        return len(self.value)

    def exposed_get(self, index):
        if 0 <= index < len(self.value):
            return self.value[index]
        return None

    def exposed_contains(self, item):
        return item in self.value

    def exposed_history(self):
        return self.history

    def exposed_save(self, filename="db_list.json"):
        with open(filename, "w") as f:
            json.dump(self.value, f)
        self.log(f"save('{filename}')")

    def exposed_load(self, filename="db_list.json"):
        try:
            with open(filename, "r") as f:
                self.value = json.load(f)
            self.log(f"load('{filename}')")
        except FileNotFoundError:
            self.log(f"load('{filename}') - file not found")

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
