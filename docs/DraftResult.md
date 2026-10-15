# DraftResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_id** | **UUID** |  | 
**status** | **str** |  | 
**policy_flags** | **Dict[str, object]** |  | 
**thread_id** | **UUID** |  | [optional] 
**sent** | [**AgentSendResult**](AgentSendResult.md) |  | [optional] 

## Example

```python
from lockally.models.draft_result import DraftResult

# TODO update the JSON string below
json = "{}"
# create an instance of DraftResult from a JSON string
draft_result_instance = DraftResult.from_json(json)
# print the JSON string representation of the object
print(DraftResult.to_json())

# convert the object into a dict
draft_result_dict = draft_result_instance.to_dict()
# create an instance of DraftResult from a dict
draft_result_from_dict = DraftResult.from_dict(draft_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


