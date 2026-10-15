# InboxList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inboxes** | [**List[Inbox]**](Inbox.md) |  | 

## Example

```python
from lockally.models.inbox_list import InboxList

# TODO update the JSON string below
json = "{}"
# create an instance of InboxList from a JSON string
inbox_list_instance = InboxList.from_json(json)
# print the JSON string representation of the object
print(InboxList.to_json())

# convert the object into a dict
inbox_list_dict = inbox_list_instance.to_dict()
# create an instance of InboxList from a dict
inbox_list_from_dict = InboxList.from_dict(inbox_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


