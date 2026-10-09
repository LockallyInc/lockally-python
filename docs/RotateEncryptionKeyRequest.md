# RotateEncryptionKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_email** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**kdf_params** | **object** |  | [optional] 

## Example

```python
from lockally.models.rotate_encryption_key_request import RotateEncryptionKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RotateEncryptionKeyRequest from a JSON string
rotate_encryption_key_request_instance = RotateEncryptionKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RotateEncryptionKeyRequest.to_json())

# convert the object into a dict
rotate_encryption_key_request_dict = rotate_encryption_key_request_instance.to_dict()
# create an instance of RotateEncryptionKeyRequest from a dict
rotate_encryption_key_request_from_dict = RotateEncryptionKeyRequest.from_dict(rotate_encryption_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


