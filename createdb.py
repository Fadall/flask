from app import app, db
from src.models import Commande, Livreur, Panier, Plat, Users

with app.app_context():
    db.drop_all()

    db.create_all()

    new_user = Users(role =0,prenom='Fadal', nom='Kebe', telephone=781019310, password='passer', user_img="")
    new_user2 = Users(prenom='Embeka', nom='Kebe', telephone=775200001, password='passer', user_img="")

    new_plat = Plat(libelle='Yassa Guinar', quantite=32, prix=2500, image_url="https://i.pinimg.com/564x/25/66/c7/2566c7d3313749a0ac6dabfe42f41141.jpg", description="Un plat sénégalais emblématique, le Yassa Guinar est une délicieuse préparation de poulet mariné dans une sauce épicée et acidulée à base d'oignons, de moutarde et de citron. C'est un régal pour les papilles avec une explosion de saveurs africaines authentiques.")
    new_plat2 = Plat(libelle='Couscous Marocain', quantite=15, prix=1500, image_url="https://i.pinimg.com/564x/e0/14/87/e01487dfd4f36748fa7f56fc72659fdf.jpg", description="Originaire du Maroc, le Couscous Marocain est un plat traditionnellement préparé avec de la semoule de blé dur, des légumes colorés tels que les carottes, les courgettes et les pois chiches, le tout cuit à la vapeur et accompagné d'une sauce aromatique.")
    new_plat3 = Plat(libelle='Fufu', quantite=27, prix=1500, image_url="https://i.pinimg.com/564x/2c/0d/f5/2c0df556b9d08e2940d15a5e5ab9cff0.jpg", description="Un plat populaire d'Afrique de l'Ouest, le Fufu est une pâte épaisse et élastique faite à partir de farine de manioc, de banane plantain ou d'autres tubercules. Il est souvent servi avec une variété de soupes ou de sauces épicées.")
    new_plat4 = Plat(libelle='Thiebou Djeun', quantite=20, prix=2000, image_url="https://i.pinimg.com/564x/f1/c9/a7/f1c9a75b6ba165496d4143b1814ad40c.jpg", description="Considéré comme le plat national du Sénégal, le Thiebou Djeun est un ragoût de poisson cuit dans une sauce tomate épicée avec des légumes tels que le chou, les carottes et l'aubergine, servi avec du riz cassé. C'est un incontournable de la cuisine sénégalaise.")
    new_plat5 = Plat(libelle='Jollof Rice', quantite=12, prix=2500, image_url="https://i.pinimg.com/564x/18/1b/ad/181baddb1f195c60d88b4eddb5dac16f.jpg", description="Un plat emblématique de l'Afrique de l'Ouest, le Jollof Rice est un riz épicé cuit dans une sauce tomate avec des oignons, du piment et des épices. Il est souvent accompagné de viande ou de poulet et est apprécié pour son goût riche et savoureux.")
    new_plat6 = Plat(libelle='Attieke Poisson', quantite=35, prix=2000, image_url="https://i.pinimg.com/564x/37/47/6b/37476bbfaac200423f671832101a13b1.jpg", description="Originaire de la Côte d'Ivoire, l'Attieke Poisson est un plat composé d'Attieke, une semoule de manioc fermentée, accompagnée de poisson grillé et d'une sauce tomate épicée. C'est un plat délicieusement léger et rafraîchissant.")
    new_plat7 = Plat(libelle='Riz Cantonais', quantite=23, prix=3000, image_url="https://i.pinimg.com/564x/7e/c3/bf/7ec3bfb211f6c7802deca944d6ae8bfa.jpg", description="Un plat populaire de la cuisine chinoise, le Riz Cantonais est un riz sauté avec des petits pois, des carottes, des œufs et parfois du porc ou du poulet. Il est assaisonné de sauce soja et est souvent servi comme plat d'accompagnement dans les repas chinois.")
    new_plat8 = Plat(libelle='Mafé', quantite=8, prix=1500, image_url="https://i.pinimg.com/564x/07/ac/de/07acde3040a4fd5c1f3150b3652cf12d.jpg", description="Originaire d'Afrique de l'Ouest, le Mafé est un ragoût de viande (généralement du bœuf ou du poulet) cuit dans une sauce aux arachides, aux tomates et aux légumes. Il est servi avec du riz ou du couscous et est apprécié pour son goût riche et crémeux.")
    new_plat8 = Plat(libelle='Tô', quantite=17, prix=1500, image_url="https://i.pinimg.com/564x/03/c2/ca/03c2ca0070ea5fbca8c3af38a5409b84.jpg", description="Un plat traditionnel du Togo, le Tô est une bouillie épaisse faite à partir de farine de maïs ou de millet. Il est souvent consommé avec une sauce épicée à base de viande ou de légumes et est apprécié pour sa texture réconfortante et son goût savoureux.")

    new_livreur = Livreur(prenom='Alioune', nom='Kamara', telephone = '785945623')
    new_livreur2 = Livreur(prenom='Malick', nom='Diop', telephone = '778748712')
    new_livreur3 = Livreur(prenom='Aziz', nom='Dabo', telephone = '771559057')

    new_panier = Panier(plat='Yassa Guinar', client='775200001', image_url='https://i.pinimg.com/564x/25/66/c7/2566c7d3313749a0ac6dabfe42f41141.jpg', quantite=32, description="Un plat sénégalais emblématique, le Yassa Guinar est une délicieuse préparation de poulet mariné dans une sauce épicée et acidulée à base d'oignons, de moutarde et de citron. C'est un régal pour les papilles avec une explosion de saveurs africaines authentiques.")
    new_panier2 = Panier(plat='Couscous Marocain', client='775200001', image_url='https://i.pinimg.com/564x/e0/14/87/e01487dfd4f36748fa7f56fc72659fdf.jpg', quantite=15, description="Originaire du Maroc, le Couscous Marocain est un plat traditionnellement préparé avec de la semoule de blé dur, des légumes colorés tels que les carottes, les courgettes et les pois chiches, le tout cuit à la vapeur et accompagné d'une sauce aromatique.")

    Commande.query.delete()

    db.session.add(new_user)
    db.session.add(new_user2)

    db.session.add(new_plat)
    db.session.add(new_plat2)
    db.session.add(new_plat3)
    db.session.add(new_plat4)
    db.session.add(new_plat5)
    db.session.add(new_plat6)
    db.session.add(new_plat7)
    db.session.add(new_plat8)

    db.session.add(new_livreur)
    db.session.add(new_livreur2)
    db.session.add(new_livreur3)

    db.session.add(new_panier)
    db.session.add(new_panier2)

    db.session.commit()

    print("Base de données créée avec succès et utilisateur ajouté !")
