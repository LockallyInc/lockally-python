# CreateApiKey201Response


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
**test** | **bool** | True for an lk_test_* key: the whole request path runs but a send never reaches the mail server and nothing counts against the account. | [optional] 
**expires_at** | **datetime** | When the key stops authenticating. Null means it does not expire, which is how every key behaved before expiry existed. Enforced at authentication, so the key fails the first request after this moment rather than whenever a sweep runs.  | [optional] 
**rotated_to** | **UUID** | The successor issued by &#x60;POST /v1/api-keys/{id}/rotate&#x60;. Set on the PREDECESSOR, so you can see which key replaced this one while both still work through the overlap window.  | [optional] 
**secret** | **str** | The full &#x60;lk_live_&lt;prefix&gt;_&lt;secret&gt;&#x60; token. Shown ONCE. | 

## Example

```python
from lockally.models.create_api_key201_response import CreateApiKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKey201Response from a JSON string
create_api_key201_response_instance = CreateApiKey201Response.from_json(json)
# print the JSON string representation of the object
print(CreateApiKey201Response.to_json())

# convert the object into a dict
create_api_key201_response_dict = create_api_key201_response_instance.to_dict()
# create an instance of CreateApiKey201Response from a dict
create_api_key201_response_from_dict = CreateApiKey201Response.from_dict(create_api_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


