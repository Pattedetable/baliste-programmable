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


#include "char_baliste.h"
#include "instructions.h"

void loop() {
	// Code qui se répète en boucle

	Baliste baliste;

	int bouton = 0;
	
	// Choix de la séquence avec les boutons
	// Connecter un côté du bouton au ground et l'autre à une pin
	
	  while (bouton == 0)
	  {
	  	if (digitalRead(baliste.getBoutonNoir1()) == LOW) // Selon documentation, LOW = enfoncé, HIGH = pas enfoncé
	  	{
	    	bouton = 1;
	    }
	    else if (digitalRead(baliste.getBoutonRouge()) == LOW)
	    {
	      bouton = 2;
	     }
	    else if (digitalRead(baliste.getBoutonNoir2()) == LOW)
	    {
	      bouton = 3;
	    }
	  }
	
	// Écrire les instructions plus bas
	
	
	// Séquence pour le défi
	
	if (bouton == 1)
	{
	baliste.attendrePendant(2000); // Délai de 2 secondes
	baliste.avancerPendant(7000, 75);
	baliste.tourelleHorairePendant(6200, 40);
	baliste.tirerBaliste();
	baliste.avancerPendant(13000, 75);
	baliste.tirerBaliste();
	baliste.tourelleAntihorairePendant(7000, 40);
	baliste.reculerPendant(6500, 80);
	baliste.tourelleHorairePendant(6200, 40);
	baliste.tirerBaliste();
	baliste.tourelleAntihorairePendant(7000, 40);
	baliste.reculerPendant(13000, 80);
	}
	
	
	// Séquence de Gatling
	
	if (bouton == 2)
	{
	//baliste.attendrePendant(2000); // Délai de 2 secondes
	//baliste.avancer(75);
	//baliste.attendrePendant(500);
	//baliste.tourelleHoraire(40);
	//baliste.tournerBaliste();
	//baliste.attendrePendant(5000);
	//baliste.arreterTourelle();
	//baliste.tourelleAntihoraire(40);
	//baliste.attendrePendant(10000);
	//baliste.arreterTourelle();
	//baliste.tourelleHoraire(40);
	//baliste.attendrePendant(4500);
	//baliste.arreterTourelle();
	//baliste.arreterBaliste();
	//baliste.attendrePendant(1000);
	//baliste.arreter();
	instructions(baliste);
	}
	
	
	// Faire tirer la baliste à volonté
	
	if (bouton == 3)
	{
	  baliste.tournerBaliste();
	  while (digitalRead(baliste.getBoutonNoir2()) == LOW)
	  {
	
	  }
	  baliste.arreterBaliste();
	}
	delete &baliste;
	
	baliste.attendrePendant(1000);

}


void setup() {
	// Code qui ne sera utilisé qu'une seule fois

  
}

