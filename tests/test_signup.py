"""Tests for POST /activities/{activity_name}/signup endpoint"""

def test_signup_success(client):
    """Test successful signup for an activity"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.post("/activities/Chess%20Club/signup?email=new@student.edu")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Signed up new@student.edu for Chess Club" == data["message"]

    # Verify participant was added
    response2 = client.get("/activities")
    activities = response2.json()
    assert "new@student.edu" in activities["Chess Club"]["participants"]


def test_signup_duplicate_participant(client):
    """Test signup fails when student is already signed up"""
    # Arrange - daniel@mergington.edu is already signed up for Chess Club

    # Act
    response = client.post("/activities/Chess%20Club/signup?email=daniel@mergington.edu")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student already signed up for this activity" == data["detail"]


def test_signup_nonexistent_activity(client):
    """Test signup fails for non-existent activity"""
    # Arrange - activities are reset to initial state by fixture

    # Act
    response = client.post("/activities/NonExistent/signup?email=test@test.com")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" == data["detail"]