import requests
import sys
import logging


class OpenData:
	endpoint = "https://www.opendata.nhs.scot/en/api/3/action/datastore_search"

	resources = {
		# COVID
		'daily':                '287fc645-4352-4477-9c8c-55bc054b7e76', # Daily and Cumulative Cases
		'total_by_area':        'e8454cf0-1152-4bcb-b9da-4343f625dfef', # Total Cases By Council Area
		'daily_by_area':        '427f9a25-db22-4014-a3bc-893b68243055', # Daily Case Trends By Council Area
		'total_by_deprivation': 'a965ee86-0974-4c93-bbea-e839e27d7085', # Total Cases By Deprivation

		# Other
		'councils':             '967937c4-8d67-4f39-974f-fd58c4acfda5', # Mapping of council ID to name
		'population':           '09ebfefb-33f4-4f6a-8312-2d14e2b02ace', # Population by council
	}


	@staticmethod
	def fetch(resource, **kwargs):
		if resource not in OpenData.resources:
			logging.error(f"ERROR: Requested resource '{resource}' is not valid")
			return {}

		kwargs['resource_id'] = OpenData.resources[resource]
		r = requests.get(OpenData.endpoint, params=kwargs)

		if r.status_code != 200:
			logging.error(f'ERROR: Bad response from OpenData API:\n{r.content}')
			return {}

		json = r.json()
		return json['result']


	# Util method to just return the records from fetch()
	@staticmethod
	def fetch_records(resource, **kwargs):
		results = OpenData.fetch(resource, **kwargs)

		if 'records' in results:
			return results['records']
		
		logging.error(f'ERROR: OpenData API did not return any records:\n{results}')
		return {}
