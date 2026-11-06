# BulkUpsertExternalContactsRequestContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** | Defaults to the email address when empty. | [optional] 
**phone** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**contact_type** | **str** |  | [optional] [default to 'external']
**department** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'active']
**external_id** | **str** |  | 

## Example

```python
from lockally.models.bulk_upsert_external_contacts_request_contacts_inner import BulkUpsertExternalContactsRequestContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertExternalContactsRequestContactsInner from a JSON string
bulk_upsert_external_contacts_request_contacts_inner_instance = BulkUpsertExternalContactsRequestContactsInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertExternalContactsRequestContactsInner.to_json())

# convert the object into a dict
bulk_upsert_external_contacts_request_contacts_inner_dict = bulk_upsert_external_contacts_request_contacts_inner_instance.to_dict()
# create an instance of BulkUpsertExternalContactsRequestContactsInner from a dict
bulk_upsert_external_contacts_request_contacts_inner_from_dict = BulkUpsertExternalContactsRequestContactsInner.from_dict(bulk_upsert_external_contacts_request_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


