# ContactLookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**known** | **bool** |  | 
**internal** | **bool** | True when the address is one of the tenant&#39;s own mailboxes. | 
**contact** | [**ContactLookupContact**](ContactLookupContact.md) |  | [optional] 
**history** | [**ContactLookupHistory**](ContactLookupHistory.md) |  | [optional] 

## Example

```python
from lockally.models.contact_lookup import ContactLookup

# TODO update the JSON string below
json = "{}"
# create an instance of ContactLookup from a JSON string
contact_lookup_instance = ContactLookup.from_json(json)
# print the JSON string representation of the object
print(ContactLookup.to_json())

# convert the object into a dict
contact_lookup_dict = contact_lookup_instance.to_dict()
# create an instance of ContactLookup from a dict
contact_lookup_from_dict = ContactLookup.from_dict(contact_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


