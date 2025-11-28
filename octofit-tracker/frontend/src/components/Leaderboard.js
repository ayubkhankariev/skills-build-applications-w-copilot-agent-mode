import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

export default function Leaderboard() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched leaderboard:', results);
      });
  }, []);
  return (
    <div className="card shadow-sm mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>User</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {data.map((l, i) => (
                <tr key={i}>
                  <td>{i + 1}</td>
                  <td>{l.user}</td>
                  <td>{l.score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
