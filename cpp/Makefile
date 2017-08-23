#####################################################################################
#
#	Makefile showing how to use libnecpp, the library
#	version of nec++. This lets you incorporate NEC2
#	antenna electromagnetic modeling into your own programs
#
#	Copyright (C) 2004-2005, 2015  Timothy C.A. Molteno
#	
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#	
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

LD_LIBRARY_PATH=/usr/lib/atlas-base/atlas solve
# TEST_LIBRARY_PATH=../lib
# ./configure  --prefix=`pwd` --with-bounds

#####################################################################################
#
#	The target below shows how to compile and use the nec2++ codebase
#	from within other C++ programs (GPL compatable of course!)
#

NECPP_SRC = ${NECPP_SRC_PATH}/c_ggrid.cpp \
            ${NECPP_SRC_PATH}/matrix_algebra.cpp \
            ${NECPP_SRC_PATH}/nec_ground.cpp \
            ${NECPP_SRC_PATH}/c_evlcom.cpp \
            ${NECPP_SRC_PATH}/c_plot_card.cpp \
            ${NECPP_SRC_PATH}/misc.cpp \
            ${NECPP_SRC_PATH}/nec_context.cpp \
            ${NECPP_SRC_PATH}/nec_output.cpp \
            ${NECPP_SRC_PATH}/c_geometry.cpp \
            ${NECPP_SRC_PATH}/nec_exception.cpp \
            ${NECPP_SRC_PATH}/nec_radiation_pattern.cpp \
	    ${NECPP_SRC_PATH}/nec_structure_currents.cpp \
            ${NECPP_SRC_PATH}/electromag.cpp \
            ${NECPP_SRC_PATH}/nec_results.cpp

NECPP_OBJS = $(NECPP_SRC:.cpp=.o)

CPP_SRC  = necpp_main.cpp
CPP_OBJS = $(CPP_SRC:.cpp=.o)

CXXFLAGS=-I ${NECPP_SRC_PATH} -I .. -O2 -Wall


helix: ${CPP_OBJS} ${NECPP_OBJS}
	gcc -g  -o helix ${CPP_OBJS} ${NECPP_OBJS} -lstdc++ -lm -llapack
	./helix

cpp_clean:
	rm -f ${CPP_OBJS} ${NECPP_OBJS} 

clean: #cpp_clean
	rm -f helix
