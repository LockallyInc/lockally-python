# MapMigrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[MapMigrationRequestMappingsInner]**](MapMigrationRequestMappingsInner.md) |  | 

## Example

```python
from lockally.models.map_migration_request import MapMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapMigrationRequest from a JSON string
map_migration_request_instance = MapMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(MapMigrationRequest.to_json())

# convert the object into a dict
map_migration_request_dict = map_migration_request_instance.to_dict()
# create an instance of MapMigrationRequest from a dict
map_migration_request_from_dict = MapMigrationRequest.from_dict(map_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


