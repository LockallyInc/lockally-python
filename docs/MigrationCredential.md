# MigrationCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**provider** | **str** |  | 
**encryption_key_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.migration_credential import MigrationCredential

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationCredential from a JSON string
migration_credential_instance = MigrationCredential.from_json(json)
# print the JSON string representation of the object
print(MigrationCredential.to_json())

# convert the object into a dict
migration_credential_dict = migration_credential_instance.to_dict()
# create an instance of MigrationCredential from a dict
migration_credential_from_dict = MigrationCredential.from_dict(migration_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


