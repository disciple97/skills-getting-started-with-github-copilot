import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Initial activities data for resetting between tests
initial_activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Competitive soccer practice and matches for students",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["alex@mergington.edu", "riley@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Pick-up games and team drills for basketball enthusiasts",
        "schedule": "Wednesdays and Fridays, 4:30 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["jordan@mergington.edu", "casey@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Create paintings, drawings, and mixed-media artwork",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["maya@mergington.edu", "zoe@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, stage production, and theater performance practice",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["liam@mergington.edu", "nora@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Team-based science challenges and competition prep",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["sophia@mergington.edu", "noah@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ethan@mergington.edu", "ava@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Test client fixture that resets the activities database before each test"""
    activities.clear()
    activities.update(initial_activities)
    return TestClient(app)