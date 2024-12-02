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
    "free_tours_context": {
        "booked_tours": [
            {
                "tour_id": "tour_001",
                "tour_name": "Golden Gate Bridge Walking Tour",
                "date": "2024-03-20",
                "time_slot": "10:00",
                "num_people": 2,
                "guide_name": "Alice Smith",
                "status": "confirmed"
            },
            {
                "tour_id": "tour_002",
                "tour_name": "Alcatraz Island Tour",
                "date": "2024-03-21",
                "time_slot": "14:00",
                "num_people": 4,
                "guide_name": "Bob Johnson",
                "status": "confirmed"
            }
        ]
    },
    "general_context": {
        "current_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}