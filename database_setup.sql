```sql
-- Database Setup for AI-Enhanced Smart Material Analyzer

-- Create database
CREATE DATABASE materials_db;

-- Switch to the new database
\c materials_db;

-- Create table for sensor data
CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    density FLOAT NOT NULL,
    composition VARCHAR(255) NOT NULL,
    thermal_conductivity FLOAT NOT NULL
);

-- Create table for material properties
CREATE TABLE material_properties (
    id SERIAL PRIMARY KEY,
    material_name VARCHAR(255) NOT NULL,
    density_range FLOAT[2] NOT NULL,
    composition VARCHAR(255) NOT NULL,
    thermal_conductivity_range FLOAT[2] NOT NULL
);

-- Create table for quality assessment
CREATE TABLE quality_assessment (
    id SERIAL PRIMARY KEY,
    material_id INT REFERENCES material_properties(id),
    timestamp TIMESTAMP NOT NULL,
    quality_score FLOAT NOT NULL,
    defects VARCHAR(255)
);

-- Create table for user data
CREATE TABLE user_data (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    access_level INT NOT NULL
);
```
