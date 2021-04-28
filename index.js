const admin = require('./node_modules/firebase-admin');
const serviceAccount = require("./serviceAccountKey.json");
const collectionKey = "members";
const data = require("./members.json");
// const collectionKey1 = "directors";
// const data1 = require("./newreferee1.json");
// const data2 = require("./newreferee2.json");
// const data3 = require("./newreferee3.json");
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://intempo-19a70.firebaseio.com"
});
const firestore = admin.firestore();
const settings = { timestampsInSnapshots: true };
firestore.settings(settings);

// upload member data
if (data && (typeof data === "object")) {
    Object.keys(data).forEach(docKey => {
        firestore.collection(collectionKey).doc(docKey).set(data[docKey]).then((res) => {
            console.log("Document " + docKey + " successfully written!");
        }).catch((error) => {
            console.error("Error writing document: ", error);
        }).finally(() => {
            console.log("All documents have been successfully written!");
        });
    });
    console.log(`${data.size()} documents have been written!`);
}

// // upload referee 1 data
// if (data1 && (typeof data1 === "object")) {
//     Object.keys(data1).forEach(docKey => {
//         firestore.collection(collectionKey1).doc(docKey).set(data1[docKey]).then((res) => {
//             console.log("Document " + docKey + " successfully written!");
//         }).catch((error) => {
//             console.error("Error writing document: ", error);
//         });
//     });
// }

// // upload referee 2 data
// if (data2 && (typeof data2 === "object")) {
//     Object.keys(data2).forEach(docKey => {
//         firestore.collection(collectionKey1).doc(docKey).set(data2[docKey]).then((res) => {
//             console.log("Document " + docKey + " successfully written!");
//         }).catch((error) => {
//             console.error("Error writing document: ", error);
//         });
//     });
// }

// // upload referee 3 data
// if (data3 && (typeof data3 === "object")) {
//     Object.keys(data3).forEach(docKey => {
//         firestore.collection(collectionKey1).doc(docKey).set(data3[docKey]).then((res) => {
//             console.log("Document " + docKey + " successfully written!");
//         }).catch((error) => {
//             console.error("Error writing document: ", error);
//         });
//     });
// }