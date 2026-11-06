# BulkUpsertExternalContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | 
**updated** | **int** |  | 
**failed** | **int** |  | 
**results** | [**List[BulkUpsertExternalContacts200ResponseResultsInner]**](BulkUpsertExternalContacts200ResponseResultsInner.md) |  | 

## Example

```python
from lockally.models.bulk_upsert_external_contacts200_response import BulkUpsertExternalContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsertExternalContacts200Response from a JSON string
bulk_upsert_external_contacts200_response_instance = BulkUpsertExternalContacts200Response.from_json(json)
# print the JSON string representation of the object
print(BulkUpsertExternalContacts200Response.to_json())

# convert the object into a dict
bulk_upsert_external_contacts200_response_dict = bulk_upsert_external_contacts200_response_instance.to_dict()
# create an instance of BulkUpsertExternalContacts200Response from a dict
bulk_upsert_external_contacts200_response_from_dict = BulkUpsertExternalContacts200Response.from_dict(bulk_upsert_external_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


