//
// Copyright 2018-2019 Manuel Barrette
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
// Dernière modification : 16 octobre 2018
//
/*****************************************************************************/

#include "char_baliste.h"
#include "Arduino.h"

using namespace std;

// Constructeur
Baliste::Baliste()
{
	voltageBatterie = 6; // À modifier selon la batterie
	voltageMoteurRouesTourelle = 4; // À modifier selon le moteur
	voltageMoteurBaliste = 4; // À modifier selon le moteur

	pourcentMax = voltageMoteurRouesTourelle/voltageBatterie;

	// Numéro des pins connectées aux moteurs (servent dans tout le programme)

	// Le moteur 1 est utilisé pour les roues.
	M1 = 4;
	E1 = 5;

	// Le moteur 2 est utilisé pour la tourelle.
	M2 = 2;
	E2 = 3;

	// Les moteurs 3 et 4 sont utilisés pour la baliste.
	M3 = 12;
	E3 = 10;
	M4 = 13;
	E4 = 11;

	// Les boutons sont connectés aux pins 6 à 8
	boutonRouge = 7;
	boutonNoir1 = 6;
	boutonNoir2 = 8;

	limite = 3*50000*40/1000;
	angle = 0;

	sensRotation = 1;
	voltageRotation = 0;

	pinMode(M1,OUTPUT);
	pinMode(M2,OUTPUT);
	pinMode(M3,OUTPUT);
	pinMode(M4,OUTPUT);
	pinMode(boutonRouge,INPUT_PULLUP);
	pinMode(boutonNoir1,INPUT_PULLUP);
	pinMode(boutonNoir2,INPUT_PULLUP);
}

// Destructeur
Baliste::~Baliste()
{

}

// Obtenir la valeur de l'angle de rotation
int Baliste::getAngle() const
{
	return angle;
}

// Obtenir la valeur de la limite de rotation permise
int Baliste::getLimite() const
{
	return limite;
}

//Obtenir la valeur des pins des moteurs
int Baliste::getM1() const
{
	return M1;
}

int Baliste::getM2() const
{
	return M2;
}

int Baliste::getM3() const
{
	return M3;
}

int Baliste::getM4() const
{
	return M4;
}

// Obtenir la valeur des pins des boutons
int Baliste::getBoutonRouge() const
{
	return boutonRouge;
}

int Baliste::getBoutonNoir1() const
{
	return boutonNoir1;
}

int Baliste::getBoutonNoir2() const
{
	return boutonNoir2;
}

int Baliste::conversionPourcent(int pourcentVoltage)
{
	// Convertir un pourcentage en base 255
	int pourcent = pourcentVoltage*pourcentMax; // Pour ne pas dépasser pourcentMax
	int voltage = pourcent*255/100;
	if (voltage < 0)
	{
		return -1;
	}
	else if (voltage > pourcentMax*255)
	{
		return -1;
	}
	else
	{
		return voltage;
	}
}

void Baliste::attendrePendant(unsigned long temps)
{
	int tempsActuel = 0;
	int pas = 50;
	while(tempsActuel <= temps)
	{
		if (getAngle() <= getLimite() and getAngle() >= -getLimite())
		{
			delay(pas);
			angle += sensRotation*pas*voltageRotation/100;
		}
		else
		{
			arretUrgence();
		}
		tempsActuel += pas;
	}
}

/*****************************************************************************/
//
// Actions des roues
//


void Baliste::arreter()
{
	// Arrêter les roues
	analogWrite(E1, 0);
}

void Baliste::avancer(int pourcentVoltage)
{
	// Faire avancer les roues
	int voltage = conversionPourcent(pourcentVoltage);
	if(voltage == -1)
	{
		return;
	}
	digitalWrite(M1, HIGH);
	analogWrite(E1, voltage);
}


void Baliste::avancerPendant(long int temps, int pourcentVoltage)
{
	// Avancer pendant un certain temps (en millisecondes)
	accelerer(1, pourcentVoltage);
	avancer(pourcentVoltage);
	attendrePendant(temps - 1000);
	decelerer(1, pourcentVoltage);
	arreter();
}


void Baliste::reculer(int pourcentVoltage)
{
	// Faire reculer les roues
	int voltage = conversionPourcent(pourcentVoltage);
	if(voltage == -1)
	{
		return;
	}
	digitalWrite(M1, LOW);
	analogWrite(E1, voltage);
}


void Baliste::reculerPendant(long int temps, int pourcentVoltage)
{
	// Reculer pendant un certain temps (en millisecondes)
	accelerer(-1, pourcentVoltage);
	reculer(pourcentVoltage);
	attendrePendant(temps - 1000);
	decelerer(-1, pourcentVoltage);
	arreter();
}


