# ListSharedMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SharedMember]**](SharedMember.md) |  | 

## Example

```python
from lockally.models.list_shared_members200_response import ListSharedMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSharedMembers200Response from a JSON string
list_shared_members200_response_instance = ListSharedMembers200Response.from_json(json)
# print the JSON string representation of the object
print(ListSharedMembers200Response.to_json())

# convert the object into a dict
list_shared_members200_response_dict = list_shared_members200_response_instance.to_dict()
# create an instance of ListSharedMembers200Response from a dict
list_shared_members200_response_from_dict = ListSharedMembers200Response.from_dict(list_shared_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


