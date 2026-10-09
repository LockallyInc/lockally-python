# CalendarIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**provider** | **str** |  | 
**label** | **str** |  | [optional] 
**status** | **str** |  | 
**last_sync_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.calendar_integration import CalendarIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarIntegration from a JSON string
calendar_integration_instance = CalendarIntegration.from_json(json)
# print the JSON string representation of the object
print(CalendarIntegration.to_json())

# convert the object into a dict
calendar_integration_dict = calendar_integration_instance.to_dict()
# create an instance of CalendarIntegration from a dict
calendar_integration_from_dict = CalendarIntegration.from_dict(calendar_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


