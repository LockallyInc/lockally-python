# GetEncryptionKey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**email** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**encrypted_private_key** | **str** |  | [optional] 
**kdf_params** | **object** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**rotated_at** | **datetime** |  | [optional] 
**has_recovery** | **bool** |  | [optional] 
**recovery_set_at** | **datetime** |  | [optional] 
**recovery_blob** | **str** |  | [optional] 

## Example

```python
from lockally.models.get_encryption_key200_response import GetEncryptionKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncryptionKey200Response from a JSON string
get_encryption_key200_response_instance = GetEncryptionKey200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncryptionKey200Response.to_json())

# convert the object into a dict
get_encryption_key200_response_dict = get_encryption_key200_response_instance.to_dict()
# create an instance of GetEncryptionKey200Response from a dict
get_encryption_key200_response_from_dict = GetEncryptionKey200Response.from_dict(get_encryption_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


