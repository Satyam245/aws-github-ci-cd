def lambda_handler(event, context):
print("Processing order event")
return {
"statusCode": 200,
"body": "Order processed successfully"
}
