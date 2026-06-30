import requests
import json

PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5MmJlYjE4OS1hYWE0LTQ4NjYtOTZmMi02ZmUyMTc3NDI5OTEiLCJlbWFpbCI6Im5vd3JpbnRAc2Vhcy51cGVubi5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiM2ZjMWNiYWZlZGZlZTYyNGNjMmIiLCJzY29wZWRLZXlTZWNyZXQiOiI0ZGFkY2M3YzQ5NWUyZWJlZTlmNTRkMTkwNmZkN2Q2MjZkMWMwOGU2OTQyNzg3NmQxNDYyZGE3NmMxMjFhOTBlIiwiZXhwIjoxODE0MzI1NzIyfQ.L23QQQcj3zIKEio0beBFD2Zo2yCkhGmsrvImPbAxENo"


def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    headers = {
        "Authorization": f"Bearer {PINATA_JWT}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    cid = response.json()["IpfsHash"]

    return cid


def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"

    url = f"https://gateway.pinata.cloud/ipfs/{cid}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data