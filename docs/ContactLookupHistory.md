# ContactLookupHistory

Correspondence history, limited to the mailboxes this key is granted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_count** | **int** |  | [optional] 
**first_seen** | **datetime** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.contact_lookup_history import ContactLookupHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ContactLookupHistory from a JSON string
contact_lookup_history_instance = ContactLookupHistory.from_json(json)
# print the JSON string representation of the object
print(ContactLookupHistory.to_json())

# convert the object into a dict
contact_lookup_history_dict = contact_lookup_history_instance.to_dict()
# create an instance of ContactLookupHistory from a dict
contact_lookup_history_from_dict = ContactLookupHistory.from_dict(contact_lookup_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


