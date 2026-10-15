# UpdateCalendarRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from lockally.models.update_calendar_request import UpdateCalendarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCalendarRequest from a JSON string
update_calendar_request_instance = UpdateCalendarRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCalendarRequest.to_json())

# convert the object into a dict
update_calendar_request_dict = update_calendar_request_instance.to_dict()
# create an instance of UpdateCalendarRequest from a dict
update_calendar_request_from_dict = UpdateCalendarRequest.from_dict(update_calendar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


