console.log('This is JS from your About page.')

function openPopup() {
    document.getElementById("popup").style.display = "flex";
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}

document.addEventListener('DOMContentLoaded', () => {
	const dropdown = document.querySelector('.dropdown');
	const toggle = dropdown.querySelector('.dropdown-toggle');

	toggle.addEventListener('click', () => {
		dropdown.classList.toggle('open');
	});
});

function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('submit', function (e) {
        if (e.target.matches('.follow-form')) {
            e.preventDefault();

            const form = e.target;
            const url = form.dataset.url;
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: "" // no need to send any extra data
            })
            .then(response => response.json())
            .then(data => {
                if (data.html) {
                    form.outerHTML = data.html; // Replace with updated button
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('submit', function (e) {
        if (e.target.matches('.follower-form')) {
            e.preventDefault();

            const form = e.target;
            const url = form.dataset.url;
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: "" // no need to send any extra data
            })
            .then(response => response.json())
            .then(data => {
                if (data.html) {
                    form.outerHTML = data.html; // Replace with updated button
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    });
});