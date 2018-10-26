import FWCore.ParameterSet.Config as cms


from DQM.HLTEvF.HLTObjectMonitorLeadLead_cfi import *

hlt4vector = cms.Path(
    hltObjectMonitorLeadLead
)
