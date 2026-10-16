# CreateCalendarIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from lockally.models.create_calendar_integration_request import CreateCalendarIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCalendarIntegrationRequest from a JSON string
create_calendar_integration_request_instance = CreateCalendarIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCalendarIntegrationRequest.to_json())

# convert the object into a dict
create_calendar_integration_request_dict = create_calendar_integration_request_instance.to_dict()
# create an instance of CreateCalendarIntegrationRequest from a dict
create_calendar_integration_request_from_dict = CreateCalendarIntegrationRequest.from_dict(create_calendar_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


