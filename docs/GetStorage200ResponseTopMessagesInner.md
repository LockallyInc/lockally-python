# GetStorage200ResponseTopMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**filenames** | **List[str]** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_storage200_response_top_messages_inner import GetStorage200ResponseTopMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorage200ResponseTopMessagesInner from a JSON string
get_storage200_response_top_messages_inner_instance = GetStorage200ResponseTopMessagesInner.from_json(json)
# print the JSON string representation of the object
print(GetStorage200ResponseTopMessagesInner.to_json())

# convert the object into a dict
get_storage200_response_top_messages_inner_dict = get_storage200_response_top_messages_inner_instance.to_dict()
# create an instance of GetStorage200ResponseTopMessagesInner from a dict
get_storage200_response_top_messages_inner_from_dict = GetStorage200ResponseTopMessagesInner.from_dict(get_storage200_response_top_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


