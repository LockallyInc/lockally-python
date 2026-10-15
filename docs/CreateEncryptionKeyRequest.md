# CreateEncryptionKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_email** | **str** |  | 
**public_key** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**kdf_params** | **object** |  | [optional] 

## Example

```python
from lockally.models.create_encryption_key_request import CreateEncryptionKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEncryptionKeyRequest from a JSON string
create_encryption_key_request_instance = CreateEncryptionKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEncryptionKeyRequest.to_json())

# convert the object into a dict
create_encryption_key_request_dict = create_encryption_key_request_instance.to_dict()
# create an instance of CreateEncryptionKeyRequest from a dict
create_encryption_key_request_from_dict = CreateEncryptionKeyRequest.from_dict(create_encryption_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


