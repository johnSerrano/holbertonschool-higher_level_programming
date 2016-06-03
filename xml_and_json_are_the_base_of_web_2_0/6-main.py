from car import Car
import json

if __name__ == "__main__":
	with open("6-main.json") as f:
		cars_json_list = json.loads(f.read())
	cars = []
	for car in cars_json_list:
		cars.append(Car(car))
	for car in cars:
		print car.to_comma()
