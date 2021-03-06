# The following comments couldn't be translated into the new config version:

# Database output service

import FWCore.ParameterSet.Config as cms

process = cms.Process("ProcessOne")
#PopCon config
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = cms.string("sqlite_file:DBGasGainCorrection_test.db")
#process.CondDBCommon.connect = cms.string("oracle://cms_orcoff_prep/CMS_COND_CSC")
process.CondDBCommon.DBParameters.authenticationPath = '/afs/cern.ch/cms/DB/conddb'

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    destinations = cms.untracked.vstring('cout')
)

process.source = cms.Source("EmptyIOVSource",
    lastValue = cms.uint64(1),
    timetype = cms.string('runnumber'),
    #change the firstRun if you want a different IOV
    firstValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    logconnect = cms.untracked.string('sqlite_file:gainslog.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('CSCDBGasGainCorrectionRcd'),
        tag = cms.string('CSCDBGasGainCorrection_data') 
        #tag = cms.string('CSCDBGasGainCorrection_MC') 
    ))
)

process.WriteGasGainCorrectionWithPopCon = cms.EDAnalyzer("CSCDBGasGainCorrectionPopConAnalyzer",
    SinceAppendMode = cms.bool(True),
    record = cms.string('CSCDBGasGainCorrectionRcd'),
    loggingOn = cms.untracked.bool(True),
    Source = cms.PSet(
         dataCorrFileName= cms.untracked.string("/afs/cern.ch/user/r/rakness/scratch0/CMSSW_4_4_0_pre1/src/CalibMuon/CSCCalibration/test/gains_per_gas_gain_sector_allcorrected_newformat.dat"),
         isForMC = cms.untracked.bool(False)
    )
)

process.p = cms.Path(process.WriteGasGainCorrectionWithPopCon)
#process.CondDBCommon.connect = 'oracle://cms_orcoff_prep/CMS_COND_CSC'



