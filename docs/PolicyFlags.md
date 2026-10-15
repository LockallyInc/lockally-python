# PolicyFlags

Why a draft was held. A key is absent when that check passed. The set is closed: a flag added to the policy engine must be added here too, or typed clients will drop it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_approve** | **bool** |  | [optional] 
**injection_risk** | **bool** |  | [optional] 
**new_recipient** | **List[str]** |  | [optional] 
**new_thread** | **bool** |  | [optional] 
**pii** | **List[str]** |  | [optional] 
**recipient_count** | **int** |  | [optional] 

## Example

```python
from lockally.models.policy_flags import PolicyFlags

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyFlags from a JSON string
policy_flags_instance = PolicyFlags.from_json(json)
# print the JSON string representation of the object
print(PolicyFlags.to_json())

# convert the object into a dict
policy_flags_dict = policy_flags_instance.to_dict()
# create an instance of PolicyFlags from a dict
policy_flags_from_dict = PolicyFlags.from_dict(policy_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


