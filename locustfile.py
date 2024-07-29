import time
import uuid
from locust import HttpUser, task, between
from faker import Faker


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    faker = Faker()

    def make_payload(self) -> str:
        key = uuid.uuid4()
        return {"key": str(key),
         "payload": {
            "street": self.faker.street_name(),
            "number" : int(self.faker.random_int(min=1, max=999)),
            "city" : self.faker.city(),
            "postalCode" : self.faker.postalcode()
        }}

    @task
    def view_items(self):
        for item_id in range(10):
            self.client.post("/message", json=self.make_payload())
            # time.sleep(1)

