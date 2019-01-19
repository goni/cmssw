import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing


#----------------------------------------------------------------------------

# Setup Settings for ONIA TREE: PbPb 2018

HLTProcess     = "HLT" # Name of HLT process 
isMC           = False # if input is MONTECARLO: True or if it's DATA: False
muonSelection  = "Glb" # Single muon selection: Glb(isGlobal), GlbTrk(isGlobal&&isTracker), Trk(isTracker) are availale
applyEventSel  = True  # Only apply Event Selection if the required collections are present
#############################################################################
keepExtraColl  = False # General Tracks + Stand Alone Muons + Converted Photon collections
saveHLTBit     = False # for trigger analysis
saveHLTobj     = False # For trigger analysis

#----------------------------------------------------------------------------

# Print Onia Tree settings:
print( " " )
print( "[INFO] Settings used for ONIA TREE: " )
print( "[INFO] isMC          = " + ("True" if isMC else "False") )
print( "[INFO] applyEventSel = " + ("True" if applyEventSel else "False") )
print( "[INFO] keepExtraColl = " + ("True" if keepExtraColl else "False") )
print( "[INFO] muonSelection = " + muonSelection )
print( " " )

# set up process
process = cms.Process("HIOnia")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# Input and Output File Names
options.outputFile = "Oniatree.root"
options.secondaryOutputFile = "Jpsi_DataSet.root"
options.inputFiles =[
    '/store/hidata/HIRun2018A/HIDoubleMuon/AOD/PromptReco-v1/000/326/483/00000/901AFDEE-00C0-3242-A7DF-90885EC50A1E.root'
]
options.maxEvents = -1 # -1 means all events

# Get and parse the command line arguments
options.parseArguments()

