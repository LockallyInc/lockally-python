# UpdateGALSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gal_enabled** | **bool** |  | [optional] 
**hide_from_directory** | **bool** |  | [optional] 
**department_grouping** | **bool** |  | [optional] 
**search_visibility** | **str** |  | [optional] 
**include_external_contacts** | **bool** |  | [optional] 

## Example

```python
from lockally.models.update_gal_settings_request import UpdateGALSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGALSettingsRequest from a JSON string
update_gal_settings_request_instance = UpdateGALSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGALSettingsRequest.to_json())

# convert the object into a dict
update_gal_settings_request_dict = update_gal_settings_request_instance.to_dict()
# create an instance of UpdateGALSettingsRequest from a dict
update_gal_settings_request_from_dict = UpdateGALSettingsRequest.from_dict(update_gal_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


