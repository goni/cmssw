import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring( 
'/store/user/anstahll/TriggerStudy2016/MC/ZMuMu_Pythia8_5p02TeV_TuneCUETP8M1_RECO_20160725/ZMuMuPythia8/ZMuMu_Pythia8_5p02TeV_TuneCUETP8M1_RECO_20160725/160725_195230/0000/step4_ZMuMu_Pythia8_5p02TeV_TuneCUETP8M1_RAW2DIGI_L1Reco_RECO_1.root'
    )
)

process.load("DQM.HLTEvF.HLTObjectMonitor_cfi")

process.hltObjectMonitor.processName = cms.string("TEST")

process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.hltObjectMonitor*process.dqmOutput )
