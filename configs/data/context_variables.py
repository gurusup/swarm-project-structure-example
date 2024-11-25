from datetime import datetime

context_variables = {
    "customer_context": {
        "CUSTOMER_ID": "customer_12345",
        "NAME": "John Doe",
        "PHONE_NUMBER": "(123) 456-7890",
        "EMAIL": "johndoe@example.com",
        "STATUS": "Premium",
        "ACCOUNT_STATUS": "Active",
        "LOCATION": "1234 Main St, San Francisco, CA 94123, USA"
    },
    "general_context": {
        "current_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}