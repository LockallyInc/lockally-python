# TrackingPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_opens** | **bool** |  | 
**track_clicks** | **bool** |  | 
**updated_at** | **datetime** | Absent until a policy has been set. | [optional] 
**configured** | **bool** | Whether this deployment holds a tracking signing secret. False means tracking cannot work whatever the flags say. | 

## Example

```python
from lockally.models.tracking_policy import TrackingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingPolicy from a JSON string
tracking_policy_instance = TrackingPolicy.from_json(json)
# print the JSON string representation of the object
print(TrackingPolicy.to_json())

# convert the object into a dict
tracking_policy_dict = tracking_policy_instance.to_dict()
# create an instance of TrackingPolicy from a dict
tracking_policy_from_dict = TrackingPolicy.from_dict(tracking_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


