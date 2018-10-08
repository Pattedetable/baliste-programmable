//
// Copyright 2018 Manuel Barrette
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//*****************************************************************************/
//
// Auteur original : Manuel Barrette
// Première version : 5 mars 2018
//
// Auteur-e-s suivant-e-s :
//
// Dernière modification : 31 août 2018
//
/*****************************************************************************/

#ifndef CHAR_BALISTE_H_INCLUDED
#define CHAR_BALISTE_H_INCLUDED

class Baliste
{

	public:


	/*****************************************************************************/
	//
	// Prototypes de fonctions
	//
	
	// Constructeur
	Baliste();
	
	// Destructeur
	~Baliste();
	
	// Obtenir la valeur actuelle de l'angle de rotation
	int getAngle() const;

	// Obtenir la valeur de la limite de rotation permise
	int getLimite() const;

	// Obtenir la valeur des pins des moteurs
	int getM1() const;
	int getM2() const;
	int getM3() const;
	int getM4() const;

	// Obtenir la valeur des pins pour les boutons
	int getBoutonRouge() const;
	int getBoutonNoir1() const;
	int getBoutonNoir2() const;

	// Convertir un pourcentage en base 255
	int conversionPourcent(int pourcentVoltage);
	
	// Attendre un temps donné en millisecondes
	void attendrePendant(unsigned long temps);

	// Arrêter les roues
	void arreter();
	
	// Faire avancer l'engin
	void avancer(int pourcentVoltage = 100);
	
	// Avancer pendant un certain temps (en millisecondes)
	void avancerPendant(long int temps, int pourcentVoltage = 100);
	
	// Faire reculer l'engin
	void reculer(int pourcentVoltage = 100);
	
	// Reculer pendant un certain temps (en millisecondes)
	void reculerPendant(long int temps, int pourcentVoltage = 100);
	
	// Faire augmenter graduellement le voltage des roues
	void accelerer(int sens, int pourcentVoltage = 100);
	
	// Faire diminuer graduellement le voltage des roues
	void decelerer(int sens, int pourcentVoltage = 100);
	
	// Arrêter le mouvement de la tourelle
	void arreterTourelle();
	
	// Faire tourner la tourelle dans le sens horaire
	void tourelleHoraire(int pourcentVoltage = 100);
	
	// Faire tourner la tourelle dans le sens horaire pendant un certain temps (en millisecondes)
	void tourelleHorairePendant(long int temps, int pourcentVoltage = 100);
	
	// Faire tourner la tourelle dans le sens antihoraire
	void tourelleAntihoraire(int pourcentVoltage = 100);
	
	// Faire tourner la tourelle dans le sens antihoraire pendant un certain temps (en millisecondes)
	void tourelleAntihorairePendant(long int temps, int pourcentVoltage = 100);
	
	// Arrêter la tourelle si on tourne trop
	void arretUrgence();
	
	// Faire augmenter graduellement le voltage de la tourelle
	void tourelleAccelerer(int sens, int pourcentVoltage = 100);
	
	// Faire diminuer graduellement le voltage de la tourelle
	void tourelleDecelerer(int sens, int pourcentVoltage = 100);
	
	// Arrêter les moteurs de la baliste
	void arreterBaliste();
	
	//Faire tourner les moteurs de la baliste
	void tournerBaliste();
	
	// Faire un tir avec la baliste
	void tirerBaliste();

	private:
	
	int M1, E1, M2, E2, M3, E3, M4, E4;
	int boutonRouge, boutonNoir1, boutonNoir2;
	float voltageBatterie, voltageMoteurRouesTourelle, voltageMoteurBaliste, pourcentMax;

	int limite;
	int angle;

	int sensRotation;
	int voltageRotation;
};

#endif // CHAR_BALISTE_H_INCLUDED
