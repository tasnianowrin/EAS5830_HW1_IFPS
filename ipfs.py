import requests
import json

PROJECT_ID = "PMy First Key"
PROJECT_SECRET = "XI7jDQtwaUApzU+hjw4HxcPksdmmMU5rZOy+VMLi5Y3iw7kwaMapmw"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://ipfs.infura.io:5001/api/v0/add"

	files = {
	"file": ("data.json", json.dumps(data), "application/json")
	}

	response = requests.post(
	url,
	files=files,
	auth=(PROJECT_ID, PROJECT_SECRET)
	)

	response.raise_for_status()
	cid = response.json()["Hash"]
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	url = f"https://ipfs.io/ipfs/{cid}"

	response = requests.get(url)
	response.raise_for_status()

	data = response.json()

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
