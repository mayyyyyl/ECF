const btn_checkdate = document.getElementById("check_date");
const reponse = document.getElementById("message_verification");

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
    }
    else {
        messages = await resp.json();
        let html;
        for (i = 0; i < messages.length; i++) {
            html += '<p>' + messages[i] + '</p>';
        };
        reponse.innerHTML = html
    }

}

async function getsuites() {

    let url = new URL('/api/suites', window.location.origin);
    url.searchParams.append('hotelId', hotelIdSelected.value);

    let resp = await fetch(url, {
        method: 'GET',
        headers: {
            "Content-type": "application/x-www-form-urlencoded"
        }
    });

    let html;
    if (resp.status == 204) {

        html += '<option> Pas de suites pour le moment</option>'
        document.getElementById("suiteIdSelected").innerHTML = html;
    }
    else {
        let suites = await resp.json();

        for (let i = 0; i < suites.length; i++) {

            html += '<option value="' + suites[i].id + '">' + suites[i].titre + '</option>';

        }
        document.getElementById("suiteIdSelected").innerHTML = html;
    }
}

getsuites()