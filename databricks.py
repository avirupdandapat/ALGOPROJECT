from azure_databricks_api import AzureDatabricksRESTClient

azure_region = 'East US 2'
token = 'dapi04ff27ce22586d5e881cfe4474acb186'

client = AzureDatabricksRESTClient(region=azure_region, token=token)

print(client.workspace.)
