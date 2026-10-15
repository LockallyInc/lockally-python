# UpdateCalendarIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from lockally.models.update_calendar_integration_request import UpdateCalendarIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCalendarIntegrationRequest from a JSON string
update_calendar_integration_request_instance = UpdateCalendarIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCalendarIntegrationRequest.to_json())

# convert the object into a dict
update_calendar_integration_request_dict = update_calendar_integration_request_instance.to_dict()
# create an instance of UpdateCalendarIntegrationRequest from a dict
update_calendar_integration_request_from_dict = UpdateCalendarIntegrationRequest.from_dict(update_calendar_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


