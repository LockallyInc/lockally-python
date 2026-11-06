# UpdateTrackingPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_opens** | **bool** |  | [optional] 
**track_clicks** | **bool** |  | [optional] 

## Example

```python
from lockally.models.update_tracking_policy_request import UpdateTrackingPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrackingPolicyRequest from a JSON string
update_tracking_policy_request_instance = UpdateTrackingPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTrackingPolicyRequest.to_json())

# convert the object into a dict
update_tracking_policy_request_dict = update_tracking_policy_request_instance.to_dict()
# create an instance of UpdateTrackingPolicyRequest from a dict
update_tracking_policy_request_from_dict = UpdateTrackingPolicyRequest.from_dict(update_tracking_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


