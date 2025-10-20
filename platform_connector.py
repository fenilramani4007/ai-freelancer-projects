"""
AI Freelancer Agent - Platform Integration Module
Connects to Upwork, Fiverr, and Freelancer.com APIs
"""

import requests
import json
from datetime import datetime
import time

class FreelancerPlatformConnector:
    def __init__(self):
        self.platforms = {
            'upwork': {
                'base_url': 'https://www.upwork.com/api',
                'auth_type': 'oauth2',
                'rate_limit': 100  # requests per hour
            },
            'fiverr': {
                'base_url': 'https://api.fiverr.com/v1',
                'auth_type': 'api_key',
                'rate_limit': 1000  # requests per hour
            },
            'freelancer': {
                'base_url': 'https://www.freelancer.com/api',
                'auth_type': 'oauth2',
                'rate_limit': 200  # requests per hour
            }
        }
        
    def authenticate_upwork(self, client_id, client_secret, access_token):
        """Authenticate with Upwork API using OAuth2"""
        headers = {
            'Authorization': f'Bearer {access_token}',
            'User-Agent': 'AI-Freelancer-Agent/1.0'
        }
        return headers
    
    def authenticate_fiverr(self, api_key):
        """Authenticate with Fiverr API"""
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        return headers
    
    def authenticate_freelancer(self, access_token):
        """Authenticate with Freelancer API using OAuth2"""
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        return headers
    
    def search_projects(self, platform, skills, budget_min=100, budget_max=10000):
        """Search for projects on specified platform"""
        if platform == 'upwork':
            return self._search_upwork_projects(skills, budget_min, budget_max)
        elif platform == 'fiverr':
            return self._search_fiverr_projects(skills, budget_min, budget_max)
        elif platform == 'freelancer':
            return self._search_freelancer_projects(skills, budget_min, budget_max)
    
    def _search_upwork_projects(self, skills, budget_min, budget_max):
        """Search Upwork for matching projects"""
        params = {
            'q': ' OR '.join(skills),
            'budget': f'{budget_min}-{budget_max}',
            'job_type': 'hourly,fixed',
            'duration': 'week,month,ongoing',
            'sort': 'recency'
        }
        # Implementation for Upwork API call
        return self._make_api_request('upwork', '/profiles/v1/search/jobs', params)
    
    def submit_proposal(self, platform, job_id, proposal_text, bid_amount):
        """Submit proposal to a project"""
        proposal_data = {
            'job_id': job_id,
            'cover_letter': proposal_text,
            'bid_amount': bid_amount,
            'estimated_duration': self._calculate_duration(bid_amount)
        }
        
        if platform == 'upwork':
            return self._submit_upwork_proposal(proposal_data)
        elif platform == 'fiverr':
            return self._create_fiverr_gig(proposal_data)
        elif platform == 'freelancer':
            return self._submit_freelancer_bid(proposal_data)
    
    def get_messages(self, platform, conversation_id=None):
        """Retrieve messages from platform"""
        if platform == 'upwork':
            return self._get_upwork_messages(conversation_id)
        elif platform == 'fiverr':
            return self._get_fiverr_messages(conversation_id)
        elif platform == 'freelancer':
            return self._get_freelancer_messages(conversation_id)
    
    def send_message(self, platform, recipient_id, message_text):
        """Send message to client"""
        message_data = {
            'recipient_id': recipient_id,
            'message': message_text,
            'timestamp': datetime.now().isoformat()
        }
        
        if platform == 'upwork':
            return self._send_upwork_message(message_data)
        elif platform == 'fiverr':
            return self._send_fiverr_message(message_data)
        elif platform == 'freelancer':
            return self._send_freelancer_message(message_data)
    
    def _make_api_request(self, platform, endpoint, params=None, data=None, method='GET'):
        """Generic API request handler with rate limiting"""
        base_url = self.platforms[platform]['base_url']
        url = f"{base_url}{endpoint}"
        
        # Rate limiting
        time.sleep(3600 / self.platforms[platform]['rate_limit'])
        
        try:
            if method == 'GET':
                response = requests.get(url, params=params, headers=self._get_headers(platform))
            elif method == 'POST':
                response = requests.post(url, json=data, headers=self._get_headers(platform))
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"API request failed for {platform}: {e}")
            return None
    
    def _get_headers(self, platform):
        """Get authentication headers for platform"""
        # This would use stored credentials
        # Implementation depends on authentication setup
        pass
    
    def _calculate_duration(self, bid_amount):
        """Calculate project duration based on bid amount"""
        if bid_amount < 500:
            return "1-2 weeks"
        elif bid_amount < 2000:
            return "2-4 weeks"
        else:
            return "1-2 months"

# Usage Example
if __name__ == "__main__":
    connector = FreelancerPlatformConnector()
    
    # Search for web development projects
    skills = ["web development", "react", "node.js", "python"]
    projects = connector.search_projects("upwork", skills, 500, 5000)
    
    print(f"Found {len(projects)} matching projects")