# SendMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **List[str]** |  | 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**unsubscribe** | **bool** |  | [optional] 
**template_id** | **UUID** |  | [optional] 
**variables** | **Dict[str, str]** |  | [optional] 
**send_at** | **datetime** |  | [optional] 
**attachments** | [**List[V1SendPostRequestAttachmentsInner]**](V1SendPostRequestAttachmentsInner.md) |  | [optional] 

## Example

```python
from lockally.models.send_message import SendMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessage from a JSON string
send_message_instance = SendMessage.from_json(json)
# print the JSON string representation of the object
print(SendMessage.to_json())

# convert the object into a dict
send_message_dict = send_message_instance.to_dict()
# create an instance of SendMessage from a dict
send_message_from_dict = SendMessage.from_dict(send_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


