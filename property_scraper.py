import requests
import json

API_ENDPOINT = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'

data = {
	'CultureId':1,
	'ApplicationId':1,
	'RecordsPerPage':9,
	'MaximumResults':9,
	'PropertySearchTypeId':1,
	'PriceMin':600000,
	'PriceMax':3000000,
	'TransactionTypeId':2,
	'StoreyRange':'0-0',
	'BuildingTypeId':1,
	'BedRange':'0-0',
	'BathRange':'0-0',
	'LongitudeMin':'-79.83311516500737',
	'LongitudeMax':'-79.56137520529057',
	'LatitudeMin':'43.43915833923067',
	'LatitudeMax':'43.48949362853605',
	'SortOrder':'A',
	'SortBy':1,
	'PolygonPoints':'-79.62549798492394 43.46763572471077,-79.64558236602745 43.494291139570706,-79.68042962554894 43.504750798635776,-79.71235864166222 43.50076638026952,-79.7384511709591 43.47573323909139,-79.75823844583327 43.475225379547226,-79.75613229278527 43.465891502687235,-79.78445641998253 43.43336500548521,-79.77854966518488 43.42989165800441,-79.7023320138177 43.39397799130074,-79.6315061331173 43.45854029974646,-79.62532632354699 43.467884895177,-79.62532632354699 43.46825864895044,-79.62549798492394 43.46763572471077',
	'PolyZoomLevel':13,
	'viewState':'m',
	'Longitude':-79.6900100708008,
	'Latitude':43.4664306640625,
	'ZoomLevel':12,
	'CurrentPage':1,
	'PropertyTypeGroupID':1,
	'Token':'D6TmfZprLI8kfnR6T3fYSMrpp7gM4druIvEkoS1p4Po=',
	'GUID':'20fdade4-fb61-47ba-919c-c22c2bdf7dca'
}

r = requests.post(API_ENDPOINT, data=data)
current_page = r.json()['Paging']['CurrentPage']
total_pages = r.json()['Paging']['TotalPages'] 


while current_page <= total_pages:
	data['CurrentPage'] = current_page
	r = requests.post(API_ENDPOINT, data=data)
	properties = r.json()['Results']
	
	for property in properties:
		print('MLS: {} - Postal: {} - Address: {} - Bedrooms: {} - Bathrooms: {} - Stories: {} - Price: {} - Page #: {} / {}'.format(property.get('MlsNumber', 'NO MSL NUMBER'), property.get('PostalCode', 'NO POSTAL CODE'), property.get('Property', {'error': 'No Property Key'}).get('Address', {'error': 'No Address Key'}).get('AddressText', {'error': 'No AddressText Key'}), property.get('Building', {'error': 'No Building Key'}).get('Bedrooms', {'error': 'No Bedrooms Key'}), property.get('Bedrooms', {'error': 'No Bedrroms Key'}).get('BedroomTotal', {'error': 'No BedroomTotal Key'}), property.get('Building', {'error': 'No Building Key'}).get('StoriesTotal', {'error': 'No StoriesTotal Key'}), property.get('Property', {'error': 'No Property Key'}).get('Price', {'error': 'No Price Key'}), current_page, total_pages))
		print('***********')
	
	current_page += 1	
