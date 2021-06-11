from fastapi import FastAPI


def custom_openapi_doc(api: FastAPI):
    openapi_schema = api.openapi()

    default_required = ["message"]
    default_properties = {
        "message": {
            "title": "Message",
            "type": "string"
        }
    }

    openapi_schema["components"]["schemas"]["ValidationError"]["required"] = default_required
    openapi_schema["components"]["schemas"]["ValidationError"]["properties"] = default_properties

    openapi_schema["components"]["schemas"]["HTTPValidationError"]["required"] = default_required
    openapi_schema["components"]["schemas"]["HTTPValidationError"]["properties"] = default_properties

    api.openapi_schema = openapi_schema
    return api.openapi_schema
