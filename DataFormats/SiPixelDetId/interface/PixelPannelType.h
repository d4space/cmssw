#ifndef DataFormats_SiPixelDetId_PixelPannelType_H
#define DataFormats_SiPixelDetId_PixelPannelType_H

#include "DataFormats/SiPixelDetId/interface/PixelEndcapName.h"

class PixelPannelType {
public:
  enum PannelType { p3L, p3R, p4L, p4R };

  static PannelType pannelType( const PixelEndcapName & name) {
    PannelType type = (name.pannelName()==1) ? p4L : p3L;
    return type;
  } 
};

#endif