void Baliste::accelerer(int sens, int pourcentVoltage)
{
	// Accélérer de façon graduelle sur une seconde
	int nb = 5;
	if (sens == 1)
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    avancer(pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
	else
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    reculer(pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
}


void Baliste::decelerer(int sens, int pourcentVoltage)
{
	// Décélerer de façon graduelle sur une seconde
	int nb = 5;
	if (sens == 1)
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    avancer(pourcentVoltage*(1 - i/nb));
	    attendrePendant(100);
	  }
	}
	else
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    reculer(pourcentVoltage - pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
}

/*****************************************************************************/
//
// Actions de la tourelle
//

void Baliste::arreterTourelle()
{
	// Arrêter le mouvement de la tourelle
	analogWrite(E2, 0);
}


void Baliste::tourelleHoraire(int pourcentVoltage)
{
	// Faire tourner la tourelle dans le sens horaire
	int voltage = conversionPourcent(pourcentVoltage);
	if(voltage == -1)
	{
	  return;
	}
	digitalWrite(M2, LOW);
	analogWrite(E2, voltage);
	sensRotation = 1;
	voltageRotation = pourcentVoltage;
}


void Baliste::tourelleHorairePendant(long int temps, int pourcentVoltage)
{
	// Faire tourner la tourelle dans le sens antihoraire pendant un certain temps (en millisecondes)
	tourelleAccelerer(1, pourcentVoltage);
	tourelleHoraire(pourcentVoltage);
	attendrePendant(temps-1000);
	tourelleDecelerer(1, pourcentVoltage);
	arreterTourelle();
}


void Baliste::tourelleAntihoraire(int pourcentVoltage)
{
	// Faire tourner la tourelle dans le sens antihoraire
	int voltage = conversionPourcent(pourcentVoltage);
	if(voltage == -1)
	{
	  return;
	}
	digitalWrite(M2, HIGH);
	analogWrite(E2, voltage);
	sensRotation = -1;
	voltageRotation = pourcentVoltage;
}


void Baliste::tourelleAntihorairePendant(long int temps, int pourcentVoltage)
{
	// Faire tourner la tourelle dans le sens antihoraire pendant un certain temps (en millisecondes)
	tourelleAccelerer(-1, pourcentVoltage);
	tourelleAntihoraire(pourcentVoltage);
	attendrePendant(temps-1000);
	tourelleDecelerer(-1, pourcentVoltage);
	arreterTourelle();
}


void Baliste::arretUrgence()
{
	// Arrêter le mouvement de la tourelle si elle tourne trop loin
	arreterTourelle();
	delay(2000);
	if (getAngle() >= 0)
	{
	  tourelleAntihoraire(50);
	  delay(getAngle()*2);
	  arreterTourelle();
	}
	else
	{
	  tourelleHoraire(50);
	  delay(-getAngle()*2-2000);
	  arreterTourelle();
	}
	angle = 0;
	exit(0);
}

/*
void Baliste::arretUrgenceGauche()
{
  // Arrêter le mouvement de la tourelle si elle vient appuyer sur le bouton de gauche
  arreterTourelle();
  attendrePendant(1000);
  tourelleHorairePendant(1000); // Ajuster selon les tests
  exit(0);
}
*/

void Baliste::tourelleAccelerer(int sens, int pourcentVoltage)
{
	// Accélérer de façon graduelle sur une demi-seconde
	int nb = 5;
	if (sens == 1)
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    tourelleHoraire(pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
	else
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    tourelleAntihoraire(pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
}


void Baliste::tourelleDecelerer(int sens, int pourcentVoltage)
{
	// Décélerer de façon graduelle sur une demi-seconde
	int nb = 5;
	if (sens == 1)
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    tourelleHoraire(pourcentVoltage*(1 - i/nb));
	    attendrePendant(100);
	  }
	}
	else
	{
	  for (int i = 1; i <= nb; i++)
	  {
	    tourelleAntihoraire(pourcentVoltage - pourcentVoltage*i/nb);
	    attendrePendant(100);
	  }
	}
}


//void Baliste::tourelleAntihorairePendant(long int temps)
//{
//	// Faire tourner la tourelle dans le sens antihoraire pendant un certain temps (en millisecondes)
//	tourelleAntihoraire();
//	attendrePendant(temps);
//	arreterTourelle();
//}


//void Baliste::tourelleHorairePendant(long int temps)
//{
//	// Faire tourner la tourelle dans le sens horaire pendant un certain temps (en millisecondes)
//	tourelleHoraire();
//	attendrePendant(temps);
//	arreterTourelle();
//}





/*****************************************************************************/
//
// Actions de la baliste
//

void Baliste::arreterBaliste()
{
	// Arrêter les moteurs de la baliste
	analogWrite(E3, 0);
	analogWrite(E4, 0);
}


void Baliste::tournerBaliste()
{
	// Faire tirer à volonté la baliste
	//  int voltage = 255*pourcentMax;
	int voltage = 213;
	digitalWrite(M3, LOW);
	digitalWrite(M4, LOW);
	analogWrite(E3, voltage);
	analogWrite(E4, voltage);
}


void Baliste::tirerBaliste()
{
	// Faire un tir avec la baliste
	tournerBaliste();
	attendrePendant(5000); // 2 tirs 5 volts!
	arreterBaliste();
}
