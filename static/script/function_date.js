const btn_checkdate = document.getElementById("check_date");
const reponse = document.getElementById("message_verification");
const btn_envoie = document.getElementById("send_form");

btn_checkdate.addEventListener('click', () => {
    verificationDate();
});

async function verificationDate() {

    let url = new URL('/api/reservation', window.location.origin);
    url.searchParams.append('suiteId', suiteIdSelected.value);
    url.searchParams.append('start', start.value);
    url.searchParams.append('end', end.value);

    let resp = await fetch(url, {
        method: 'POST',
        headers: {
            "Content-type": "application/x-www-form-urlencoded"
        },
        body: `suiteId=${suiteIdSelected.value}&start=${start.value}&end=${end.value}`
    });

    if (resp.status == 204) {
        reponse.innerHTML = "Réservation possible à ces dates"
        btn_envoie.removeAttribute("hidden");
        btn_checkdate.setAttribute("disabled", "disabled");
    }
    else {
        messages = await resp.json();
        btn_checkdate.removeAttribute("disabled");
        btn_envoie.setAttribute("hidden", "hidden");
        let html;
        for (i = 0; i < messages.length; i++) {
            html += '<p>' + messages[i] + '</p>';
        };
        reponse.innerHTML = html
    }

}
