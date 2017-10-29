#include <iostream>
#include <string>
#include <fstream>
#include <unistd.h>
using namespace std;

#include "c_geometry.h"
#include "nec_context.h"
#include "nec_exception.h"
#include "nec_radiation_pattern.h"

nec_context parse_nec_card(char * file_name) 
{
  nec_context nec;
  nec.initialize();

  //open file, so
  //FILE* file = fopen(file_name, 'r');  

  c_geometry g = new c_geometry();
  g.parse_geometry(file);
}

int main(int argc, char **argv) {

  char in_file_name = NULL;
  char out_file_name = NULL;
  
  //argument parser 
  while ((c = getopt(argc, argv, "i:o:")) != -1)
    switch (c) {
      case 'i':
        in_file_name = optarg;
        break;

      case 'o':
        out_file_name = optarg;
        break;

      default:
        break;
    }

  try {

    //parse NEC card
    nec_context nec = parse_nec_card(in_file_name);

    // now get the radiation pattern data. The result index is 0 since
    // this is the first (and only) radiation pattern.
    nec_radiation_pattern* rp = nec.get_radiation_pattern(0);

    int nth = rp->get_ntheta();
    int nph = rp->get_nphi();
    
    //redireting output to out.txt
    ofstream out("out.txt");
    streambuf *coutbuf = std::cout.rdbuf(); //keep the old buff
    //What does that mean? idk but it works!
    cout.rdbuf(out.rdbuf());//now actually redirect
    cout << "Theta,\tPhi,\tHorizontal Power Gain,\tVertical Power Gain,\tTotal Power Gain,\tetheta_magnitude,\tetheta_phase,\tephi_magnitude,\tephi_phase" << endl;
    for (int j=0; j<nph; j++) {
      for (int i=0; i<nth; i++) {
        cout
          << rp->get_theta(i) << ",\t"
          << rp->get_phi(j) << "  ,\t"
          << rp->get_power_gain_horiz(i,j) << "  ,\t"
          << rp->get_power_gain_vert(i,j) << "  ,\t"
          << rp->get_power_gain(i,j) << "  ,\t"
          << rp->get_etheta_magnitude(i,j) << "  ,\t"
          << rp->get_etheta_phase(i,j) << "  ,\t"
          << rp->get_ephi_magnitude(i,j) << "  ,\t"
          << rp->get_ephi_phase(i,j)
          << endl;
      }
    }
  }
  catch (nec_exception* e) {
    //probably should do something
  }
  return 0;
}
