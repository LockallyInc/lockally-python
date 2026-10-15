# AddSharedMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_email** | **str** |  | 
**role** | **str** |  | [optional] [default to 'member']

## Example

```python
from lockally.models.add_shared_member_request import AddSharedMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSharedMemberRequest from a JSON string
add_shared_member_request_instance = AddSharedMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddSharedMemberRequest.to_json())

# convert the object into a dict
add_shared_member_request_dict = add_shared_member_request_instance.to_dict()
# create an instance of AddSharedMemberRequest from a dict
add_shared_member_request_from_dict = AddSharedMemberRequest.from_dict(add_shared_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


