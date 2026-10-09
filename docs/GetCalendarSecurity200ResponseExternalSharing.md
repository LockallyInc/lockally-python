# GetCalendarSecurity200ResponseExternalSharing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites_allowed** | **bool** |  | [optional] 
**sharing_allowed** | **bool** |  | [optional] 
**public_links** | **bool** |  | [optional] 

## Example

```python
from lockally.models.get_calendar_security200_response_external_sharing import GetCalendarSecurity200ResponseExternalSharing

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarSecurity200ResponseExternalSharing from a JSON string
get_calendar_security200_response_external_sharing_instance = GetCalendarSecurity200ResponseExternalSharing.from_json(json)
# print the JSON string representation of the object
print(GetCalendarSecurity200ResponseExternalSharing.to_json())

# convert the object into a dict
get_calendar_security200_response_external_sharing_dict = get_calendar_security200_response_external_sharing_instance.to_dict()
# create an instance of GetCalendarSecurity200ResponseExternalSharing from a dict
get_calendar_security200_response_external_sharing_from_dict = GetCalendarSecurity200ResponseExternalSharing.from_dict(get_calendar_security200_response_external_sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


