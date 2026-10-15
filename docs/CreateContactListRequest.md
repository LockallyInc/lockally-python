# CreateContactListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] [default to 'company_wide']

## Example

```python
from lockally.models.create_contact_list_request import CreateContactListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactListRequest from a JSON string
create_contact_list_request_instance = CreateContactListRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactListRequest.to_json())

# convert the object into a dict
create_contact_list_request_dict = create_contact_list_request_instance.to_dict()
# create an instance of CreateContactListRequest from a dict
create_contact_list_request_from_dict = CreateContactListRequest.from_dict(create_contact_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


