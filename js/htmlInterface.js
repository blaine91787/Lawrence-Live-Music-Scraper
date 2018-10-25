console.log("Hello");

function searchClick() {
        var venue = document.getElementById("venueSearch").value;
        var event = document.getElementById("eventSearch").value;
        console.log(event);
        console.log(venue);
        console.log("FUCK YOUUUUU")
        userKeyword = venue; // userKeyword is a variable in places.js
        initialize(); // initialize() is a function in places.js
}

function clearField(id) {
        switch (id.value) {
                case "Venue Search":
                        id.value='';
                        break;
                case "Event Search":
                        id.value='';
                        break;
        }
}
