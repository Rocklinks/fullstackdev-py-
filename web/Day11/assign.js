function fetchUserDetails(callback) {
    setTimeout(() => {
        const user = { id: 1, name: "Rocklin K S", email: "ksrocklin@gmail.com" };
        callback(user);
    }, 3000);
}

fetchUserDetails((user) => {
    console.log("User details fetched:", user);
});


function fetchUserData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = Math.random() > 0.3; // 70% success rate
            if (success) {
                resolve({ id: 2, name: "Raymond", email: "raymond@yahoo.com" });
            } else {
                reject("Failed to fetch user data");
            }
        }, 3000);
    });
}

fetchUserData()
    .then((user) => console.log("User data fetched:", user))
    .catch((error) => console.error("Error:", error));

