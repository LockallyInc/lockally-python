# CreateMigrationCredentialRequestCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**port** | **int** |  | 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**oauth_token** | **str** |  | [optional] 

## Example

```python
from lockally.models.create_migration_credential_request_credentials import CreateMigrationCredentialRequestCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationCredentialRequestCredentials from a JSON string
create_migration_credential_request_credentials_instance = CreateMigrationCredentialRequestCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationCredentialRequestCredentials.to_json())

# convert the object into a dict
create_migration_credential_request_credentials_dict = create_migration_credential_request_credentials_instance.to_dict()
# create an instance of CreateMigrationCredentialRequestCredentials from a dict
create_migration_credential_request_credentials_from_dict = CreateMigrationCredentialRequestCredentials.from_dict(create_migration_credential_request_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


