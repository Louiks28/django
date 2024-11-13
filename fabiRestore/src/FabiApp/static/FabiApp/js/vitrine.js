// Ouvertre et Fermeture Menu déroulant
document.querySelectorAll('.dropdown-toggle').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            if (menu !== this.nextElementSibling) {
                menu.style.display = 'none';
                const icon = menu.previousElementSibling.querySelector('.logo_deroulant');
                icon.src = dropdownIconPath;
            }
        });

        const dropdownMenu = this.nextElementSibling;
        const icon = this.querySelector('.logo_deroulant');

        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
            icon.src = dropdownIconPath;
        } else {
            dropdownMenu.style.display = 'block';
            icon.src = upArrowIconPath;
        }
    });
});


// Un clic a l'extérieur et le menu ferme
document.addEventListener('click', function(event) {

if (!event.target.closest('.btn-effacer')) {
    const isClickInsideDropdown = event.target.closest('.dropdown');
    if (!isClickInsideDropdown) {
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            menu.style.display = 'none';
            const icon = menu.previousElementSibling.querySelector('.logo_deroulant');
            icon.src = dropdownIconPath;
        });
    }
}
});


// Effacer la sélection
document.querySelector('.btn-effacer').addEventListener('click', function() {
    // Supprimez la classe 'selected' de tous les éléments li dans le dropdown-menu
    document.querySelectorAll('.dropdown-menu li').forEach(li => {
        li.classList.remove('selected');
    });


    // Réinitialisez l'état du menu déroulant
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
        menu.style.display = 'none';
    });

    // Rétablir le texte initial des boutons
    const buttonVitrine2 = document.querySelector('.btn-vitrine2');
    buttonVitrine2.childNodes[0].textContent = "Disponibilité";
    
    const buttonVitrine1 = document.querySelector('.btn-vitrine1');
    buttonVitrine1.childNodes[0].textContent = "Catégories";

});



// Bouton tout_voir Catégories
document.querySelector('.dropdown_categorie .tout_voir').addEventListener('click', function() {
    // Ajoutez la classe 'selected' à tous les éléments li dans le dropdown-menu
    this.closest('.dropdown-menu').querySelectorAll('li:not(.tout_voir)').forEach(li => {
        li.classList.remove('selected');
    });
    // Fermez le dropdown-menu
    const dropdownMenu = this.closest('.dropdown-menu');
    dropdownMenu.style.display = 'none';

    // Rétablir le texte initial du bouton
    const buttonVitrine1 = document.querySelector('.btn-vitrine1');
    buttonVitrine1.childNodes[0].textContent = "Catégories";
});


// Bouton tout_voir Disponibilité
document.querySelector('.dropdown_statut .tout_voir').addEventListener('click', function() {
    // Ajoutez la classe 'selected' à tous les éléments li dans le dropdown-menu
    this.closest('.dropdown-menu').querySelectorAll('li:not(.tout_voir)').forEach(li => {
        li.classList.remove('selected'); 
    });
    // Fermez le dropdown-menu
    const dropdownMenu = this.closest('.dropdown-menu');
    dropdownMenu.style.display = 'none';

    // Rétablir le texte initial des boutons
    const buttonVitrine2 = document.querySelector('.btn-vitrine2');
    buttonVitrine2.childNodes[0].textContent = "Disponibilité";
});





// GESTION DES FILTRES

let selectedCategory = new URLSearchParams(window.location.search).get('categorie');
let selectedStatus = new URLSearchParams(window.location.search).get('statut');


// Fonction pour appliquer la classe 'selected' et mettre à jour le texte du bouton
function applySelectedState() {
    
    // Gérer le bouton Catégorie
    const categoryButton = document.querySelector('.btn-vitrine1');
    if (selectedCategory) {
        categoryButton.childNodes[0].textContent = selectedCategory + " "; // Mettre à jour le texte du bouton
        document.querySelectorAll('.dropdown_categorie li').forEach(link => {
            if (link.getAttribute('data-filter') === selectedCategory) {
                link.classList.add('selected'); // Ajouter la classe 'selected'
            } else {
                link.classList.remove('selected');
            }
        });
    } else {
        categoryButton.childNodes[0].textContent = "Catégories ";
    }

    // Gérer le bouton Statut
    const statusButton = document.querySelector('.btn-vitrine2');
    if (selectedStatus) {
        statusButton.childNodes[0].textContent = selectedStatus + " ";
        document.querySelectorAll('.dropdown_statut li').forEach(link => {
            if (link.getAttribute('data-filter') === selectedStatus) {
                link.classList.add('selected');
            } else {
                link.classList.remove('selected');
            }
        });
    } else {
        statusButton.childNodes[0].textContent = "Disponibilité ";
    }
}

// Appliquer l'état 'selected' et le texte du bouton au chargement de la page
applySelectedState();


// Gérer la sélection d'une catégorie
document.querySelectorAll('.dropdown_categorie li').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        selectedCategory = this.getAttribute('data-filter') === 'all' ? null : this.getAttribute('data-filter');
        updateMeubles();
    });
});

// Gérer la sélection d'un statut
document.querySelectorAll('.dropdown_statut li').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        selectedStatus = this.getAttribute('data-filter') === 'all' ? null : this.getAttribute('data-filter');
        updateMeubles();
    });
});

// Gérer le bouton Effacer pour réinitialiser les filtres
document.querySelector('.btn-effacer').addEventListener('click', function() {
    selectedCategory = null;
    selectedStatus = null;
    updateMeubles();
});

// Fonction pour mettre à jour les meubles affichés en fonction des filtres
function updateMeubles() {
    const url = new URL(window.location.href);
    if (selectedCategory) {
        url.searchParams.set('categorie', selectedCategory);
    } else {
        url.searchParams.delete('categorie');
    }
    if (selectedStatus) {
        url.searchParams.set('statut', selectedStatus);
    } else {
        url.searchParams.delete('statut');
    }
    // console.log("Statut : " , selectedStatus)
    // console.log("Catégorie : " , selectedCategory)

    // Affiche l'icône de chargement
    document.getElementById('loading-icon').style.display = 'block';

    // Rafraichit la page
    window.location.href = url.toString();

}
