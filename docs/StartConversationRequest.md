# StartConversationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **List[str]** |  | 
**cc** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | 
**html** | **str** |  | [optional] 

## Example

```python
from lockally.models.start_conversation_request import StartConversationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartConversationRequest from a JSON string
start_conversation_request_instance = StartConversationRequest.from_json(json)
# print the JSON string representation of the object
print(StartConversationRequest.to_json())

# convert the object into a dict
start_conversation_request_dict = start_conversation_request_instance.to_dict()
# create an instance of StartConversationRequest from a dict
start_conversation_request_from_dict = StartConversationRequest.from_dict(start_conversation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


