# V1InboxesMailboxMessagesPostRequest


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
from lockally.models.v1_inboxes_mailbox_messages_post_request import V1InboxesMailboxMessagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1InboxesMailboxMessagesPostRequest from a JSON string
v1_inboxes_mailbox_messages_post_request_instance = V1InboxesMailboxMessagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1InboxesMailboxMessagesPostRequest.to_json())

# convert the object into a dict
v1_inboxes_mailbox_messages_post_request_dict = v1_inboxes_mailbox_messages_post_request_instance.to_dict()
# create an instance of V1InboxesMailboxMessagesPostRequest from a dict
v1_inboxes_mailbox_messages_post_request_from_dict = V1InboxesMailboxMessagesPostRequest.from_dict(v1_inboxes_mailbox_messages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


