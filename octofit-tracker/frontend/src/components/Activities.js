import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Activities API endpoint:', apiUrl);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4">Activities</h2>
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-dark">
                <tr>
                  <th>#</th>
                  <th>Type</th>
                  <th>Duration</th>
                  <th>Calories</th>
                  <th>User</th>
                </tr>
              </thead>
              <tbody>
                {activities.length === 0 ? (
                  <tr><td colSpan="5" className="text-center">No activities found</td></tr>
                ) : (
                  activities.map((activity, idx) => (
                    <tr key={activity.id || idx}>
                      <td>{idx + 1}</td>
                      <td>{activity.type || '-'}</td>
                      <td>{activity.duration || '-'}</td>
                      <td>{activity.calories || '-'}</td>
                      <td>{activity.user || '-'}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Activities;
