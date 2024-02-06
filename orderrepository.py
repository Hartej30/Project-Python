
import csv

class OrderRepository:
    def __init__(self, filename: str):
        self.__filename = filename

    def save_orders(self, orders: list[dict]):
        with open(self.__filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["customer_name", "pizza_name"])
            for order in orders:
                writer.writerow([order["customer_name"], order["pizza_name"]])

    def load_orders(self) -> list[dict]:
        orders = []
        with open(self.__filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                orders.append(row)
        return orders
