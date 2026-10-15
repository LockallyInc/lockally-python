# ListMailboxes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Mailbox]**](Mailbox.md) |  | 
**limit** | **int** |  | 

## Example

```python
from lockally.models.list_mailboxes200_response import ListMailboxes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMailboxes200Response from a JSON string
list_mailboxes200_response_instance = ListMailboxes200Response.from_json(json)
# print the JSON string representation of the object
print(ListMailboxes200Response.to_json())

# convert the object into a dict
list_mailboxes200_response_dict = list_mailboxes200_response_instance.to_dict()
# create an instance of ListMailboxes200Response from a dict
list_mailboxes200_response_from_dict = ListMailboxes200Response.from_dict(list_mailboxes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


