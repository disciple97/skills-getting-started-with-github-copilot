"""Tests for GET /activities endpoint"""

def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all available activities"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9  # Number of initial activities
    assert "Chess Club" in data
    assert "Programming Class" in data

    # Verify structure of one activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_includes_participants(client):
    """Test that activities include participant lists"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()

    # Check that participants are included
    chess_participants = data["Chess Club"]["participants"]
    assert "michael@mergington.edu" in chess_participants
    assert "daniel@mergington.edu" in chess_participants
    assert len(chess_participants) == 2