triggerList    = {
		# Double Muon Trigger List
		'DoubleMuonTrigger' : cms.vstring(
			"HLT_HIL1DoubleMuOpen_v1",#0 
			"HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v1", #1
			"HLT_HIL1DoubleMuOpen_Centrality_50_100_v1", #2
			"HLT_HIL1DoubleMu10_v1", #3
			"HLT_HIL2_L1DoubleMu10_v1",#4
			"HLT_HIL3_L1DoubleMu10_v1", #5
			"HLT_HIL2DoubleMuOpen_v1", #6
			"HLT_HIL3DoubleMuOpen_v1", #7
			"HLT_HIL3DoubleMuOpen_M60120_v1", #8
			"HLT_HIL3DoubleMuOpen_JpsiPsi_v1", #9
			"HLT_HIL3DoubleMuOpen_Upsi_v1", #10
			"HLT_HIL3Mu0_L2Mu0_v1", #11
			"HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1",#12
			"HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v1",#13
			"HLT_HIL3Mu3_L1TripleMuOpen_v1"#14
                        ),
		# Double Muon Filter List
		'DoubleMuonFilter'  : cms.vstring(
			"hltL1fL1sL1DoubleMuOpenL1Filtered0",
			"hltL1fL1sL1DoubleMuOpenOSCentrality40100L1Filtered0",
			"hltL1fL1sL1DoubleMuOpenCentrality50100L1Filtered0",
			"hltL1fL1sL1DoubleMu10L1Filtered0",
			"hltL2fL1sL1DoubleMu10L1f0L2Filtered0",
			"hltDoubleMuOpenL1DoubleMu10Filtered",
			"hltL2fL1sL1DoubleMuOpenL1f0L2Filtered0",
			"hltL3fL1DoubleMuOpenL3Filtered0",
			"hltL3fL1DoubleMuOpenL3FilteredM60120",
			"hltL3fL1DoubleMuOpenL3FilteredPsi",
			"hltL3fL1DoubleMuOpenL3FilteredUpsi",
			"hltL3f0L3Mu0L2Mu0Filtered0",
                        "hltL3f0L3Mu0L2Mu0DR3p5FilteredNHitQ10M1to5",
			"hltL3f0L3Mu2p5NHitQ10L2Mu2FilteredM7toinf",
                        "hltL3fL1sL1DoubleMuOpenL1fN3L2f0L3Filtered3"
			),
                # Single Muon Trigger List
                'SingleMuonTrigger' : cms.vstring(
                        "HLT_HIL1MuOpen_Centrality_70_100_v1",
                        "HLT_HIL1MuOpen_Centrality_80_100_v1",
                        "HLT_HIL2Mu3_NHitQ15_v1",
                        "HLT_HIL2Mu5_NHitQ15_v1",
                        "HLT_HIL2Mu7_NHitQ15_v1",
                        "HLT_HIL3Mu3_NHitQ10_v1",
                        "HLT_HIL3Mu5_NHitQ10_v1",
                        "HLT_HIL3Mu7_NHitQ10_v1",
                        "HLT_HIL3Mu12_v1",
                        "HLT_HIL3Mu15_v1",
                        "HLT_HIL3Mu20_v1",
			),
	        # Single Muon Filter List
	        'SingleMuonFilter'  : cms.vstring(
                        "hltL1fL1sL1MuOpenCentrality70100L1Filtered0",
                        "hltL1fL1sL1MuOpenCentrality80100L1Filtered0",
                        "hltL2fL1sMu3OpenL1f0L2Filtered3NHitQ15",
                        "hltL2fL1sMu3OpenL1f0L2Filtered5NHitQ15",
                        "hltL2fL1sMu3OpenL1f0L2Filtered7NHitQ15",
                        "hltL3fL1sL1SingleMu3OpenL1f0L2f0L3Filtered3NHitQ10",
                        "hltL3fL1sL1SingleMu3OpenL1f0L2f0L3Filtered5NHitQ10",
                        "hltL3fL1sL1SingleMu3OpenL1f0L2f0L3Filtered7NHitQ10",
                        "hltL3fL1sL1SingleMu3OpenL1f7L2f0L3Filtered12",
                        "hltL3fL1sL1SingleMu3OpenL1f7L2f0L3Filtered15",
                        "hltL3fL1sL1SingleMu3OpenL1f7L2f0L3Filtered20",
			)
                }

## Global tag
if isMC:
  globalTag = '103X_upgrade2018_realistic_HI_v6'
else:
  globalTag = '103X_dataRun2_Prompt_v3'

#----------------------------------------------------------------------------

# load the Geometry and Magnetic Field
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

# Global Tag:
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globalTag, '')
### For Centrality
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
print('\n\033[31m~*~ USING CENTRALITY TABLE FOR PbPb 2018 ~*~\033[0m\n')
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        label = cms.untracked.string("HFtowers")
        ),
    ])

#----------------------------------------------------------------------------

# For OniaTree Analyzer
from HiAnalysis.HiOnia.oniaTreeAnalyzer_cff import oniaTreeAnalyzer
oniaTreeAnalyzer(process, muonTriggerList=triggerList, HLTProName=HLTProcess, muonSelection=muonSelection, useL1Stage2=True, isMC=isMC, outputFileName=options.outputFile)

#process.onia2MuMuPatGlbGlb.dimuonSelection = cms.string("8 < mass && mass < 14 && charge==0 && abs(daughter('muon1').innerTrack.dz - daughter('muon2').innerTrack.dz) < 25")
process.hionia.minimumFlag      = cms.bool(keepExtraColl)           #for Reco_trk_*
process.hionia.useGeTracks      = cms.untracked.bool(keepExtraColl) #for Reco_trk_*
process.hionia.fillRecoTracks   = cms.bool(keepExtraColl)           #for Reco_trk_*
process.hionia.CentralitySrc    = cms.InputTag("hiCentrality")
process.hionia.CentralityBinSrc = cms.InputTag("centralityBin","HFtowers")
process.hionia.srcTracks        = cms.InputTag("generalTracks")
#process.hionia.muonLessPV       = cms.bool(False)
process.hionia.primaryVertexTag = cms.InputTag("offlinePrimaryVertices")
process.hionia.genParticles     = cms.InputTag("genParticles")

