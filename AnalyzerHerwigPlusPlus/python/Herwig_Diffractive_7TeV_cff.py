import FWCore.ParameterSet.Config as cms

from GenLevelAnalyzer.AnalyzerHerwigPlusPlus.HerwigLHCDiffractive_cfi import *

generator = cms.EDFilter(
    "ThePEGGeneratorFilter",
    herwigDefaultsBlock,
    configFiles = cms.vstring(),
    parameterSets = cms.vstring(
    'cm7TeV',
    'basicSetup',
    'powhegDefaults',
    'diffractiveDefaults',
    'setParticlesStableForDetector'
    ),
    crossSection     = cms.untracked.double(1.0),
    filterEfficiency = cms.untracked.double(1.0)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision: 1.0 $'),
    name = cms.untracked.string('\$Source: Herwig_Diffractive_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('Process: (Z->ll), l=e or mu')
)
