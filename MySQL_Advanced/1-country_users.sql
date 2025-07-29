-- Create users table with country enumeration
-- Requirements:
-- - id: integer, never null, auto increment, primary key
-- - email: string (255 chars), never null, unique
-- - name: string (255 chars), nullable
-- - country: enumeration (US, CO, TN), never null, default US
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
