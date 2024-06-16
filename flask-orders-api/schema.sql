-- Creating the 'order' table
CREATE TABLE IF NOT EXISTS `order` (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID TEXT NOT NULL,
    Items TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ShippedAt TIMESTAMP,
    CompletedAt TIMESTAMP
);

-- Creating the 'item' table
CREATE TABLE IF NOT EXISTS `item` (
    ItemID TEXT PRIMARY KEY,
    OrderID INTEGER,
    Quantity INTEGER NOT NULL,
    Price INTEGER NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES `order` (OrderID)
);
