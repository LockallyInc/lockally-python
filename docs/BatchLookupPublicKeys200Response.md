# BatchLookupPublicKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BatchLookupPublicKeys200ResponseDataInner]**](BatchLookupPublicKeys200ResponseDataInner.md) |  | [optional] 

## Example

```python
from lockally.models.batch_lookup_public_keys200_response import BatchLookupPublicKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLookupPublicKeys200Response from a JSON string
batch_lookup_public_keys200_response_instance = BatchLookupPublicKeys200Response.from_json(json)
# print the JSON string representation of the object
print(BatchLookupPublicKeys200Response.to_json())

# convert the object into a dict
batch_lookup_public_keys200_response_dict = batch_lookup_public_keys200_response_instance.to_dict()
# create an instance of BatchLookupPublicKeys200Response from a dict
batch_lookup_public_keys200_response_from_dict = BatchLookupPublicKeys200Response.from_dict(batch_lookup_public_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


