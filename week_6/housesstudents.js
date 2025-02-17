/**Rachel White 
2/16/2024
Week 6 - Assignment 6.2 - Aggregate Queries 

*/

db.students.find({});



white = {
	"firstName": "Rachel",
	"lastName": "White",
	"studentId": "s1019",
	"houseId": "h1010"
}

// Insert the documents.
db.students.insertOne(white);



db.students.find({studentId: "s1019"}).pretty(); // Verify the addition





db.students.updateOne(
    { studentId: "s1019" },
    { $set: { "houseId": "h1007" } } //Changes house


);
 
db.students.find({studentId: "s1019"}).pretty(); // Verify the update



db.students.deleteOne({ studentId: "s1019" });


db.students.find({ studentId: "s1019" }).pretty()// Verify the deletion



db.students.aggregate([
    {
        $group: {
            _id: "$houseId",
            students: {
                $push: {
                    firstName: "$firstName",
                    lastName: "$lastName",
                    studentId: "$studentId"
                }
            }
        }
    },
    {
        $project: {
            _id: 0,
            houseId: "$_id",
            students: 1
        }
    },
    {
        $sort: { houseId: 1 }
    }
]);




db.students.find({houseId: "h1007"}).pretty();


db.students.find({houseId: "h1009"}).pretty();


db.houses.aggregate([
    // 1. Match houses with an "Eagle" mascot
    {
        $match: {
            mascot: "Eagle"
        }
    },
    // 2. Lookup students
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $project: {
            _id: 1,
            mascot: 1,
            founder: 1,
            houseId: 1,
            students: {
                $map: {
                    input: "$students",
                    as: "student",
                    in: {
                        firstName: "$$student.firstName",
                        lastName: "$$student.lastName",
                        studentId: "$$student.studentId"
                    }
                }
            }
        }
    },
    {
        $sort: {
            houseId: 1
        }
    }
])


