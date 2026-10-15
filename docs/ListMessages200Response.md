# ListMessages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Message]**](Message.md) |  | 
**next_cursor** | **str** | Pass as &#x60;cursor&#x60; to fetch the next page. Absent on the final page. | [optional] 

## Example

```python
from lockally.models.list_messages200_response import ListMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessages200Response from a JSON string
list_messages200_response_instance = ListMessages200Response.from_json(json)
# print the JSON string representation of the object
print(ListMessages200Response.to_json())

# convert the object into a dict
list_messages200_response_dict = list_messages200_response_instance.to_dict()
# create an instance of ListMessages200Response from a dict
list_messages200_response_from_dict = ListMessages200Response.from_dict(list_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


