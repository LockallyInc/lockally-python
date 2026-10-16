# MapMigrationRequestMappingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_email** | **str** |  | 
**dest_email** | **str** |  | 

## Example

```python
from lockally.models.map_migration_request_mappings_inner import MapMigrationRequestMappingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MapMigrationRequestMappingsInner from a JSON string
map_migration_request_mappings_inner_instance = MapMigrationRequestMappingsInner.from_json(json)
# print the JSON string representation of the object
print(MapMigrationRequestMappingsInner.to_json())

# convert the object into a dict
map_migration_request_mappings_inner_dict = map_migration_request_mappings_inner_instance.to_dict()
# create an instance of MapMigrationRequestMappingsInner from a dict
map_migration_request_mappings_inner_from_dict = MapMigrationRequestMappingsInner.from_dict(map_migration_request_mappings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


