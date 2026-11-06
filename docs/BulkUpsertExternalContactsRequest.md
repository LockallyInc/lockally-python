# BulkUpsertExternalContactsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[BulkUpsertExternalContactsRequestContactsInner]**](BulkUpsertExternalContactsRequestContactsInner.md) |  | 

## Example

```python
from lockally.models.bulk_upsert_external_contacts_request import BulkUpsertExternalContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertExternalContactsRequest from a JSON string
bulk_upsert_external_contacts_request_instance = BulkUpsertExternalContactsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertExternalContactsRequest.to_json())

# convert the object into a dict
bulk_upsert_external_contacts_request_dict = bulk_upsert_external_contacts_request_instance.to_dict()
# create an instance of BulkUpsertExternalContactsRequest from a dict
bulk_upsert_external_contacts_request_from_dict = BulkUpsertExternalContactsRequest.from_dict(bulk_upsert_external_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


