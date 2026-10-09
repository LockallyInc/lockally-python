# V1ApiKeysPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**prefix** | **str** | 8-char public prefix; safe to store and display. | 
**scopes** | **List[str]** |  | 
**label** | **str** |  | 
**last_used_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**secret** | **str** | The full &#x60;lk_live_&lt;prefix&gt;_&lt;secret&gt;&#x60; token. Shown ONCE. | 

## Example

```python
from lockally.models.v1_api_keys_post201_response import V1ApiKeysPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ApiKeysPost201Response from a JSON string
v1_api_keys_post201_response_instance = V1ApiKeysPost201Response.from_json(json)
# print the JSON string representation of the object
print(V1ApiKeysPost201Response.to_json())

# convert the object into a dict
v1_api_keys_post201_response_dict = v1_api_keys_post201_response_instance.to_dict()
# create an instance of V1ApiKeysPost201Response from a dict
v1_api_keys_post201_response_from_dict = V1ApiKeysPost201Response.from_dict(v1_api_keys_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


