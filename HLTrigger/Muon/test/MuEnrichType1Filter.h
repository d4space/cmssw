#ifndef MuEnrichFltr_h
#define MuEnrichFltr_h
//
// class declaration
//
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class MuEnrichType1Filter : public edm::EDFilter {
public:
  explicit MuEnrichType1Filter(const edm::ParameterSet&);
  ~MuEnrichType1Filter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  int nrejected;
  int naccepted;
  int type;
      // ----------member data ---------------------------
};

#endif

