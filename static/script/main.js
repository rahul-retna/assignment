const _ = s => document.querySelector(s)

const getData = (id) => {
    element = _(`#${id}`);
    value = element.value;
    if(typeof(value || undefined) === 'undefined') {
        element.classList.add("error");
        throw new Error(`missing value for #${id}`)
    }
    element.classList.remove("error")
    return value
}

const pretty = charge => {
    charge = (Math.floor(parseFloat(charge) * 100) / 100) || charge;
    charge = charge.toLocaleString("en-US")
    return charge
}

window.onload = () => {
    _(".submit").addEventListener("click", () => {
        let age, sex, bmi, children, smoker, region, error = false
        try {
            age = getData("age");
            sex = getData("sex");
            bmi = getData("bmi");
            children = getData("children");
            smoker = getData("smoker");
            region = getData("region");
        } catch(err) {
            console.log(err);
            error = true
        } finally {
            if(!error) {
                fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    }, body: JSON.stringify({
                        age,
                        sex,
                        bmi,
                        children,
                        smoker,
                        region
                    })
                }).then(resp => {
                    return resp.json()
                }).then(data=>{
                    if(!data.success) {
                        throw new Error("failed to fetch")
                    }
                    _(".err").innerHTML = ""
                    _(".result").innerHTML = pretty(data.charge)
                }).catch(error => {
                    console.log(error);
                    _(".err").innerHTML = "Error"
                    _(".result").innerHTML = ""
                })
            }
        }
    })
}
