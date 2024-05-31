function dataFormater(responseData,Display) {
    if(String(responseData.status)==='success'){
        let formattedData = responseData.types.join(', ');
        let data = `<span> The hash is possibly: </span> <strong id="data">` + formattedData +  "</strong>";
        Display.innerHTML = data;
    }
    else{
        Display.innerHTML = `<span> Can't identify this hash. </span>`;
    }
}

const apiUrl = `http://${serverIp}:5000/api/hash-id`;

    
const jsonDataDisplay = document.querySelector("#jsonDataDisplay");
const submitBtn = document.querySelector(".submit-btn");

const fetchData = async (event) => {
    event.preventDefault(); 
    try {
        const hashInput = await document.querySelector("#hash").value;
        if(hashInput !== "")
            {
                const data = { "hash": hashInput };
                let response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                let responseData = await response.json();
                dataFormater(responseData,jsonDataDisplay);
            } else {
                jsonDataDisplay.innerHTML = `<div> Please enter a hash. </div>`;
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