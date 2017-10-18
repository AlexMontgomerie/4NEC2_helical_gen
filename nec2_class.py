"""
Classes to implimented
  - EK (maybe?)
  - EN
  - EX
  - FR
  - GE
  - GH
  - GN
  - GD
  - GS
  - LD
  - PQ
  - RP

"""

class EN:
  """
  To indicate to the program the end of all execution
  Refer to http://www.nec2.org/part_3/cards/en.html for more information
  """
  def __init__(self):
    self.EN_out = "EN"

  def explain(self):
    pass

  def construct(self):
    return self.EN_out

  def validate(self):
    pass


class GE:
  """
  terminate reading of geometry data cards and reset geometry if
  a ground plane is used
  GPflag:
    * 0   - no ground plane present
    * 1   - ground plane present (wire touching ground is interpolated
    * -1  - ground plane present (segments touching ground go to zero)
  Refer to http://www.nec2.org/part_3/cards/ge.html for more information
  """
  def __init__(self, gpflag=0):
    self.gpflag = gpflag
    self.GE_out = "GE"

  def construct(self):
    self.GE_out = "GE " + gpflag + "\n"

  def validate(self):
    if not isinstance(gpflag, int):
      raise ValueError('GE: gpflag must be an integer')

    if !(gpflag >= -1 or gpflag <= 1):
      raise ValueError('GE: gpflag out of bounds')


class GH:
  """
  Purpose to generate helix or spiral of wire segments
  ITG: tag number assigned to all segments of the helix/spiral
  NS: number of segments into which the helix/spiral is divided
  S: Spacing between turns
  HL: Total length of the helix
  A1: radius in x at z = 0
  B1: radius in y at z = 0
  A2: radius in x at z = HL
  B2: radius in y at z = HL
  RAD: Radius of the wire

  Note,
    Structure is a helix if A2 = A1 and HL > 0
    Structure is a spiral if A2 = A1 and HL = 0
    HL > 0 gives right-handed helix
    HL < 0 gives left-handed helix

  Refer to http://www.nec2.org/part_3/cards/gh.html for more information
  """
  def __init__(self,ITG=0,NS=0,S=0,HL=0,A1=0,B1=0,A2=0,B2=0,RAD=0):
    self.ITG  = ITG
    self.NS   = NS
    self.S    = S
    self.HL   = HL
    self.A1   = A1
    self.B1   = B1
    self.A2   = A2
    self.B2   = B2
    self.RAD  = RAD

    self.GH_out = "GH"

  def explain(self):
    pass

  def construct(self):
    self.GH_out = "GH " + self.ITG + " " + self.NS + " " + self.S + " " + \
    self.HL + " " + self.A1 + " " + self.B1 + " " + self.A2 + " " + self.B2 + " " + self.RAD + "\n"

    return self.GH_out

  def get_pitch(self):
    #TODO: calculate pitch as a function of the other parameters
    pitch = None
    return pitch

  def get_spacing(self):
    #TODO: calculate spacing between wires as function of parameters
    spacing = None
    return spacing

  def validate(self):
    #check that they are of the right type (at least ITG and NS are > 0 and integers)
    if not isinstance(self.ITG, int):
      raise ValueError('GH: ITG must be an integer')
    if not isinstance(self.NS, int):
      raise ValueError('GH: NS must be an integer')
    #check rad > 0
    if self.RAD <= 0:
      raise ValueError('GH: wire radius must be larger than 0')


