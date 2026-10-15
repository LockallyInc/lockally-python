# GetCalendarSecurity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_calendars** | **int** |  | [optional] 
**public_calendars** | **int** |  | [optional] 
**private_calendars** | **int** |  | [optional] 
**total_members** | **int** |  | [optional] 
**delegated_access** | [**List[GetCalendarSecurity200ResponseDelegatedAccessInner]**](GetCalendarSecurity200ResponseDelegatedAccessInner.md) |  | [optional] 
**public_calendar_list** | [**List[GetCalendarSecurity200ResponsePublicCalendarListInner]**](GetCalendarSecurity200ResponsePublicCalendarListInner.md) |  | [optional] 
**alerts** | [**List[GetCalendarSecurity200ResponseAlertsInner]**](GetCalendarSecurity200ResponseAlertsInner.md) |  | [optional] 
**external_sharing** | [**GetCalendarSecurity200ResponseExternalSharing**](GetCalendarSecurity200ResponseExternalSharing.md) |  | [optional] 

## Example

```python
from lockally.models.get_calendar_security200_response import GetCalendarSecurity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarSecurity200Response from a JSON string
get_calendar_security200_response_instance = GetCalendarSecurity200Response.from_json(json)
# print the JSON string representation of the object
print(GetCalendarSecurity200Response.to_json())

# convert the object into a dict
get_calendar_security200_response_dict = get_calendar_security200_response_instance.to_dict()
# create an instance of GetCalendarSecurity200Response from a dict
get_calendar_security200_response_from_dict = GetCalendarSecurity200Response.from_dict(get_calendar_security200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


