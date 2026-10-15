# BatchLookupPublicKeys200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**key_id** | **UUID** |  | [optional] 

## Example

```python
from lockally.models.batch_lookup_public_keys200_response_data_inner import BatchLookupPublicKeys200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLookupPublicKeys200ResponseDataInner from a JSON string
batch_lookup_public_keys200_response_data_inner_instance = BatchLookupPublicKeys200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(BatchLookupPublicKeys200ResponseDataInner.to_json())

# convert the object into a dict
batch_lookup_public_keys200_response_data_inner_dict = batch_lookup_public_keys200_response_data_inner_instance.to_dict()
# create an instance of BatchLookupPublicKeys200ResponseDataInner from a dict
batch_lookup_public_keys200_response_data_inner_from_dict = BatchLookupPublicKeys200ResponseDataInner.from_dict(batch_lookup_public_keys200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


