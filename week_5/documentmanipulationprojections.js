/**
	Title: documentmanipulationprojections.js
    Author: Rachel White
    Date: February 9 , 2025
    Description: Hands-On 5.1: MongoDB Document Manipulation and Projections
 */

/**
 * Queries
 */


/**Instructions: 
1. Write the following queries and take screenshots of the code you used to write the queries and their results.

 a. Add a new user to the user’s collection. Ensure the fields in the new document match the existing fields in the user’s collection. Next, prove the new user was added successfully. 

*/
//Antonio Vivaldi

db.users.insertOne({
    firstName: "Antonio",
    lastName: "Vivaldi",
    employeeId: '1013',
   email: "avivaldi@me.com",
   dateCreated: new Date()
});

db.users.find({ email: "avivaldi@me.com" }).pretty();




//b. Update Mozart’s email address to mozart@me.com. Next, prove the document was updated successfully. 

db.users.updateOne(
    { firstName: "Wolfgang", lastName: "Mozart" },
    { $set: { email: "mozart@me.com" } });

db.users.find({ firstName: "Wolfgang", lastName: "Mozart" }).pretty();


//c. Display all users in the collection. Use projections to only show the first name, last name, and email address.

db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 }).pretty();
