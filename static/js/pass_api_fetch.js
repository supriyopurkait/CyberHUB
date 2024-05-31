function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function animateValue(obj, start, end, duration) {
    await delay(500);
    let startTimestamp = 0;
    const step = (timestamp) => {
    if (!startTimestamp) 
        startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start);
    if (progress < 1) {
        window.requestAnimationFrame(step);
    }
    };
    window.requestAnimationFrame(step);
}

function dataFormater (jsonDataDisplay,response) {
    if(response.isbreached == "True")
    {
        jsonDataDisplay.innerHTML = `<span> The Password has been breached </span> <strong class="data" id="num">0</strong> times <br> <strong id="caution">!! Please Change Your Password Immediately !!</strong>`;
    }
    if(response.isbreached == "False")
    {
        jsonDataDisplay.innerHTML = `<span> The Password hasn't been breached </span>`;
    }
}

const apiUrl = `http://${serverIp}:5000/api/password-breach`;

const jsonDataDisplay = document.querySelector("#jsonDataDisplay");
const submitBtn = document.querySelector(".submit-btn");

const fetchData = async (event) => {
    event.preventDefault();
    try {
        let passInput = await document.querySelector("#password").value;
        if(passInput !== "")
            {
                passInput = sha1(passInput)
                const data = { "password": passInput };
                let response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                let responseData = await response.json();
                dataFormater(jsonDataDisplay,responseData);
                if(responseData.isbreached == "True"){
                    const obj = document.getElementById("num");
                    animateValue(obj, 0, responseData.times, 3000);
                }
            } else {
                jsonDataDisplay.innerHTML = `<div> Please enter a password to check. </div>`;
            }
    } catch (error) {
        jsonDataDisplay.innerHTML = `<div>There was an error processing your request. Please try again later.</div>`;
    }
};

const enter = async (event) => {
    if (event.key === "Enter") {
        submitBtn.click();
    }
};

document.addEventListener("DOMContentLoaded", enter);
submitBtn.addEventListener("click", fetchData);