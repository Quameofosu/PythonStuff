print("Hello World")
print("========================")
print(True and True)
print("-------------Brilla Questions Game-------------\nDeveloped by Manuel Ofosu Copyright@12/12/2022")
print('-----------------------------------------------')
print('-----------------------------------------------')
print("We Wish You GodSpeed!")


{
  "openapi": "3.0.1",
  "info": {
    "title": "Disbursements",
    "description": "Partner Gateway API document",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://sandbox.momodeveloper.mtn.com/disbursement"
    }
  ],
  "paths": {
    "/token/": {
      "post": {
        "summary": "/token - POST",
        "description": "This operation is used to create an access token which can then be used to authorize and authenticate towards the other end-points of the API.",
        "operationId": "token-POST",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Basic authentication header containing API user ID and API key. Should be sent in as B64 encoded.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TokenPost200ApplicationJsonResponse"
                },
                "example": {
                  "access_token": "string",
                  "token_type": "string",
                  "expires_in": 0
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TokenPost401ApplicationJsonResponse"
                },
                "example": {
                  "error": "string"
                }
              }
            }
          },
          "500": {
            "description": "Error",
            "content": {
              "application/json": { }
            }
          }
        }
      }
    },
    "/v1_0/account/balance": {
      "get": {
        "summary": "/v1_0/account/balance - GET",
        "description": "Get the balance of the account.",
        "operationId": "get-v1_0-account-balance",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Ok",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Balance"
                },
                "example": {
                  "availableBalance": "string",
                  "currency": "string"
                }
              },
              "Incorrect target environment": {
                "schema": {
                  "$ref": "#/components/schemas/Balance"
                }
              }
            }
          },
          "400": {
            "description": "Bad request, e.g. invalid data was sent in the request.",
            "content": {
              "application/json": { },
              "Incorrect target environment": { }
            }
          },
          "500": {
            "description": "Internal error. The returned response contains details.",
            "content": {
              "Incorrect target environment": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "NOT_ALLOWED_TARGET_ENVIRONMENT",
                  "message": "Access to target environment is forbidden."
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "PAYEE_NOT_FOUND",
                  "message": "string"
                }
              }
            }
          }
        }
      }
    },
    "/v1_0/accountholder/{accountHolderIdType}/{accountHolderId}/active": {
      "get": {
        "summary": "/v1_0/accountholder/{accountHolderIdType}/{accountHolderId}/active - GET",
        "description": "Operation is used  to check if an account holder is registered and active in the system.",
        "operationId": "get-v1_0-accountholder-accountholderidtype-accountholderid-active",
        "parameters": [
          {
            "name": "accountHolderId",
            "in": "path",
            "description": "The party number. Validated according to the party id type. <br> MSISDN - Mobile Number validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format. Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "accountHolderIdType",
            "in": "path",
            "description": "Specifies the type of the party id. Allowed values [msisdn, email, party_code].",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Ok. True if account holder is registered and active, false if the account holder is not active or not found found",
            "content": {
              "Incorrect target environment": { }
            }
          },
          "400": {
            "description": "Bad request, e.g. invalid data was sent in the request.",
            "content": {
              "Incorrect target environment": { }
            }
          },
          "500": {
            "description": "Internal error. The returned response contains details.",
            "content": {
              "Incorrect target environment": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "NOT_ALLOWED_TARGET_ENVIRONMENT",
                  "message": "Access to target environment is forbidden."
                }
              }
            }
          }
        }
      }
    },
    "/v1_0/transfer": {
      "post": {
        "summary": "/transfer - POST",
        "description": "Transfer operation is used to transfer an amount from the own account to a payee account.<br> Status of the transaction can validated by using the GET /transfer/\\{referenceId\\}",
        "operationId": "transfer-POST",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Callback-Url",
            "in": "header",
            "description": "URL to the server where the callback should be sent.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Reference-Id",
            "in": "header",
            "description": "Format - UUID. Recource ID of the created request to pay transaction. This ID is used, for example validating the status of the request. ‘Universal Unique ID’ for the transaction generated using UUID version 4.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Transfer"
              },
              "example": {
                "amount": "string",
                "currency": "string",
                "externalId": "string",
                "payee": {
                  "partyIdType": "MSISDN",
                  "partyId": "string"
                },
                "payerMessage": "string",
                "payeeNote": "string"
              }
            }
          }
        },
        "responses": {
          "202": {
            "description": "Accepted",
            "content": {
              "application/json": { },
              "ReferenceId already in use": { },
              "Incorrect currency for target environment": { }
            }
          },
          "400": {
            "description": "Bad request, e.g. invalid data was sent in the request.",
            "content": {
              "application/json": { },
              "ReferenceId already in use": { },
              "Incorrect currency for target environment": { }
            }
          },
          "409": {
            "description": "Conflict, duplicated reference id",
            "content": {
              "ReferenceId already in use": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "RESOURCE_ALREADY_EXIST",
                  "message": "Duplicated reference id. Creation of resource failed."
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "PAYEE_NOT_FOUND",
                  "message": "string"
                }
              },
              "Incorrect currency for target environment": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "examples": {
                  "default": {
                    "value": null
                  }
                }
              }
            }
          },
          "500": {
            "description": "Internal Error.",
            "content": {
              "Incorrect currency for target environment": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "INVALID_CURRENCY",
                  "message": "Currency not supported."
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "PAYEE_NOT_FOUND",
                  "message": "string"
                }
              },
              "ReferenceId already in use": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "examples": {
                  "default": {
                    "value": null
                  }
                }
              }
            }
          }
        }
      }
    },
    "/v1_0/transfer/{referenceId}": {
      "get": {
        "summary": "/transfer/{referenceId} - GET",
        "description": "This operation is used to get the status of a transfer. X-Reference-Id that was passed in the post is used as reference to the request.",
        "operationId": "transfer-referenceId-GET",
        "parameters": [
          {
            "name": "referenceId",
            "in": "path",
            "description": "UUID of transaction to get result. Reference id  used when creating the request to pay.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK. Note that a failed transfer will be returned with this status too. The 'status' of the TransferResult can be used to determine the outcome of the request. The 'reason' field can be used to retrieve a cause in case of failure.",
            "content": {
              "Successful transfer": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                },
                "example": {
                  "amount": 100,
                  "currency": "UGX",
                  "financialTransactionId": 363440463,
                  "externalId": 83453,
                  "payee": {
                    "partyIdType": "MSISDN",
                    "partyId": 4609274685
                  },
                  "status": "SUCCESSFUL"
                }
              },
              "Payer limit breached": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                },
                "example": {
                  "amount": 100,
                  "currency": "UGX",
                  "externalId": 83453,
                  "payee": {
                    "partyIdType": "MSISDN",
                    "partyId": 4609274685
                  },
                  "status": "FAILED",
                  "reason": {
                    "code": "PAYER_LIMIT_REACHED",
                    "message": "The payer's limit has been breached."
                  }
                }
              },
              "API user insufficient balance": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                },
                "example": {
                  "amount": 100,
                  "currency": "UGX",
                  "externalId": 83453,
                  "payee": {
                    "partyIdType": "MSISDN",
                    "partyId": 4609274685
                  },
                  "status": "FAILED",
                  "reason": {
                    "code": "NOT_ENOUGH_FUNDS",
                    "message": "The payer does not have enough funds."
                  }
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                },
                "example": {
                  "amount": "string",
                  "currency": "string",
                  "financialTransactionId": "string",
                  "externalId": "string",
                  "payee": {
                    "partyIdType": "MSISDN",
                    "partyId": "string"
                  },
                  "payerMessage": "string",
                  "payeeNote": "string",
                  "status": "PENDING",
                  "reason": {
                    "code": "PAYEE_NOT_FOUND",
                    "message": "string"
                  }
                }
              },
              "Transfer not found": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                }
              },
              "Unspecified internal error": {
                "schema": {
                  "$ref": "#/components/schemas/TransferResult"
                }
              }
            }
          },
          "400": {
            "description": "Bad request, e.g. an incorrectly formatted reference id was provided.",
            "content": {
              "Successful transfer": { },
              "Payer limit breached": { },
              "API user insufficient balance": { },
              "application/json": { },
              "Transfer not found": { },
              "Unspecified internal error": { }
            }
          },
          "404": {
            "description": "Resource not found.",
            "content": {
              "Transfer not found": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "RESOURCE_NOT_FOUND",
                  "message": "Requested resource was not found."
                }
              },
              "Successful transfer": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "Payer limit breached": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "API user insufficient balance": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "PAYEE_NOT_FOUND",
                  "message": "string"
                }
              },
              "Unspecified internal error": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              }
            }
          },
          "500": {
            "description": "Internal Error. Note that if the retreieved transfer has failed, it will not cause this status to be returned. This status is only returned if the GET request itself fails.",
            "content": {
              "Unspecified internal error": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "INTERNAL_PROCESSING_ERROR",
                  "message": "An internal error occurred while processing."
                }
              },
              "Successful transfer": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "Payer limit breached": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "API user insufficient balance": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                },
                "example": {
                  "code": "PAYEE_NOT_FOUND",
                  "message": "string"
                }
              },
              "Transfer not found": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorReason"
                }
              }
            }
          }
        }
      }
    },
    "/v1_0/accountholder/msisdn/{accountHolderMSISDN}/basicuserinfo": {
      "get": {
        "summary": "/v1_0/accountholder/msisdn/{accountHolderMSISDN}/basicuserinfo - GET",
        "description": "This operation returns personal information of the account holder. The operation does not need any consent by the account holder.",
        "operationId": "basicuserInfo-GET",
        "parameters": [
          {
            "name": "accountHolderMSISDN",
            "in": "path",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BasicUserInfoJsonResponse"
                },
                "example": {
                  "given_name": "string",
                  "family_name": "string",
                  "birthdate": "string",
                  "locale": "string",
                  "gender": "string",
                  "status": "string"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TokenPost401ApplicationJsonResponse"
                },
                "example": {
                  "error": "string"
                }
              }
            }
          },
          "500": {
            "description": "Error",
            "content": {
              "application/json": { }
            }
          }
        }
      }
    },
    "/v1_0/bc-authorize": {
      "post": {
        "summary": "/bc-authorize - POST",
        "description": "This operation is used to claim a consent by the account holder for the requested scopes.",
        "operationId": "bc-authorize-POST",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Basic authentication header containing API user ID and API key. Should be sent in as B64 encoded.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Callback-Url",
            "in": "header",
            "description": "URL to the server where the callback should be sent.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "properties": {
                  "scope": {
                    "type": "string"
                  },
                  "login_hint": {
                    "type": "string"
                  },
                  "access_type": {
                    "enum": [
                      "online",
                      "offline"
                    ],
                    "type": "string"
                  },
                  "consent_valid_in": {
                    "type": "integer"
                  },
                  "client_notification_token": {
                    "type": "string"
                  },
                  "scope_instruction": {
                    "type": "string"
                  }
                }
              },
              "example": "login_hint=ID:{msisdn}/MSISDN&scope={scope}&access_type={online/offline}"
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/bcauthorizeResponse"
                },
                "example": {
                  "auth_req_id": "string",
                  "interval": 0,
                  "expires_in": 0
                }
              }
            }
          }
        }
      }
    },
    "/oauth2/token/": {
      "post": {
        "summary": "/oauth2/token/ - POST",
        "description": "This operation is used to claim a consent by the account holder for the requested scopes.",
        "operationId": "oauth2-token-POST",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Basic authentication header containing API user ID and API key. Should be sent in as B64 encoded.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "properties": {
                  "grant_type": {
                    "type": "string"
                  },
                  "auth_req_id": {
                    "type": "string"
                  },
                  "refresh_token": {
                    "type": "string"
                  }
                }
              },
              "example": "grant_type=urn:openid:params:grant-type:ciba&auth_req_id={auth_req_id}"
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/oauth2TokenResponse"
                },
                "example": {
                  "access_token": "string",
                  "token_type": "string",
                  "expires_in": 0,
                  "scope": "string",
                  "refresh_token": "string",
                  "refresh_token_expired_in": 0
                }
              }
            }
          }
        }
      }
    },
    "/oauth2/v1_0/userinfo": {
      "get": {
        "summary": "/oauth2/v1_0/userinfo/ - GET",
        "description": "This operation is used to claim a consent by the account holder for the requested scopes.",
        "operationId": "userinfo-token-POST",
        "parameters": [
          {
            "name": "Authorization",
            "in": "header",
            "description": "Bearer Token. Replace with a valid oauth2 token received from oauth2 token endpoint in Partner Gateway.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/consentkycResponse"
                },
                "example": {
                  "sub": "string",
                  "name": "string",
                  "given_name": "string",
                  "family_name": "string",
                  "middle_name": "string",
                  "email": "string",
                  "email_verified": true,
                  "gender": "string",
                  "locale": "string",
                  "phone_number": "string",
                  "phone_number_verified": true,
                  "address": "string",
                  "updated_at": 0,
                  "status": "string",
                  "birthdate": "string",
                  "credit_score": "string",
                  "active": true,
                  "country_of_birth": "string",
                  "region_of_birth": "string",
                  "city_of_birth": "string",
                  "occupation": "string",
                  "employer_name": "string",
                  "identification_type": "string",
                  "identification_value": "string"
                }
              }
            }
          }
        }
      }
    },
    "/v1_0/requesttopay/{referenceId}/deliverynotification": {
      "post": {
        "summary": "/requesttopay/{referenceId}/deliverynotification - POST",
        "description": "This operation is used to send additional Notification to an End User.",
        "operationId": "requesttopay-referenceId-deliverynotification-POST",
        "parameters": [
          {
            "name": "referenceId",
            "in": "path",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "notificationMessage",
            "in": "header",
            "description": "The message to send in the delivery notification. Max              length 160.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Language",
            "in": "header",
            "description": "An ISO 639-1 or ISO 639-3 language code. The language is used to select the best matching notification template when sending the delivery notification to the end-user. A default value is used if not specified.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Authorization",
            "in": "header",
            "description": "Authorization header used for Basic authentication and oauth. Format of the header parameter follows the standard for Basic and Bearer. Oauth uses Bearer authentication type where the credential is the received access token.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-Target-Environment",
            "in": "header",
            "description": "The identifier of the EWP system where the transaction shall be processed. This parameter is used to route the request to the EWP system that will initiate the transaction.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/deliverynotification"
              },
              "example": {
                "notificationMessage": "string"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK. Notification successfully enqueued.",
            "content": {
              "application/json": { }
            }
          },
          "400": {
            "description": "Bad request. Invalid data was sent in the request.",
            "content": {
              "application/json": { }
            }
          },
          "404": {
            "description": "Resource not found. The reference ID does not exist, or the calling user is not the owner of the financial transaction.",
            "content": {
              "application/json": { }
            }
          },
          "409": {
            "description": "Conflict. The transaction is not successfully completed.",
            "content": {
              "application/json": { }
            }
          },
          "410": {
            "description": "Gone. The delivery notification opportunity has expired.",
            "content": {
              "application/json": { }
            }
          },
          "429": {
            "description": "Too many requests. Too many attempts for the same ID has been made recently. This will only occur if a successful attempt has previously been performed.",
            "content": {
              "application/json": { }
            }
          },
          "500": {
            "description": "Internal server error. An unexpected error occurred.",
            "content": {
              "application/json": { }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "bcauthorize": {
        "type": "object",
        "properties": {
          "scope": {
            "type": "string",
            "description": "Space separated list of scopes."
          },
          "login_hint": {
            "type": "string",
            "description": "The identity of the account holder."
          },
          "access_type": {
            "enum": [
              "online",
              "offline"
            ],
            "type": "string",
            "description": "Value either online, or offline."
          },
          "consent_valid_in": {
            "type": "integer",
            "description": "The validity time of the consent in secondsThis parameter can only be used together with access type offline."
          },
          "client_notification_token": {
            "type": "string",
            "description": "This token is required when the client is using Ping or Push mode."
          },
          "scope_instruction": {
            "type": "string",
            "description": "Base64 encoded Instrcution of the financial transaction."
          }
        }
      },
      "bcauthorizeResponse": {
        "type": "object",
        "properties": {
          "auth_req_id": {
            "type": "string",
            "description": "Authentication request ID as an UUID."
          },
          "interval": {
            "type": "number",
            "description": "Indicates how long time the client should wait between retries towards the endpoint /oauth2/token."
          },
          "expires_in": {
            "type": "number",
            "description": "Shows when the authentication request ID expires, in seconds."
          }
        }
      },
      "BasicUserInfoJsonResponse": {
        "type": "object",
        "properties": {
          "given_name": {
            "type": "string",
            "description": "Given name(s) or first name(s) of the End-User. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters."
          },
          "family_name": {
            "type": "string",
            "description": "Surname(s) or last name(s) of the End-User. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters."
          },
          "birthdate": {
            "type": "string",
            "description": "Account holder birth date."
          },
          "locale": {
            "type": "string",
            "description": "End-User's locale, represented as a  BCP47 [RFC5646] language tag. This is typically an  ISO 639-1 Alpha-2 [ISO639�|�1] language code in lowercase and an  ISO 3166-1 Alpha-2 [ISO3166�|�1] country code in uppercase, separated by a dash. For example,  en-US or  fr-CA. As a compatibility note, some implementations have used an underscore as the separator rather than a dash, for example,  en_US; Relying Parties may choose to accept this locale syntax as well."
          },
          "gender": {
            "type": "string",
            "description": "End-User's gender. Values defined by this specification are female and male. Other values may be used when neither of the defined values are applicable."
          },
          "status": {
            "type": "string",
            "description": "Accountholder status."
          }
        }
      },
      "TokenPost200ApplicationJsonResponse": {
        "type": "object",
        "properties": {
          "access_token": {
            "type": "string",
            "description": "A JWT token which can be used to authrize against the other API end-points. The format of the token follows the JWT standard format (see jwt.io for an example). This is the token that should be sent in in the Authorization header when calling the other API end-points."
          },
          "token_type": {
            "type": "string",
            "description": "The token type."
          },
          "expires_in": {
            "type": "integer",
            "description": "The validity time in seconds of the token."
          }
        }
      },
      "oauth2TokenRequest": {
        "type": "object",
        "properties": {
          "grant_type": {
            "type": "string",
            "description": "Value ca be either \"urn:openid:params:grant-type:ciba\" or refresh_token"
          },
          "auth_req_id": {
            "type": "string",
            "description": "Authentication request ID.Value is only mandatory if grant_type is \"urn:openid:params:grant-type:ciba\""
          },
          "refresh_token": {
            "type": "string",
            "description": "UUID.Refresh token retrieved from oauth2 token endpoint for consents with grant_type offline. This parameter is only valid if grant_type is refresh_token."
          }
        }
      },
      "oauth2TokenResponse": {
        "type": "object",
        "properties": {
          "access_token": {
            "type": "string",
            "description": "Oauth2 JWT access token.The generated token is valid 3600 seconds as default."
          },
          "token_type": {
            "type": "string",
            "description": "Value is Bearer"
          },
          "expires_in": {
            "type": "number",
            "description": "Shows when the authentication request ID expires, in seconds."
          },
          "scope": {
            "type": "string",
            "description": "List of scopes that belongs to the authentication request ID."
          },
          "refresh_token": {
            "type": "string",
            "description": "UUID of the refresh_token"
          },
          "refresh_token_expired_in": {
            "type": "integer",
            "description": "The time in seconds until the consent can no longer be refreshed. Based on the default value for consent validity, or the value set to parameter consent_valid_in sent in the bc-authorize request."
          }
        }
      },
      "consentkycResponse": {
        "type": "object",
        "properties": {
          "sub": {
            "type": "string",
            "description": "Subject - Identifier for the End-User at the Issuer."
          },
          "name": {
            "type": "string",
            "description": "End-User's full name in displayable form including all name parts."
          },
          "given_name": {
            "type": "string",
            "description": "Given name(s) or first name(s) of the End-User."
          },
          "family_name": {
            "type": "string",
            "description": "Surname(s) or last name(s) of the End-User."
          },
          "middle_name": {
            "type": "string",
            "description": "Middle name(s) of the End-User."
          },
          "email": {
            "type": "string",
            "description": "End-User's preferred e-mail address. Its value MUST conform to the  RFC 5322 [RFC5322] address specification syntax."
          },
          "email_verified": {
            "type": "boolean",
            "description": "The response value is True if the End-User's e-mail address has been verified;otherwise false."
          },
          "gender": {
            "type": "string",
            "description": "End-User's gender."
          },
          "locale": {
            "type": "string",
            "description": "Preffered language."
          },
          "phone_number": {
            "type": "string",
            "description": "End-User's preferred telephone number"
          },
          "phone_number_verified": {
            "type": "boolean",
            "description": "The response value is True if the End-User's phone number has been verified; otherwise false."
          },
          "address": {
            "type": "string",
            "description": "User Address"
          },
          "updated_at": {
            "type": "number",
            "description": "The time the End-User's information was last updated."
          },
          "status": {
            "type": "string",
            "description": "Account holder status."
          },
          "birthdate": {
            "type": "string",
            "description": "The birth date of the account holder."
          },
          "credit_score": {
            "type": "string",
            "description": "The credit score of the account holder."
          },
          "active": {
            "type": "boolean",
            "description": "The status of the account holder."
          },
          "country_of_birth": {
            "type": "string",
            "description": "Account holder country of birth."
          },
          "region_of_birth": {
            "type": "string",
            "description": "The birth region of the account holder."
          },
          "city_of_birth": {
            "type": "string",
            "description": "The city of birth for the account holder."
          },
          "occupation": {
            "type": "string",
            "description": "Occupation of the account holder."
          },
          "employer_name": {
            "type": "string",
            "description": "The name of the employer."
          },
          "identification_type": {
            "type": "string",
            "description": "Type of identification.The first non-expired identification is always chosen."
          },
          "identification_value": {
            "type": "string",
            "description": "The value of the identification."
          }
        }
      },
      "address": {
        "type": "object",
        "properties": {
          "formatted": {
            "type": "string",
            "description": "Full mailing address, formatted for display or use on a mailing label. This field may contain multiple lines, separated by newlines."
          },
          "street_address": {
            "type": "string",
            "description": "Full street address component, which may include house number, street name, Post Office Box, and multi-line extended street address information."
          },
          "locality": {
            "type": "string",
            "description": "City or locality component."
          },
          "region": {
            "type": "string",
            "description": "State, province, prefecture, or region component."
          },
          "postal_code": {
            "type": "string",
            "description": "Zip code or postal code component."
          },
          "country": {
            "type": "string",
            "description": "Country name component."
          }
        }
      },
      "TokenPost401ApplicationJsonResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "An error code."
          }
        }
      },
      "Balance": {
        "type": "object",
        "properties": {
          "availableBalance": {
            "type": "string",
            "description": "The available balance of the account"
          },
          "currency": {
            "type": "string",
            "description": "ISO4217 Currency"
          }
        },
        "description": "The available balance of the account"
      },
      "Party": {
        "type": "object",
        "properties": {
          "partyIdType": {
            "enum": [
              "MSISDN",
              "EMAIL",
              "PARTY_CODE"
            ],
            "type": "string"
          },
          "partyId": {
            "type": "string"
          }
        },
        "description": "Party identifies a account holder in the wallet platform. Party consists of two parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format. Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid"
      },
      "PreApproval": {
        "type": "object",
        "properties": {
          "payer": {
            "$ref": "#/components/schemas/Party"
          },
          "payerCurrency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "payerMessage": {
            "type": "string",
            "description": "The mesage that is shown to the approver."
          },
          "validityTime": {
            "type": "integer",
            "description": "The request validity time of the pre-approval"
          }
        }
      },
      "PreApprovalResult": {
        "type": "object",
        "properties": {
          "payer": {
            "$ref": "#/components/schemas/Party"
          },
          "payerCurrency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "payerMessage": {
            "type": "string",
            "description": "The mesage that is shown to the approver."
          },
          "validityTime": {
            "type": "integer",
            "description": "The request validity time of the pre-approval"
          },
          "status": {
            "enum": [
              "PENDING",
              "SUCCESSFUL",
              "FAILED"
            ],
            "type": "string"
          },
          "reason": {
            "$ref": "#/components/schemas/ErrorReason"
          }
        }
      },
      "RequestToPay": {
        "type": "object",
        "properties": {
          "amount": {
            "type": "string",
            "description": "Amount that will be debited from the payer account."
          },
          "currency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "externalId": {
            "type": "string",
            "description": "External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique."
          },
          "payer": {
            "$ref": "#/components/schemas/Party"
          },
          "payerMessage": {
            "type": "string",
            "description": "Message that will be written in the payer transaction history message field."
          },
          "payeeNote": {
            "type": "string",
            "description": "Message that will be written in the payee transaction history note field."
          }
        }
      },
      "RequestToPayResult": {
        "type": "object",
        "properties": {
          "amount": {
            "type": "string",
            "description": "Amount that will be debited from the payer account."
          },
          "currency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "financialTransactionId": {
            "type": "string",
            "description": "Financial transactionIdd from mobile money manager.<br> Used to connect to the specific financial transaction made in the account"
          },
          "externalId": {
            "type": "string",
            "description": "External id provided in the creation of the requestToPay transaction."
          },
          "payer": {
            "$ref": "#/components/schemas/Party"
          },
          "payerMessage": {
            "type": "string",
            "description": "Message that will be written in the payer transaction history message field."
          },
          "payeeNote": {
            "type": "string",
            "description": "Message that will be written in the payee transaction history note field."
          },
          "status": {
            "enum": [
              "PENDING",
              "SUCCESSFUL",
              "FAILED"
            ],
            "type": "string"
          },
          "reason": {
            "$ref": "#/components/schemas/ErrorReason"
          }
        }
      },
      "Transfer": {
        "type": "object",
        "properties": {
          "amount": {
            "type": "string",
            "description": "Amount that will be debited from the payer account."
          },
          "currency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "externalId": {
            "type": "string",
            "description": "External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique."
          },
          "payee": {
            "$ref": "#/components/schemas/Party"
          },
          "payerMessage": {
            "type": "string",
            "description": "Message that will be written in the payer transaction history message field."
          },
          "payeeNote": {
            "type": "string",
            "description": "Message that will be written in the payee transaction history note field."
          }
        }
      },
      "TransferResult": {
        "type": "object",
        "properties": {
          "amount": {
            "type": "string",
            "description": "Amount that will be debited from the payer account."
          },
          "currency": {
            "type": "string",
            "description": "ISO4217 Currency"
          },
          "financialTransactionId": {
            "type": "string",
            "description": "Financial transactionIdd from mobile money manager.<br> Used to connect to the specific financial transaction made in the account"
          },
          "externalId": {
            "type": "string",
            "description": "External id is used as a reference to the transaction. External id is used for reconciliation. The external id will be included in transaction history report. <br>External id is not required to be unique."
          },
          "payee": {
            "$ref": "#/components/schemas/Party"
          },
          "payerMessage": {
            "type": "string",
            "description": "Message that will be written in the payer transaction history message field."
          },
          "payeeNote": {
            "type": "string",
            "description": "Message that will be written in the payee transaction history note field."
          },
          "status": {
            "enum": [
              "PENDING",
              "SUCCESSFUL",
              "FAILED"
            ],
            "type": "string"
          },
          "reason": {
            "$ref": "#/components/schemas/ErrorReason"
          }
        }
      },
      "deliverynotification": {
        "type": "object",
        "properties": {
          "notificationMessage": {
            "type": "string"
          }
        }
      },
      "ErrorReason": {
        "type": "object",
        "properties": {
          "code": {
            "enum": [
              "PAYEE_NOT_FOUND",
              "PAYER_NOT_FOUND",
              "NOT_ALLOWED",
              "NOT_ALLOWED_TARGET_ENVIRONMENT",
              "INVALID_CALLBACK_URL_HOST",
              "INVALID_CURRENCY",
              "SERVICE_UNAVAILABLE",
              "INTERNAL_PROCESSING_ERROR",
              "NOT_ENOUGH_FUNDS",
              "PAYER_LIMIT_REACHED",
              "PAYEE_NOT_ALLOWED_TO_RECEIVE",
              "PAYMENT_NOT_APPROVED",
              "RESOURCE_NOT_FOUND",
              "APPROVAL_REJECTED",
              "EXPIRED",
              "TRANSACTION_CANCELED",
              "RESOURCE_ALREADY_EXIST"
            ],
            "type": "string"
          },
          "message": {
            "type": "string"
          }
        }
      },
      "BooleanResult": {
        "type": "object",
        "properties": {
          "result": {
            "type": "boolean"
          }
        }
      }
    },
    "securitySchemes": {
      "apiKeyHeader": {
        "type": "apiKey",
        "name": "Ocp-Apim-Subscription-Key",
        "in": "header"
      },
      "apiKeyQuery": {
        "type": "apiKey",
        "name": "subscription-key",
        "in": "query"
      }
    }
  },
  "security": [
    {
      "apiKeyHeader": [ ]
    },
    {
      "apiKeyQuery": [ ]
    }
  ]
}