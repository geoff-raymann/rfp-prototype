
CREATE TABLE IF NOT EXISTS certifications (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    certification_id TEXT UNIQUE NOT NULL,
    expiry_date DATE NOT NULL,
    status TEXT NOT NULL
);

INSERT INTO certifications (name, certification_id, expiry_date, status) VALUES
('John Doe', 'CERT123', '2026-12-31', 'Valid'),
('Jane Smith', 'CERT456', '2024-07-30', 'Valid'),
('Alice Johnson', 'CERT789', '2023-11-15', 'Invalid'),
('Bob Brown', 'CERT101', '2025-10-01', 'Valid'),
('Charlie Davis', 'CERT202', '2025-01-20', 'Valid');
