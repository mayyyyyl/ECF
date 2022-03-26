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