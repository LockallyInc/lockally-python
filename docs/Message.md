# Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**message_id** | **str** | RFC 5322 Message-ID header, including angle brackets. | 
**sender** | **str** |  | 
**recipients** | **List[str]** |  | 
**subject** | **str** |  | [optional] 
**status** | **str** |  | 
**queued_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**bounce_reason** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 

## Example

```python
from lockally.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


