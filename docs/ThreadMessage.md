# ThreadMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**direction** | **str** |  | 
**rfc_message_id** | **str** | The Internet Message-ID | 
**in_reply_to** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**var_from** | **str** |  | 
**to** | **List[str]** |  | 
**snippet** | **str** |  | [optional] 
**has_attachments** | **bool** |  | 
**attachments** | **List[Dict[str, object]]** |  | [optional] 
**annotations** | **Dict[str, object]** | Signals computed at ingest | [optional] 
**received_at** | **datetime** |  | 

## Example

```python
from lockally.models.thread_message import ThreadMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadMessage from a JSON string
thread_message_instance = ThreadMessage.from_json(json)
# print the JSON string representation of the object
print(ThreadMessage.to_json())

# convert the object into a dict
thread_message_dict = thread_message_instance.to_dict()
# create an instance of ThreadMessage from a dict
thread_message_from_dict = ThreadMessage.from_dict(thread_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


