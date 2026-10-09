# V1SendPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **List[str]** |  | 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** | Plain-text body. Required if &#x60;html&#x60; is absent. | [optional] 
**html** | **str** | HTML body. Required if &#x60;text&#x60; is absent. | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**reply_to** | **str** | Where replies go. REQUIRED when &#x60;from&#x60; has no mailbox behind it, since a reply there would be delivered nowhere. A &#x60;Reply-To&#x60; entry in &#x60;headers&#x60; satisfies the same rule. The named form &#x60;Acme Support &lt;a@b.com&gt;&#x60; is also accepted. | [optional] 
**reply_to_name** | **str** | Display name shown on &#x60;Reply-To&#x60;, e.g. &#x60;Acme Support&#x60;. Ignored without &#x60;reply_to&#x60;. Encoded and quoted for you, so accents, commas and quotes are all safe. | [optional] 
**unsubscribe** | **bool** | Mark as opt-in/broadcast: skips suppressed recipients and adds a managed one-click List-Unsubscribe header. | [optional] 
**template_id** | **UUID** | Render subject/text/html from a stored template (GET /v1/templates). Mutually exclusive with inline subject/text/html. | [optional] 
**variables** | **Dict[str, str]** | Values substituted into the template&#39;s {{variable}} placeholders. | [optional] 
**send_at** | **datetime** | Schedule delivery for a future RFC3339 time (≤ 30 days out). Omit or past &#x3D; send now. Cancel with DELETE /v1/messages/{id} while scheduled. | [optional] 
**attachments** | [**List[V1SendPostRequestAttachmentsInner]**](V1SendPostRequestAttachmentsInner.md) |  | [optional] 

## Example

```python
from lockally.models.v1_send_post_request import V1SendPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendPostRequest from a JSON string
v1_send_post_request_instance = V1SendPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SendPostRequest.to_json())

# convert the object into a dict
v1_send_post_request_dict = v1_send_post_request_instance.to_dict()
# create an instance of V1SendPostRequest from a dict
v1_send_post_request_from_dict = V1SendPostRequest.from_dict(v1_send_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


