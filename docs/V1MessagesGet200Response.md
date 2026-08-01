# V1MessagesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Message]**](Message.md) |  | 
**next_cursor** | **str** | Pass as &#x60;cursor&#x60; to fetch the next page. Absent on the final page. | [optional] 

## Example

```python
from lockally.models.v1_messages_get200_response import V1MessagesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1MessagesGet200Response from a JSON string
v1_messages_get200_response_instance = V1MessagesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1MessagesGet200Response.to_json())

# convert the object into a dict
v1_messages_get200_response_dict = v1_messages_get200_response_instance.to_dict()
# create an instance of V1MessagesGet200Response from a dict
v1_messages_get200_response_from_dict = V1MessagesGet200Response.from_dict(v1_messages_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


