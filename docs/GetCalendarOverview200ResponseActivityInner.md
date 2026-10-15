# GetCalendarOverview200ResponseActivityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**actor** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_calendar_overview200_response_activity_inner import GetCalendarOverview200ResponseActivityInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarOverview200ResponseActivityInner from a JSON string
get_calendar_overview200_response_activity_inner_instance = GetCalendarOverview200ResponseActivityInner.from_json(json)
# print the JSON string representation of the object
print(GetCalendarOverview200ResponseActivityInner.to_json())

# convert the object into a dict
get_calendar_overview200_response_activity_inner_dict = get_calendar_overview200_response_activity_inner_instance.to_dict()
# create an instance of GetCalendarOverview200ResponseActivityInner from a dict
get_calendar_overview200_response_activity_inner_from_dict = GetCalendarOverview200ResponseActivityInner.from_dict(get_calendar_overview200_response_activity_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


