# CalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**calendar_id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**uid** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**starts_at** | **datetime** |  | 
**ends_at** | **datetime** |  | 
**all_day** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.calendar_event import CalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEvent from a JSON string
calendar_event_instance = CalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEvent.to_json())

# convert the object into a dict
calendar_event_dict = calendar_event_instance.to_dict()
# create an instance of CalendarEvent from a dict
calendar_event_from_dict = CalendarEvent.from_dict(calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


