# BulkUpsertExternalContacts200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**external_id** | **str** |  | 
**status** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from lockally.models.bulk_upsert_external_contacts200_response_results_inner import BulkUpsertExternalContacts200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertExternalContacts200ResponseResultsInner from a JSON string
bulk_upsert_external_contacts200_response_results_inner_instance = BulkUpsertExternalContacts200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertExternalContacts200ResponseResultsInner.to_json())

# convert the object into a dict
bulk_upsert_external_contacts200_response_results_inner_dict = bulk_upsert_external_contacts200_response_results_inner_instance.to_dict()
# create an instance of BulkUpsertExternalContacts200ResponseResultsInner from a dict
bulk_upsert_external_contacts200_response_results_inner_from_dict = BulkUpsertExternalContacts200ResponseResultsInner.from_dict(bulk_upsert_external_contacts200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