class GN:
  """
  specify the ground plane parameters
  IPERF: ground type flag
    * -1  - nullifies previous ground parameters (remainder must be blank)
    * 0   - finite ground, reflection coefficient approximation
    * 1   - perfectly conductig ground
    * 2   - finite ground, Sommerfield/Norton method
  NRADL: number of radial wires in ground plane screen
  EPSE: dielectric constant for ground (in antenna vicintity)
  SIG: conductivity of ground (in antenna vicintity)

  """
  def __init__(self):
    pass

  def explain(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass

class GD:
  """

  """
  def __init__(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass


class GS:
  """

  """
  def __init__(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass


class LD:
  """

  """
  def __init__(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass


class PQ:
  """

  """
  def __init__(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass


class CM:
  """
  The CM class is used to comment the calculations, it has one attribute: the comment text.
  A CM class is required for each input file.
  """
  def __init__(self, comment):
    self.comment = comment
    self.CM_out = None

  def explain(self):
    pass

  def construct(self):
    """ This writes the appropriate line in the .nec file"""
    self.CM_out = "CM " + self.comment + "\n"
    #Should we just return that string instead of creating a new prop?

  def validate(self):
    pass


#TODO: this might only be for 4nec2, so maybe not have it?
class SY:
  """

  """
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def explain(self):
    pass

  def construct(self):
    pass
    #TODO: construct the SY type

  def validate(self):
    pass


class GW:
  """
  The GW class defines a strait wire. A (GW) segment has the folowing properties:
      -start_x, start_y, start_z The coordinates of the start point (float)
    -end_x, end_y, end_z The coordinates of the end point of the segment (float)
    -wire_num an ID for the wire (int)
    -wire_seg ??
    -radius physical radius of the wire (float)
  Refer to http://www.nec2.org/part_3/cards/gw.html for more information
  """

  def __init__(self, wire_num, wire_seg, start, end, radius):
    self.wire_num = wire_num
    self.wire_seg = wire_seg
    self.radius = radius

    self.start_x = start[0]
    self.start_y = start[1]
    self.start_z = start[2]

    self.end_x = end[0]
    self.end_y = end[1]
    self.end_z = end[2]

  def explain(self):

  def construct(self):
    pass

  def validate(self):
    pass


class LD:
  """

  """
  def __init__(self):
    pass

  def explain(self):

  def construct(self):
    pass

  def validate(self):
    pass


class EX:
  """

  """
  def __init__(self):
    pass

  def explain(self):
    pass

  def construct(self):
    pass

  def validate(self):
    pass


class FR:
  """
  The FR class describes the frequencies used for the analysis,
  it has the folowing properties:
    - frequency, the first frequency considered in MHz (float)
    - increment, size of steps in MHz or noUnits when sweeping
        a frequency domain (float)
    - nsteps, number of steps considered (default 1) (int)
    - incType, type of incrementation: (int)
        + 0 : linear, frequency incremented by self.increment at each step
        + 1 : logarithmic frequency multiplied by self.increment at each step
  More information at: http://www.nec2.org/part_3/cards/fr.html
  """
  def __init__(self, frequency = 298.8):
    #define single frequency analysis as default case
    self.frequency = frequency
    self.increment = 0. #MHz
    self.nsteps = 1
    self.incType = 0

  def withLinSpace(self, increment = 0., nsteps = 1):
    """ To define a linear incrementation. Give increment in MHz"""
    self.increment = increment
    self.nsteps = nsteps
    self.incType = 0

  def withLogSpace(self, increment = 1.,nsteps = 1):
    """ To define a logarithmic incrementation. Give increment without units """
    self.increment = increment
    self.nsteps = nsteps
    self.incType = 1

  def explain(self):
    """Provides some details on the current FR definition, for debug"""
    strFreq1 = str(self.frequency)
    if self.nsteps == 1:
        print('Describing single frequency analysis at ', strFreq1, ' MHz')
    elif self.incType == 0:
        strFreq2 = str(self.frequency + self.increment*(self.nsteps - 1))
        print('Sweeping linear domain from ', strFreq1, ' to ', strFreq2,' MHz using ', str(self.nsteps), ' steps')
    elif self.incType == 1:
        strFreq2 = str(self.frequency*(self.increment**(self.nsteps - 1)))
        print('Sweeping log domain from ', strFreq1, ' to ', strFreq2,' MHz using ', str(self.nsteps), ' steps')

  def construct(self):
    pass

  def validate(self):
    pass
