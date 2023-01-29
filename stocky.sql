-- Create a new table called 'stky' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('dbo.stky ', 'U') IS NOT NULL
DROP TABLE dbo.stky
GO
-- Create the table in the specified schema
CREATE TABLE dbo.stky  
(
    EmployeesId INT NOT NULL PRIMARY KEY,
    Name [NVARCHAR](50)  NOT NULL,
    Location [NVARCHAR](50)  NOT NULL
    -- specify more columns here
);
GO