# UpdateContactListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from lockally.models.update_contact_list_request import UpdateContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactListRequest from a JSON string
update_contact_list_request_instance = UpdateContactListRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactListRequest.to_json())

# convert the object into a dict
update_contact_list_request_dict = update_contact_list_request_instance.to_dict()
# create an instance of UpdateContactListRequest from a dict
update_contact_list_request_from_dict = UpdateContactListRequest.from_dict(update_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


