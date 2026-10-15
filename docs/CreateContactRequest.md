# CreateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**contact_type** | **str** |  | [optional] [default to 'external']
**department** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from lockally.models.create_contact_request import CreateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactRequest from a JSON string
create_contact_request_instance = CreateContactRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactRequest.to_json())

# convert the object into a dict
create_contact_request_dict = create_contact_request_instance.to_dict()
# create an instance of CreateContactRequest from a dict
create_contact_request_from_dict = CreateContactRequest.from_dict(create_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


