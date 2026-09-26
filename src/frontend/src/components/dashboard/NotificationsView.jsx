import React from 'react';
import { Bell, AlertCircle, Info } from 'lucide-react';

export default function NotificationsView() {
  const notifs = [
    { title: 'Campus Maintenance', msg: 'Main server will be down for 2 hours on Sunday.', type: 'warning', time: '2 hours ago' },
    { title: 'Exam Schedule Released', msg: 'Midterm exam schedule is now available in your portal.', type: 'info', time: '5 hours ago' },
    { title: 'Library Dues', msg: 'Please return "Introduction to Algorithms" to avoid late fees.', type: 'alert', time: '1 day ago' },
  ];

  return (
    <div className="fade-in">
      <div className="dashboard-header" style={{ marginBottom: '2rem' }}>
        <h1>Notification Center</h1>
        <p className="subtitle">Global campus alerts and personal messages.</p>
      </div>
      
      <div className="grid grid-cols-1 gap-4">
        {notifs.map((n, i) => (
          <div key={i} className="card" style={{ display: 'flex', gap: '1.5rem', alignItems: 'flex-start' }}>
            {n.type === 'warning' ? <AlertCircle className="text-warning" size={28} /> : 
             n.type === 'alert' ? <AlertCircle className="text-danger" size={28} /> : 
             <Info className="text-secondary" size={28} />}
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <h3 style={{ fontWeight: 'bold' }}>{n.title}</h3>
                <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{n.time}</span>
              </div>
              <p style={{ color: 'var(--text-muted)' }}>{n.msg}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
