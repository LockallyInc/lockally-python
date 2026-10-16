# ThreadMessageBodyBody

Absent when the stored message could not be fetched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**truncated** | **bool** |  | [optional] 

## Example

```python
from lockally.models.thread_message_body_body import ThreadMessageBodyBody

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadMessageBodyBody from a JSON string
thread_message_body_body_instance = ThreadMessageBodyBody.from_json(json)
# print the JSON string representation of the object
print(ThreadMessageBodyBody.to_json())

# convert the object into a dict
thread_message_body_body_dict = thread_message_body_body_instance.to_dict()
# create an instance of ThreadMessageBodyBody from a dict
thread_message_body_body_from_dict = ThreadMessageBodyBody.from_dict(thread_message_body_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


