# V1ApiKeysPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Free-text identifier shown in the dashboard. | 
**scopes** | **List[str]** | Allowed scopes on this key. | 
**test** | **bool** | Issue a test key (&#x60;lk_test_&#x60; prefix). A test key accepts sends, records them and fires a simulated delivery webhook without sending mail, and counts against no limit or allowance.  | [optional] [default to False]

## Example

```python
from lockally.models.v1_api_keys_post_request import V1ApiKeysPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ApiKeysPostRequest from a JSON string
v1_api_keys_post_request_instance = V1ApiKeysPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ApiKeysPostRequest.to_json())

# convert the object into a dict
v1_api_keys_post_request_dict = v1_api_keys_post_request_instance.to_dict()
# create an instance of V1ApiKeysPostRequest from a dict
v1_api_keys_post_request_from_dict = V1ApiKeysPostRequest.from_dict(v1_api_keys_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


