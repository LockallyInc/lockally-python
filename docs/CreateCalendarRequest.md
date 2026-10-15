# CreateCalendarRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] [default to 'tenant']

## Example

```python
from lockally.models.create_calendar_request import CreateCalendarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCalendarRequest from a JSON string
create_calendar_request_instance = CreateCalendarRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCalendarRequest.to_json())

# convert the object into a dict
create_calendar_request_dict = create_calendar_request_instance.to_dict()
# create an instance of CreateCalendarRequest from a dict
create_calendar_request_from_dict = CreateCalendarRequest.from_dict(create_calendar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


