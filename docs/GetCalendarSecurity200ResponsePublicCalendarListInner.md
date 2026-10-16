# GetCalendarSecurity200ResponsePublicCalendarListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**member_count** | **int** |  | [optional] 
**has_feed** | **bool** |  | [optional] 

## Example

```python
from lockally.models.get_calendar_security200_response_public_calendar_list_inner import GetCalendarSecurity200ResponsePublicCalendarListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarSecurity200ResponsePublicCalendarListInner from a JSON string
get_calendar_security200_response_public_calendar_list_inner_instance = GetCalendarSecurity200ResponsePublicCalendarListInner.from_json(json)
# print the JSON string representation of the object
print(GetCalendarSecurity200ResponsePublicCalendarListInner.to_json())

# convert the object into a dict
get_calendar_security200_response_public_calendar_list_inner_dict = get_calendar_security200_response_public_calendar_list_inner_instance.to_dict()
# create an instance of GetCalendarSecurity200ResponsePublicCalendarListInner from a dict
get_calendar_security200_response_public_calendar_list_inner_from_dict = GetCalendarSecurity200ResponsePublicCalendarListInner.from_dict(get_calendar_security200_response_public_calendar_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


