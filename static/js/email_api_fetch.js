function dataFormater(response, emailInput) {
    if(response.status == "failed"){
        return "<div>" + response.message + "</div>";

    }

    else if(response.is_breached == false){
        return `<div>No breach found for ${emailInput}</div>`;
    }

    else{
        let data = `<strong id="caution">!! Please Change your credentials Immediately !!</strong>`;
        data += `<div> Total number of breaches found: ${response.data.length}</div>`;
        response.data.forEach(breach => {
            data += `<div class="topOuter">`;
            data += `<div class="detailsContainer">`;
            data += `<img src="` + breach.LogoPath + `" alt="` + breach.Name + `" onerror="this.src='../static/assets/undifined.png';">`;
            data += `<div class="details">`;
            data += `<div class="name"><strong>Name:</strong> <p class="resultData">` + breach.Name + `</p></div>`;
            data += `<div class="domain"><strong>Domain Name:</strong> <p class="resultData"><a href="https://` + breach.Domain + `">` + breach.Domain + `</a></p></div>`;
            data += `<div class="date"><strong>Breached On:</strong> <p class="resultData">` + breach.BreachDate + `</p></div>`;
            data += `<div class="leak"><strong>Potential Leakage:</strong> <p class="resultData">${breach.DataClasses.join(", ")}</p></div>`;
            data += `</div>`; 
            data += `</div>`;
            data += `</div>`;
            data +="<hr>";
            });
        return data;
    }
}


const emailInputField = document.querySelector("#email");
const jsonDataDisplay = document.querySelector("#jsonData");
const submitBtn = document.querySelector(".submit-btn");

const apiUrl = `http://${serverIp}:5000/api/email-breach`;

const fetchData = async (event) => {
    event.preventDefault(); // Prevents default form submission behavior
    try {
        jsonDataDisplay.innerHTML = "<div>Please wait...</div>";
        const emailInput = emailInputField.value.trim();
        if (emailInput && emailInput.includes("@")) {
            const data = { "email": emailInput };
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            const responseData = await response.json();
            jsonDataDisplay.innerHTML = dataFormater(responseData, emailInput);
        } else {
            jsonDataDisplay.innerHTML = "<div>Please enter a valid email address.</div>";
        }
    } catch (error) {
        jsonDataDisplay.innerHTML = "<div>There was an error processing your request. Please try again later.</div>";
    }
};

const handleEnterKey = (event) => {
    if (event.key === "Enter") {
        fetchData(event);
    }
};

document.addEventListener("DOMContentLoaded", () => {
    emailInputField.addEventListener("keydown", handleEnterKey);
    submitBtn.addEventListener("click", fetchData);
});