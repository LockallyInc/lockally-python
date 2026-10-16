# Inbox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**email** | **str** |  | 
**last_message_at** | **datetime** |  | [optional] 
**thread_count** | **int** |  | 

## Example

```python
from lockally.models.inbox import Inbox

# TODO update the JSON string below
json = "{}"
# create an instance of Inbox from a JSON string
inbox_instance = Inbox.from_json(json)
# print the JSON string representation of the object
print(Inbox.to_json())

# convert the object into a dict
inbox_dict = inbox_instance.to_dict()
# create an instance of Inbox from a dict
inbox_from_dict = Inbox.from_dict(inbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


