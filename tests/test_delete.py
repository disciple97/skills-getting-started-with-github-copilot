"""Tests for DELETE /activities/{activity_name}/signup endpoint"""

def test_delete_signup_success(client):
    """Test successful removal of a participant from an activity"""
    # Arrange - michael@mergington.edu is signed up for Chess Club

    # Act
    response = client.delete("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Removed michael@mergington.edu from Chess Club" == data["message"]

    # Verify participant was removed
    response2 = client.get("/activities")
    activities = response2.json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_delete_signup_nonexistent_participant(client):
    """Test delete fails when participant is not signed up"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.delete("/activities/Chess%20Club/signup?email=notsignedup@test.com")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Participant not found" == data["detail"]


def test_delete_signup_nonexistent_activity(client):
    """Test delete fails for non-existent activity"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.delete("/activities/NonExistent/signup?email=test@test.com")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]