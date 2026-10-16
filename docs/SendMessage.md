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
**reply_to** | **str** | Where replies go. Required when &#x60;from&#x60; has no mailbox behind it. The named form &#x60;Acme Support &lt;a@b.com&gt;&#x60; is also accepted. | [optional] 
**reply_to_name** | **str** | Display name shown on &#x60;Reply-To&#x60;. Ignored without &#x60;reply_to&#x60;. | [optional] 
**unsubscribe** | **bool** |  | [optional] 
**template_id** | **UUID** |  | [optional] 
**variables** | **Dict[str, str]** |  | [optional] 
**send_at** | **datetime** |  | [optional] 
**attachments** | [**List[SendEmailRequestAttachmentsInner]**](SendEmailRequestAttachmentsInner.md) |  | [optional] 

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


