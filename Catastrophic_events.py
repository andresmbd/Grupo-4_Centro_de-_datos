import random

events = {
    
    #Negative Events

    "negative" : [
        {"name": "Cooling System Failure",
         "temperature": 20,
         "clients": 0,
         "servers": -1
        },
        {"name": "Power Surge",
         "temperature": 10,
         "clients": 5,
         "servers": 1
        },
        {"name": "Severe Storm",
         "temperature": 5,
         "clients": 10,
         "servers": 0
        },
        {"name": "Power Outage",
         "temperature": 8,
         "clients": 15,
         "servers": 1
        },
        {"name": "Critical Server Failure",
         "temperature": 5,
         "clients": 20,
         "servers": 1
        },
        {"name": "Internal Virus Attack",
         "temperature": 0,
         "clients": 25,
         "servers": 0
        },
        {"name": "DDoS Attack",
         "temperature": 0,
         "clients": 30,
         "servers": 0
        },
        {"name": "Minor Fire in the Server Room",
         "temperature": 25,
         "clients": 15,
         "servers": 2
        },
        {"name": "Coolant Leak",
         "temperature": 15,
         "clients": 5,
         "servers": 1
        },
        {"name": "Administrator Human Error",
         "temperature": 3,
         "clients": 10,
         "servers": 0
        }
    ],

    #Neutral Events

    "neutral": [
    {
        "name": "Preventive Maintenance",
        "temperature": -5,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Technical Inspection",
        "temperature": 0,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Internal Audit",
        "temperature": 0,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Software Update",
        "temperature": 2,
        "clients": 5,
        "servers": 0
    },
    {
        "name": "Network Monitoring",
        "temperature": 0,
        "clients": 3,
        "servers": 0
    },
    {
        "name": "Staff Training",
        "temperature": 0,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Equipment Cleaning",
        "temperature": -3,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Performance Testing",
        "temperature": 2,
        "clients": 0,
        "servers": 0
    },
    {
        "name": "Server Optimization",
        "temperature": -4,
        "clients": 10,
        "servers": 0
    },
    {
        "name": "Stable Day",
        "temperature": 0,
        "clients": 0,
        "servers": 0
    }
]
}


category = random.choice(["negative", "neutral"])
event_ = random.choice(events[category])
print(f"⚠️ㅤALERT: {event_['name']}!\n🌡️ㅤTemperature increased by {event_['temperature']} °C\n🖥️ㅤ{event_['servers']} server damaged")