import requests

WFS_ENDPOINT = "https://api.os.uk/features/v1/wfs"
KEY = 'vCGRsoADDTxbmamXfuvELPxlqVIv9nmN'

bbox = '51.0162,0.9160,51.0163,0.9268'
# for i in range(0, 60): PAGE THROUGH THESE INSTEAD
wfs_params = {
    'key': KEY,
    'service': 'wfs',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typeNames': 'Zoomstack_RoadsLocal',
    'outputFormat': 'GeoJSON',
    'srsName': 'EPSG:4326',
    'bbox': bbox,
    'count': 100
}
response = requests.get(WFS_ENDPOINT, params=wfs_params)
payload = response.json()

features = payload['features']

if features:
    print('Data Found')
else:
    print('No Data')