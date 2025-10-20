# Platform API Configuration Guide

## 🔗 Connecting to Freelancing Platforms

### 1. **Upwork API Setup**

**Step 1: Create Upwork App**
- Go to [Upwork Developers](https://developers.upwork.com/)
- Create new application
- Get Client ID and Client Secret

**Step 2: OAuth2 Authentication**
```python
UPWORK_CONFIG = {
    'client_id': 'your_upwork_client_id',
    'client_secret': 'your_upwork_client_secret',
    'redirect_uri': 'https://your-domain.com/callback',
    'scope': 'read write'
}
```

**Available Endpoints:**
- `/profiles/v1/search/jobs` - Search jobs
- `/hr/v2/userroles/{user_id}/applications` - Submit proposals
- `/messages/v3/{room_id}` - Send/receive messages

---

### 2. **Fiverr API Setup**

**Step 1: Get API Access**
- Contact Fiverr Business Development
- Request API access (limited availability)
- Get API key

**Step 2: Configuration**
```python
FIVERR_CONFIG = {
    'api_key': 'your_fiverr_api_key',
    'base_url': 'https://api.fiverr.com/v1',
    'rate_limit': 1000  # per hour
}
```

**Available Features:**
- Create/manage gigs
- Handle orders and messages
- Track performance metrics

---

### 3. **Freelancer.com API Setup**

**Step 1: Register Application**
- Go to [Freelancer Developers](https://developers.freelancer.com/)
- Create new app
- Get Client ID and Secret

**Step 2: OAuth2 Setup**
```python
FREELANCER_CONFIG = {
    'client_id': 'your_freelancer_client_id',
    'client_secret': 'your_freelancer_client_secret',
    'sandbox_url': 'https://www.freelancer-sandbox.com/api',
    'production_url': 'https://www.freelancer.com/api'
}
```

**Key Endpoints:**
- `/projects/0.1/projects/` - Search projects
- `/projects/0.1/bids/` - Submit bids
- `/messages/0.1/threads/` - Messaging

---

## 🤖 Automated Integration Features

### **Project Scanning**
```python
# Scan all platforms every 3 hours
def scan_all_platforms():
    skills = ["web development", "mobile app", "AI/ML", "content writing"]
    
    for platform in ["upwork", "fiverr", "freelancer"]:
        projects = connector.search_projects(platform, skills)
        process_new_projects(projects)
```

### **Smart Bidding**
```python
# Auto-submit proposals based on criteria
def auto_bid_projects():
    for project in filtered_projects:
        proposal = generate_proposal(project)
        bid_amount = calculate_optimal_bid(project)
        connector.submit_proposal(platform, project.id, proposal, bid_amount)
```

### **Client Communication**
```python
# Automated client responses
def handle_client_messages():
    for platform in platforms:
        messages = connector.get_messages(platform)
        for message in messages:
            if requires_response(message):
                response = generate_response(message)
                connector.send_message(platform, message.sender_id, response)
```

---

## ⚠️ Important Considerations

### **Rate Limits**
- **Upwork**: 100 requests/hour
- **Fiverr**: 1000 requests/hour  
- **Freelancer**: 200 requests/hour

### **Terms of Service**
- Review each platform's automation policies
- Some platforms restrict automated bidding
- Focus on semi-automated assistance tools

### **Best Practices**
- Use webhooks for real-time updates
- Implement proper error handling
- Store credentials securely
- Monitor API usage limits
- Test in sandbox environments first

---

## 🚀 Quick Start

1. **Get API credentials** from each platform
2. **Update configuration** in `config.py`
3. **Run authentication** setup
4. **Test connections** with sample requests
5. **Enable automation** features

**Next**: Set up webhook endpoints for real-time project notifications!