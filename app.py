import requests

from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
	
	url = "https://api.yelp.com/v3/businesses/search"
	

	lat = request.args.get("lat")
	print(lat)
	lng = request.args.get("lng")
	print(lng)
	cost = request.args.get("cost")
	print(cost)
	rad = request.args.get("rad")
	print(rad)
	cate = request.args.get("cate")
	print(cate)
	querystring = {"latitude": lat,"longitude":lng,"price":cost, "radius":rad, "categories":cate}
	payload = ""
	headers = {"Authorization": "Bearer qO9vfdRSc3by3ho-fklOOZffpyWsDZPXeDHD-PPPkIx1hhcpmN3IaC8HtI1zqj4_E-HYbEZs78u4UMVWRt5eG8_KmM3nhzqNXuLaUswaFIQWJkx9WSgzcO0UWXgSYnYx"}

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


	#print(response.json)
	return jsonify(response.text)

@app.route('/test')
def test():
	return jsonify({"success": "true"})