# 🌟 Swarm Project - Intelligent Tour Management System

## 📝 Description
An advanced tour management system using multiple specialized agents to handle availability queries, cancellations, and reviews through a conversational interface.

## ✨ Key Features
- 🤖 Specialized multi-agent system
- 📅 Availability and booking management
- ❌ Cancellation processing
- ⭐ Reviews and feedback system
- 🔄 Automatic request triage

## 📁 Project Structure
```
swarm/
├── configs/
│ ├── agents/
│ │ └── types.py # Specialized agent definitions
│ ├── data/
│ │ └── context_variables.py # Context variables
│ ├── tools/
│ │ ├── tools.py # Core tools and functions
│ │ └── switchers.py # Agent switching functions
│ └── prompts.py # Agent instructions
└── main.py # Application entry point
```

## 🤖 Specialized Agents
| Agent | Function |
|--------|---------|
| **Triage** | Evaluates and routes requests to appropriate agent |
| **Availability** | Handles calendar queries and bookings |
| **Cancellation** | Processes cancellation requests |
| **Reviews** | Manages feedback and ratings |

## 🛠️ Core Functionality
### 📅 Availability Management
- Date availability verification
- Available time slots querying
- Calendar information
- Operating hours
- Booking process

### ❌ Cancellation Management
- Request processing
- Cancellation policies
- Refund handling
- Reason documentation

### ⭐ Review System
- Review submissions
- Feedback management
- Rating system
- Opinion collection

## 🚀 Environment Setup
1. Clone repository
2. Install Swarm package:

```
pip install git+https://github.com/openai/swarm.git
```

3. Install other dependencies
4. Configure environment variables (.env)
5. Run `python main.py`

## 🔄 Context Variables
The system uses two types of context:
- **Customer Context**: User-specific information
- **General Context**: System-wide information

## 🛠️ Available Tools
- Availability checking
- Schedule querying
- Calendar management
- Tour booking
- Agent switching system

## 👥 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Create Pull Request

## 📄 License
MIT

## 📧 Contact
For more information or inquiries, please open an issue in the repository.