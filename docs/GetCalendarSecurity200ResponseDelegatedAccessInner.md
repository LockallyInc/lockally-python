# GetCalendarSecurity200ResponseDelegatedAccessInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_id** | **UUID** |  | [optional] 
**calendar_name** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**granted_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_calendar_security200_response_delegated_access_inner import GetCalendarSecurity200ResponseDelegatedAccessInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarSecurity200ResponseDelegatedAccessInner from a JSON string
get_calendar_security200_response_delegated_access_inner_instance = GetCalendarSecurity200ResponseDelegatedAccessInner.from_json(json)
# print the JSON string representation of the object
print(GetCalendarSecurity200ResponseDelegatedAccessInner.to_json())

# convert the object into a dict
get_calendar_security200_response_delegated_access_inner_dict = get_calendar_security200_response_delegated_access_inner_instance.to_dict()
# create an instance of GetCalendarSecurity200ResponseDelegatedAccessInner from a dict
get_calendar_security200_response_delegated_access_inner_from_dict = GetCalendarSecurity200ResponseDelegatedAccessInner.from_dict(get_calendar_security200_response_delegated_access_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


