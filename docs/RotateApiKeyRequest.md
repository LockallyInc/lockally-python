# RotateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_seconds** | **int** | How long the old key keeps working. Defaults to 24 hours, which is long enough to cut over without a scramble. Capped at 30 days, because beyond that \&quot;rotated\&quot; stops meaning anything.  | [optional] [default to 86400]

## Example

```python
from lockally.models.rotate_api_key_request import RotateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RotateApiKeyRequest from a JSON string
rotate_api_key_request_instance = RotateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RotateApiKeyRequest.to_json())

# convert the object into a dict
rotate_api_key_request_dict = rotate_api_key_request_instance.to_dict()
# create an instance of RotateApiKeyRequest from a dict
rotate_api_key_request_from_dict = RotateApiKeyRequest.from_dict(rotate_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


