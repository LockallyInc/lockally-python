# GetStorage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_bytes** | **int** |  | [optional] 
**alloc_bytes** | **int** |  | [optional] 
**per_seat_bytes** | **int** |  | [optional] 
**top_mailboxes** | [**List[GetStorage200ResponseTopMailboxesInner]**](GetStorage200ResponseTopMailboxesInner.md) |  | [optional] 
**top_messages** | [**List[GetStorage200ResponseTopMessagesInner]**](GetStorage200ResponseTopMessagesInner.md) |  | [optional] 
**generated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.get_storage200_response import GetStorage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorage200Response from a JSON string
get_storage200_response_instance = GetStorage200Response.from_json(json)
# print the JSON string representation of the object
print(GetStorage200Response.to_json())

# convert the object into a dict
get_storage200_response_dict = get_storage200_response_instance.to_dict()
# create an instance of GetStorage200Response from a dict
get_storage200_response_from_dict = GetStorage200Response.from_dict(get_storage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


