# CreateMigrationCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**label** | **str** |  | [optional] 
**credentials** | [**CreateMigrationCredentialRequestCredentials**](CreateMigrationCredentialRequestCredentials.md) |  | 

## Example

```python
from lockally.models.create_migration_credential_request import CreateMigrationCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationCredentialRequest from a JSON string
create_migration_credential_request_instance = CreateMigrationCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationCredentialRequest.to_json())

# convert the object into a dict
create_migration_credential_request_dict = create_migration_credential_request_instance.to_dict()
# create an instance of CreateMigrationCredentialRequest from a dict
create_migration_credential_request_from_dict = CreateMigrationCredentialRequest.from_dict(create_migration_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


