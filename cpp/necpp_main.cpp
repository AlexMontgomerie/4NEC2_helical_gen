#include <iostream>
using namespace std;

#include "c_geometry.h"
#include "nec_context.h"
#include "nec_exception.h"
#include "nec_radiation_pattern.h"

#define SEG_CONSTANT 100

//structure for our helix
typedef struct {
  nec_float ant_rad;
  nec_float wire_rad;
  nec_float spacing;
  nec_flaot length;
  
} helical_param_t;


//function to create an nec type
nec_context get_antenna(helical_param_t helical_param, int tag_id, )
{
  //variable initialisation
  int seg_count = SEG_CONSTANT * (int) ceil(helical_param.length * 100);

  //create an nec type
  nec_context nec;
  nec.initialize();
  
  //create geometry type  
  c_geometry* geo = nec.get_geometry();
    
  //create first helix
  geo->helix(tag_id,                //tag id
            seg_count,              //segment count
            helical_param.spacing,  //spacing between helix wires
            helical_param.length,   //total length of the helix
            helical_param.ant_rad,  //antenna radius (radius in x at z = 0)
            helical_param.ant_rad,  //antenna radius (radius in y at z = 0)
            helical_param.ant_rad,  //antenna radius (radius in x at z = HL)
            helical_param.ant_rad,  //antenna radius (radius in y at z = HL)
            helical_param.wire_rad  //radius of the wire
            );

  geo->move(
  //finish geometry;
  nec.geometry_complete(0);
    
  nec.gn_card(-1,0,0.0, 0.0, 0.0,0.0, 0.0, 0.0);
  nec.ld_card(5,0,0,0,3.72e7,0.0,0.0);
  nec.pt_card(-1, 0, 0, 0);
  nec.ex_card(EXCITATION_LINEAR, 1, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
  nec.fr_card(0, 2, 2400.0, 100.0);
  nec.rp_card(0, 10, 10, 0,5,0,0, 0.0, 0.0, 9.0, 9.0, 0.0, 0.0);

  //return nec features  
  return nec;
}



int main(int argc, char **argv) {
  try {
    cout << "Nec2++ C++ example. Running (takes a few minutes...)" << endl;
    
    nec_context nec;
    nec.initialize();
    
    c_geometry* geo = nec.get_geometry();
    geo->wire(0, 70, -0.048, 0.021, -0.005, 0.035, 0.043, 0.014, 0.001, 1.0, 1.0);
    geo->wire(0, 66, 0.017, -0.015, 0.014, -0.027, 0.04, -0.031, 0.001, 1.0, 1.0);
    geo->wire(0, 47, 0.046, -0.01, 0.028, -0.013, -0.005, 0.031, 0.001, 1.0, 1.0);
    geo->wire(0, 77, -0.048, -0.038, -0.04, 0.049, -0.045, -0.04, 0.001, 1.0, 1.0);
    nec.geometry_complete(0);
    
    nec.gn_card(-1,0,0.0, 0.0, 0.0,0.0, 0.0, 0.0);
    nec.ld_card(5,0,0,0,3.72e7,0.0,0.0);
    nec.pt_card(-1, 0, 0, 0);
    nec.ex_card(EXCITATION_LINEAR, 1, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    nec.fr_card(0, 2, 2400.0, 100.0);
    nec.rp_card(0, 10, 10, 0,5,0,0, 0.0, 0.0, 9.0, 9.0, 0.0, 0.0);
    
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
