// This is where we can put in JavaScript if we need itconsole.log('This is JS fromt the home page')
document.addEventListener("DOMContentLoaded", function() {
    console.log("Grabbing buttons")
    function getCsrfToken() {
        console.log("Got the form")
        return document.querySelector("#csrf-form input[name='csrfmiddlewaretoken']").value;
    }
    //Gabs all of the buttons and applies the click listner
    document.querySelectorAll(".save-job-btn").forEach(button => {
        button.addEventListener("click", function() {
            console.log("Clicked")
            //Attribute is defined on creation
            let jobId = this.getAttribute("data-job-id");
            //Checks if the content of the button has the word save, then adds the appropriate url
            const icon = this.querySelector('i');
            let actionUrl = icon.classList.contains("fa-regular") ? "/save-job/" : "/unsave-job/";
            console.log(actionUrl);
            let csrfToken = getCsrfToken();

            //Calls a fetch to the views for the function
            fetch("/jobs" + actionUrl + jobId + "/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                //Error Thrown if response is not ok
                if (!response.ok) {
                    throw new Error("HTTP error " + response.status);
                }
                return response.json();
            })
            .then(data => {
                //Displays the message that the process was successful 
                //Can comment this out for production to be less intrusive
                alert(data.message);
                //Checks if the button says save, replaces with the opposite
                if (icon.classList.contains("fa-regular")){
                    icon.classList.remove('fa-regular');
                    icon.classList.add('fa-solid');
                } else {
                    icon.classList.remove('fa-solid');
                    icon.classList.add('fa-regular');
                }
            })
            //Errors if anything goes unexpectadly
            .catch(error => console.error("Error:", error));
        });
    });
});