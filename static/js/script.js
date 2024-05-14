  document.addEventListener('DOMContentLoaded', function() {
      var commandeForm = document.getElementById('commandeForm');
      var platImage = document.getElementById('platImage');
      var platNom = document.getElementById('platNom');
      var platQuantite = document.getElementById('platQuantite');
      var platDescription = document.getElementById('platDescription');
      var quantite = document.getElementById('quantite');
      var validerCommande = document.getElementById('validerCommande');
      var platNomInput = document.getElementById('platNomInput');
      var annuler = document.getElementById('annuler');

      var livreurForm = document.getElementById('livreurForm');

      var postulerButton = document.getElementById('postulerButton');

      postulerButton.addEventListener('click', function afficherFormulaire() {
        var emailValue = document.getElementById("email").value;
        if (emailValue.trim() !== "") {
            livreurForm.style.display = 'block';
        } else {
            console.log("Veuillez saisir votre email.");
        } 
        });

      var orderButtons = document.querySelectorAll('.order-button');

      orderButtons.forEach(function(button) {
          button.addEventListener('click', function () {
              var platDetails = {
                  image_url: button.dataset.imageUrl,
                  libelle: button.dataset.libelle,
                  quantite: parseInt(button.dataset.quantite),
                  description: button.dataset.description
              };

              platImage.src = platDetails.image_url;
              platNom.textContent = platDetails.libelle;
              platQuantite.textContent = "Quantité : " + platDetails.quantite;
              platDescription.textContent = platDetails.description;
              commandeForm.style.backgroundImage = "url('" + platDetails.image_url + "')";
              commandeForm.style.backgroundSize = "cover";
              commandeForm.style.display = 'block';
          })
      });

      livreurForm.addEventListener('click', function() {
        
        commandeForm.style.display = 'none';
        document.getElementById('commandeForm').submit()
    });

      validerCommande.addEventListener('click', function() {
          var quantity = quantite.value;
          var platNomElement = document.getElementById('platNom');
          var platNom = platNomElement.textContent.trim();

          console.log('Quantité sélectionnée:', quantity);
          console.log('Nom du plat:', platNom);

          platNomInput.value = platNom;

          commandeForm.style.display = 'none';
          document.getElementById('commandeForm').submit()
      });

      annuler.addEventListener('click', function() {
          commandeForm.style.display = 'none'
      });

      var heartButtons = document.querySelectorAll('.heart-button');

      heartButtons.forEach(function(button) {
          button.addEventListener('click', function () {
              var heartPath = button.querySelector('.heart-path');

              // Inverser la couleur du cœur
              if (heartPath.style.fill === 'brown') {
                  heartPath.style.fill = 'black';
              } else {
                  heartPath.style.fill = 'brown';
              }
          })
      })
  });

  function toggleMiniForm() {
    var formContainer = document.getElementById('miniFormContainer');
    if (formContainer.classList.contains('hidden')) {
        formContainer.classList.remove('hidden');
    } else {
        formContainer.classList.add('hidden');
    }
}
function closeForm() {
    document.getElementById("livreurForm").style.display = "none";
}