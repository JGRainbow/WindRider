import requests

key = 'vCGRsoADDTxbmamXfuvELPxlqVIv9nmN'

# bottom-left x, bottom-left y, top-right x, top-right y
bounds = [51.0162, 0.9160, 52.1388, 1.1877]
bbox = str(bounds[0]) + ',' + str(bounds[1]) + ',' + str(bounds[2]) + ',' + str(bounds[3])
print(bbox)


wfs_endpoint = "https://api.os.uk/features/v1/wfs"
wfs_params = {
    'key': key,
    'service': 'wfs',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typeNames': 'Zoomstack_RoadsLocal',
    'outputFormat': 'GeoJSON',
    'srsName': 'EPSG:4326',
    'bbox': bbox,
    'count': 5
}

# working_url = "https://api.os.uk/features/v1/wfs?key=vCGRsoADDTxbmamXfuvELPxlqVIv9nmN&service=wfs&version=2.0.0&request=GetFeature&typeNames=Zoomstack_RoadsLocal&outputFormat=GeoJSON&srsName=EPSG:4326&count=5"

response = requests.get(wfs_endpoint, params=wfs_params)
payload = response.json()
print(payload)
