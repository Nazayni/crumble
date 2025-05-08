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
