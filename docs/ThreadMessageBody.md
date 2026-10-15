# ThreadMessageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **UUID** |  | 
**mailbox** | **str** |  | 
**message** | [**ThreadMessage**](ThreadMessage.md) |  | 
**body** | [**ThreadMessageBodyBody**](ThreadMessageBodyBody.md) |  | [optional] 
**body_unavailable** | **str** | Present instead of body when the message could not be located in the mailbox. | [optional] 

## Example

```python
from lockally.models.thread_message_body import ThreadMessageBody

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadMessageBody from a JSON string
thread_message_body_instance = ThreadMessageBody.from_json(json)
# print the JSON string representation of the object
print(ThreadMessageBody.to_json())

# convert the object into a dict
thread_message_body_dict = thread_message_body_instance.to_dict()
# create an instance of ThreadMessageBody from a dict
thread_message_body_from_dict = ThreadMessageBody.from_dict(thread_message_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


