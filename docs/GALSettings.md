# GALSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **UUID** |  | 
**gal_enabled** | **bool** |  | 
**hide_from_directory** | **bool** |  | 
**department_grouping** | **bool** |  | 
**search_visibility** | **str** |  | 
**include_external_contacts** | **bool** |  | 
**last_index_rebuilt_at** | **datetime** |  | [optional] 
**last_synced_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.gal_settings import GALSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GALSettings from a JSON string
gal_settings_instance = GALSettings.from_json(json)
# print the JSON string representation of the object
print(GALSettings.to_json())

# convert the object into a dict
gal_settings_dict = gal_settings_instance.to_dict()
# create an instance of GALSettings from a dict
gal_settings_from_dict = GALSettings.from_dict(gal_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


