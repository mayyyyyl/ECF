const btn_checkdate = document.getElementById("check_date");
const reponse = document.getElementById("message_verification");

btn_checkdate.addEventListener('click', () => {
    verificationDate();
});

async function verificationDate() {

    let resp = await fetch("/api/reservation");
    let reservations = await resp.json();

    console.log(reservations);

    if (resp.status == 204) {
        reponse.innerHTML = "Réservation possible à ces dates"
    }
    else {
        reponse.innerHTML = "Réservation pas possible à ces dates"
    }

}
