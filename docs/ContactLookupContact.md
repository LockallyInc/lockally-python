# ContactLookupContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**contact_type** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from lockally.models.contact_lookup_contact import ContactLookupContact

# TODO update the JSON string below
json = "{}"
# create an instance of ContactLookupContact from a JSON string
contact_lookup_contact_instance = ContactLookupContact.from_json(json)
# print the JSON string representation of the object
print(ContactLookupContact.to_json())

# convert the object into a dict
contact_lookup_contact_dict = contact_lookup_contact_instance.to_dict()
# create an instance of ContactLookupContact from a dict
contact_lookup_contact_from_dict = ContactLookupContact.from_dict(contact_lookup_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


