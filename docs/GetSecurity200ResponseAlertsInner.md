# GetSecurity200ResponseAlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_security200_response_alerts_inner import GetSecurity200ResponseAlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecurity200ResponseAlertsInner from a JSON string
get_security200_response_alerts_inner_instance = GetSecurity200ResponseAlertsInner.from_json(json)
# print the JSON string representation of the object
print(GetSecurity200ResponseAlertsInner.to_json())

# convert the object into a dict
get_security200_response_alerts_inner_dict = get_security200_response_alerts_inner_instance.to_dict()
# create an instance of GetSecurity200ResponseAlertsInner from a dict
get_security200_response_alerts_inner_from_dict = GetSecurity200ResponseAlertsInner.from_dict(get_security200_response_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


