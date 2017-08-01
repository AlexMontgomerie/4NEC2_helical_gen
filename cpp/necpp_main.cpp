#include <iostream>
using namespace std;

#include "c_geometry.h"
#include "nec_context.h"
#include "nec_exception.h"
#include "nec_radiation_pattern.h"

#define SEG_CONSTANT 100
#define CONDUCTIVITY 3.72e7

//structure for our helix
typedef struct {
  
  nec_float ant_rad;
  nec_float wire_rad;
  nec_float spacing;
  nec_float length;
  
} helix_param_t;


//function to create an nec type
nec_context get_antenna(helix_param_t helix_param, int tag_id)
{
  //variable initialisation
  int seg_count = (int) ceil(helix_param.length * 100 * SEG_CONSTANT);

  //create an nec type
  nec_context nec;
  nec.initialize();
  
  //create geometry type  
  c_geometry* geo = nec.get_geometry();
    
  //create first helix
  geo->helix(tag_id,              //tag id
            seg_count,            //segment count
            helix_param.spacing,  //spacing between helix wires
            helix_param.length,   //total length of the helix
            helix_param.ant_rad,  //antenna radius (radius in x at z = 0)
            helix_param.ant_rad,  //antenna radius (radius in y at z = 0)
            helix_param.ant_rad,  //antenna radius (radius in x at z = HL)
            helix_param.ant_rad,  //antenna radius (radius in y at z = HL)
            helix_param.wire_rad  //radius of the wire
            );
  
  //create second helix (rotated by 180 degrees)
  geo->move(0,    //rotation in x
            0,    //rotation in y
            180,  //rotation in z
            0,    //translation in x
            0,    //translation in y
            0,    //translation in z
            0,    //its : specify segments to be moved
            1,    //nrpt: number of new structures to be generated
            0     //itgi: segment incriment
            );

  //finish geometry;
  nec.geometry_complete(0);
  
  //ground plane card (no ground plane)    
  nec.gn_card(-1,
              0,
              0.0,
              0.0, 
              0.0,
              0.0, 
              0.0, 
              0.0
              );
  
  //loading card
  nec.ld_card(5,            //type of loading (wire conductivity)
              0,            //tag number for wire section to be loaded
              0,            //number of segments to be loaded
              0,            //end segment to be loaded
              CONDUCTIVITY, //wire conductivity
              0.0,          //(unused)
              0.0           //(unused)
              );      
  //printing card
  nec.pt_card(-1, //print control (supress current printing) 
              0,  //number of segments to be printed
              0,  
              0
              );
  
  //excitation card
  nec.ex_card(EXCITATION_LINEAR, //
              1, 
              1, 
              0, 
              0.0, 
              0.0,
              0.0, 
              0.0, 
              0.0, 
              0.0
              );
  

  nec.fr_card(0, 
              2, 
              2400.0, 
              100.0
              );
  

  nec.rp_card(0, 10, 10, 0,5,0,0, 0.0, 0.0, 9.0, 9.0, 0.0, 0.0);

  //return nec features  
  return nec;
}



int main(int argc, char **argv) {
  try {
    cout << "Nec2++ C++ example. Running (takes a few minutes...)" << endl;
    
    helix_param_t helix_param;

    helix_param.ant_rad   = 0.05;
    helix_param.wire_rad  = 0.001;
    helix_param.spacing   = 0.01;
    helix_param.length    = 0.1;

    //get the nec info for helix
    nec_context nec = get_antenna(helix_param, 0);

    // now get the radiation pattern data. The result index is 0 since
    // this is the first (and only) radiation pattern.
    nec_radiation_pattern* rp = nec.get_radiation_pattern(0);
    
    int nth = rp->get_ntheta();
    int nph = rp->get_nphi();
    
    cout << endl << "Theta \tPhi \tHorizontal \tVertical \tTotal" << endl;
    for (int j=0; j<nph; j++) {
      for (int i=0; i<nth; i++) {
        cout
          << rp->get_theta(i) << "  \t" 
          << rp->get_phi(j) << "  \t" 
          << rp->get_power_gain_horiz(i,j) << "  \t" 
          << rp->get_power_gain_vert(i,j) << "  \t" 
          << rp->get_power_gain(i,j) << "  \t"
          << rp->get_etheta_magnitude(i,j) << "  \t"
          << rp->get_etheta_phase(i,j) << "  \t"
          << rp->get_ephi_magnitude(i,j) << "  \t"
          << rp->get_ephi_phase(i,j)
          << endl;
      }
    }
  }
  catch (nec_exception* e) {
    cout << e->get_message() << endl;
  }
  return 0;
}
