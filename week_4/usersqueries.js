/**
	Title: usersqueries.js
    Author: Rachel White
    Date: February 2 , 2025
    Description: MongoDB Shell Scripts for the users collection queries.
 */

/**
 * User Queries
 */

db.users.find({});
db.users.find({ email: "jbach@me.com" });
db.users.find({ lastName: "Mozart" });
db.users.find({ firstName: "Richard" });
db.users.find({ employeeId: "1010" });