if applyEventSel:
    process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
    process.load('HeavyIonsAnalysis.EventAnalysis.clusterCompatibilityFilter_cfi')
    process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
    process.oniaTreeAna.replace(process.hionia, process.centralityBin * process.hfCoincFilter2Th4 * process.primaryVertexFilter * process.clusterCompatibilityFilter * process.hionia )

#----------------------------------------------------------------------------

# For HLTBitAnalyzer
process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName              = HLTProcess
process.hltbitanalysis.hltresults                  = cms.InputTag("TriggerResults","",HLTProcess)
process.hltbitanalysis.l1tAlgBlkInputTag           = cms.InputTag("hltGtStage2Digis","",HLTProcess)
process.hltbitanalysis.l1tExtBlkInputTag           = cms.InputTag("hltGtStage2Digis","",HLTProcess)
process.hltbitanalysis.gObjectMapRecord            = cms.InputTag("hltGtStage2ObjectMap","",HLTProcess)
process.hltbitanalysis.gmtStage2Digis              = cms.string("hltGtStage2Digis")
process.hltbitanalysis.caloStage2Digis             = cms.string("hltGtStage2Digis")
process.hltbitanalysis.UseL1Stage2                 = cms.untracked.bool(True)
process.hltbitanalysis.getPrescales                = cms.untracked.bool(False)
process.hltbitanalysis.getL1InfoFromEventSetup     = cms.untracked.bool(False)
process.hltbitanalysis.UseTFileService             = cms.untracked.bool(True)
process.hltbitanalysis.RunParameters.HistogramFile = cms.untracked.string(options.outputFile)
process.hltbitanalysis.RunParameters.isData        = cms.untracked.bool(not isMC)
process.hltbitanalysis.RunParameters.Monte         = cms.bool(isMC)
process.hltbitanalysis.RunParameters.GenTracks     = cms.bool(False)
if (HLTProcess == "HLT") :
	process.hltbitanalysis.l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis","","RECO")
	process.hltbitanalysis.l1tExtBlkInputTag = cms.InputTag("gtStage2Digis","","RECO")
	process.hltbitanalysis.gmtStage2Digis    = cms.string("gtStage2Digis")
	process.hltbitanalysis.caloStage2Digis   = cms.string("gtStage2Digis")
        if saveHLTBit:
          process.hltBitAna = cms.EndPath(process.hltbitanalysis)
#
##----------------------------------------------------------------------------
#
# For HLTObject Analyzer
process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_cfi")
process.hltobject.processName = cms.string(HLTProcess)
process.hltobject.treeName = cms.string(options.outputFile)
process.hltobject.loadTriggersFromHLT = cms.untracked.bool(False)
process.hltobject.triggerNames = triggerList['DoubleMuonTrigger'] + triggerList['SingleMuonTrigger']
process.hltobject.triggerResults = cms.InputTag("TriggerResults","",HLTProcess)
process.hltobject.triggerEvent   = cms.InputTag("hltTriggerSummaryAOD","",HLTProcess)
if saveHLTobj:
  process.hltObjectAna = cms.EndPath(process.hltobject)

#----------------------------------------------------------------------------
#Options:
process.source = cms.Source("PoolSource",
#process.source = cms.Source("NewEventStreamFileReader", # for streamer data
		fileNames = cms.untracked.vstring( options.inputFiles ),
		)
process.TFileService = cms.Service("TFileService", 
		fileName = cms.string( options.outputFile )
		)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.schedule  = cms.Schedule( process.oniaTreeAna )
#process.schedule  = cms.Schedule( process.oniaTreeAna , process.hltBitAna , process.hltObjectAna )
