# AgentSendResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The Lockally message id. | [optional] 
**status** | **str** |  | [optional] 
**thread_id** | **UUID** | The conversation the message joined. | 

## Example

```python
from lockally.models.agent_send_result import AgentSendResult

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSendResult from a JSON string
agent_send_result_instance = AgentSendResult.from_json(json)
# print the JSON string representation of the object
print(AgentSendResult.to_json())

# convert the object into a dict
agent_send_result_dict = agent_send_result_instance.to_dict()
# create an instance of AgentSendResult from a dict
agent_send_result_from_dict = AgentSendResult.from_dict(agent_send_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


